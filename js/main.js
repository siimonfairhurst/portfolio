/* ==========================================================================
   Simon Fairhurst · Portfolio — Shared behaviour
   Runs on every page. Each block guards for the elements it needs, so this
   single file works on both index.html and the case-study pages.
   ========================================================================== */

(function () {
  'use strict';

  /* ---- Live Manchester clock (always UK local time, regardless of visitor) ---- */
  function startClock() {
    const nodes = document.querySelectorAll('[data-clock]');
    if (!nodes.length) return;
    function tick() {
      const now = new Date();
      const time = now.toLocaleTimeString('en-GB', {
        timeZone: 'Europe/London',
        hour12: false,
        hour: '2-digit', minute: '2-digit', second: '2-digit'
      });
      nodes.forEach((n) => { n.textContent = 'Manchester, UK · ' + time; });
    }
    tick();
    setInterval(tick, 1000);
  }

  /* ---- Home: Selected work / All work toggle ---- */
  function initHomeNav() {
    const navButtons = document.querySelectorAll('[data-home-nav]');
    const views = document.querySelectorAll('[data-view]');
    const subnav = document.querySelector('.subnav');
    const keyline = document.querySelector('.nav-keyline');
    const bottomToggle = document.querySelector('.bottombar__toggle');
    const bottombar = document.querySelector('.bottombar');
    if (!navButtons.length) return;

    function setHomeView(name) {
      navButtons.forEach((b) => b.setAttribute('aria-current', String(b.dataset.homeNav === name)));
      views.forEach((v) => v.setAttribute('data-active', String(v.dataset.view === name)));
      if (subnav) subnav.style.display = name === 'selected' ? 'flex' : 'none';
      if (bottomToggle) bottomToggle.style.display = name === 'selected' ? 'flex' : 'none';
      if (bottombar) bottombar.classList.toggle('bottombar--static', name === 'all');
      if (keyline) keyline.style.display = '';
    }

    navButtons.forEach((b) => b.addEventListener('click', () => setHomeView(b.dataset.homeNav)));
    setHomeView('selected'); // always reset to default on load
  }

  /* ---- Selected Work: Ecommerce/SaaS sub-nav + Stacked/Swipe toggle ----
     These two controls are independent axes of the same state (which
     category is showing, and in which display mode), so they're handled
     by one controller rather than two toggles fighting over the same
     elements' inline styles. */
  function initSelectedWorkControls() {
    const subButtons = document.querySelectorAll('[data-subnav]');
    const toggleButtons = document.querySelectorAll('[data-display-toggle]');
    const groups = document.querySelectorAll('[data-category-group]');
    if (!subButtons.length && !toggleButtons.length) return;

    function isMobile() { return window.innerWidth <= 780; }

    let category = 'ecommerce';
    let mode = 'stacked'; // default, never persisted across reloads per brief

    function render() {
      const effectiveMode = isMobile() ? 'swipe' : mode;
      subButtons.forEach((b) => b.setAttribute('aria-current', String(b.dataset.subnav === category)));
      toggleButtons.forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.displayToggle === effectiveMode)));
      groups.forEach((g) => {
        const matches = g.dataset.categoryGroup === category && g.dataset.display === effectiveMode;
        const isVisible = g.style.display && g.style.display !== 'none';

        if (matches) {
          if (!isVisible) {
            g.style.display = g.dataset.display === 'swipe' ? 'flex' : 'block';
            g.classList.remove('stage-in');
            void g.offsetWidth; // force reflow so the transition actually plays
          }
          g.classList.add('stage-in');
          if (g.dataset.display === 'stacked') {
            g.classList.remove('is-entering');
            void g.offsetWidth;
            g.classList.add('is-entering');
            // cardEnter uses fill-mode "both" so its final keyframe keeps
            // overriding .stacked-card's transform (and therefore the
            // hover-tilt) for as long as is-entering stays on the group.
            // Longest stagger is 5 cards * 70ms delay + the .55s animation
            // itself; clear the class once that's safely finished so normal
            // hover styles (including tilt) take back over.
            clearTimeout(g._enteringTimeout);
            g._enteringTimeout = setTimeout(() => {
              g.classList.remove('is-entering');
            }, 900);
          }
        } else if (isVisible) {
          g.classList.remove('stage-in');
          g.classList.remove('is-entering');
          setTimeout(() => {
            if (!g.classList.contains('stage-in')) g.style.display = 'none';
          }, 280);
        } else {
          g.style.display = 'none';
        }
      });
    }

    subButtons.forEach((b) => b.addEventListener('click', () => { category = b.dataset.subnav; render(); }));
    toggleButtons.forEach((b) => b.addEventListener('click', () => { mode = b.dataset.displayToggle; render(); }));
    window.addEventListener('resize', render);
    render();
  }

  /* ---- Shared tilt + shine binder, used by both the stacked deck and the
     swipe deck. `canTilt`, if given, is checked on every mousemove and lets
     a card opt out on the fly (used by Swipe to disable tilt on background
     cards and mid-drag, since dragging overwrites transform directly). ---- */
  const TILT_MAX_DEG = 10; // kept restrained rather than a full arcade tilt

  function bindTiltAndShine(el, canTilt) {
    el.addEventListener('mousemove', (e) => {
      if (canTilt && !canTilt(el)) return;
      const rect = el.getBoundingClientRect();
      const px = (e.clientX - rect.left) / rect.width;  // 0 (left) → 1 (right)
      const py = (e.clientY - rect.top) / rect.height;  // 0 (top) → 1 (bottom)
      const ry = (px - 0.5) * 2 * TILT_MAX_DEG;           // left/right cursor → rotateY
      const rx = (0.5 - py) * 2 * TILT_MAX_DEG;            // up/down cursor → rotateX
      el.classList.add('is-tilting');
      el.style.setProperty('--rx', rx.toFixed(2) + 'deg');
      el.style.setProperty('--ry', ry.toFixed(2) + 'deg');
      // Shine position tracks the same cursor coordinates as the tilt.
      el.style.setProperty('--shine-x', (px * 100).toFixed(1) + '%');
      el.style.setProperty('--shine-y', (py * 100).toFixed(1) + '%');
    });
    el.addEventListener('mouseleave', () => {
      el.classList.remove('is-tilting');
      el.style.setProperty('--rx', '0deg');
      el.style.setProperty('--ry', '0deg');
    });
  }

  /* ---- Stacked cards: hover tilt. Bring-to-front is still handled by CSS
     z-index (see .stacked-card:hover) — this only adds a pointer-tracked
     rotateX/rotateY on top of the existing --tx/--ty fan position. Sets
     --rx/--ry as inline custom properties so it never touches the fan
     layout values already on the element. ---- */
  function initCardTilt() {
    const cards = document.querySelectorAll('.stacked-card');
    if (!cards.length) return;
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    cards.forEach((card) => bindTiltAndShine(card));
  }


  /* ---- Swipe view: a real card stack you swipe through — the current
     card sits on top, the next couple peek out behind it (scaled down),
     and swiping/clicking through advances the whole deck rather than
     crossfading between two flat cards. ---- */
  function initSwipeCards() {
    document.querySelectorAll('[data-swipe-group]').forEach((group) => {
      const cards = Array.from(group.querySelectorAll('.swipe-card-wrap'));
      const n = cards.length;
      if (!n) return;
      let current = 0;
      const prevBtn = group.parentElement.querySelector('.swipe-chevron--prev');
      const nextBtn = group.parentElement.querySelector('.swipe-chevron--next');

      function place(el, d) {
        const depth = Math.min(d, 2);
        el.style.setProperty('--depth', depth);
        el.style.zIndex = String(n - depth);
        el.style.opacity = d > 2 ? '0' : (depth === 2 ? '0.9' : '1');
        el.classList.toggle('is-top', d === 0);
      }

      function layout(skipEl) {
        cards.forEach((el, i) => {
          if (el === skipEl) return;
          el.classList.remove('is-exiting');
          el.style.transition = '';
          el.style.transform = '';
          place(el, (i - current + n) % n);
        });
      }

      function goTo(nextIndex, exitEl, direction) {
        if (exitEl) {
          exitEl.classList.add('is-exiting');
          exitEl.style.transition = 'transform .28s ease, opacity .28s ease';
          exitEl.style.transform = `translateX(${direction * 620}px) rotate(${direction * 12}deg)`;
          exitEl.style.opacity = '0';
        }
        current = (nextIndex + n) % n;
        if (exitEl) {
          setTimeout(() => layout(), 280);
          cards.forEach((el) => { if (el !== exitEl) place(el, (cards.indexOf(el) - current + n) % n); });
        } else {
          layout();
        }
      }

      if (prevBtn) prevBtn.addEventListener('click', () => goTo(current - 1, cards[current], 1));
      if (nextBtn) nextBtn.addEventListener('click', () => goTo(current + 1, cards[current], -1));

      const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

      cards.forEach((wrap) => {
        let startX = null;
        let dragging = false;

        if (!reduceMotion) {
          bindTiltAndShine(wrap, (el) => el.classList.contains('is-top') && !el.classList.contains('is-dragging'));
        }

        wrap.addEventListener('pointerdown', (e) => {
          if (e.target.closest('.swipe-cta')) return;
          if (!wrap.classList.contains('is-top')) return;
          startX = e.clientX;
          dragging = true;
          wrap.classList.add('is-dragging');
          // Drop any tilt in progress — dragging takes over the transform
          // property directly, so a leftover rotate would otherwise
          // reappear the instant the drag ends and the inline override
          // clears.
          wrap.classList.remove('is-tilting');
          wrap.style.setProperty('--rx', '0deg');
          wrap.style.setProperty('--ry', '0deg');
          wrap.setPointerCapture(e.pointerId);
        });
        wrap.addEventListener('pointermove', (e) => {
          if (!dragging || startX === null) return;
          const dx = e.clientX - startX;
          wrap.style.transform = `translateX(${dx}px) rotate(${dx / 24}deg)`;
        });
        function endDrag(e) {
          if (!dragging) return;
          dragging = false;
          wrap.classList.remove('is-dragging');
          const dx = e.clientX - startX;
          if (dx < -80) goTo(current + 1, wrap, -1);
          else if (dx > 80) goTo(current - 1, wrap, 1);
          else { wrap.style.transform = ''; }
          startX = null;
        }
        wrap.addEventListener('pointerup', endDrag);
        wrap.addEventListener('pointercancel', endDrag);
      });

      layout();
    });
  }

  /* ---- All Work: filter row (Type) + sort stub ---- */
  function initAllWorkFilters() {
    const filterButtons = document.querySelectorAll('[data-filter]');
    const cards = document.querySelectorAll('[data-project-type]');
    const emptyState = document.querySelector('.allwork__empty');
    if (!filterButtons.length) return;

    function applyFilter(type) {
      filterButtons.forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.filter === type)));
      let visible = 0;
      cards.forEach((c) => {
        const show = type === 'all' || c.dataset.projectType === type;
        c.style.display = show ? '' : 'none';
        if (show) visible++;
      });
      if (emptyState) emptyState.style.display = visible === 0 ? 'block' : 'none';
    }
    filterButtons.forEach((b) => b.addEventListener('click', () => applyFilter(b.dataset.filter)));
    applyFilter('all');

    // Sort toggle is stubbed for v1 — needs a completion date + impact ranking
    // per project before it can do anything real (see brief §8, open question 5).
    document.querySelectorAll('[data-sort]').forEach((b) => {
      b.setAttribute('disabled', 'true');
      b.setAttribute('aria-disabled', 'true');
      b.title = 'Coming soon — needs a completion date and impact ranking per project';
    });
  }

  /* ---- Case study hero header entrance. Re-triggers the fade/slide-up
     every time the page is shown, including a second visit — a plain CSS
     `animation` only plays once per document and silently skips on a
     back/forward cache restore.
     Uses `pagereveal` + the transition's own `finished` promise (not
     `pageshow`) because pageshow fires too early relative to the browser's
     own cross-document view-transition lifecycle: if the fade-in starts
     while the transition is still capturing its "new page" snapshot, that
     frozen snapshot can catch the header mid-animation, and handing off
     to the live DOM afterwards then shows as a jump. Waiting for
     viewTransition.finished guarantees the handoff has already happened.
     Falls back to pageshow on browsers without pagereveal support. ---- */
  function initCsHeaderEnter() {
    const header = document.querySelector('.cs-header');
    if (!header) return;

    function play() {
      header.classList.remove('is-entering');
      void header.offsetWidth; // force reflow so the animation restarts
      header.classList.add('is-entering');
    }

    if ('onpagereveal' in window) {
      window.addEventListener('pagereveal', (e) => {
        if (e.viewTransition) {
          e.viewTransition.finished.then(play, play);
        } else {
          play();
        }
      });
    } else {
      window.addEventListener('pageshow', play);
    }
  }

  /* ---- Force every navigation to be a fresh page load rather than a
     back/forward cache restore. Cross-document View Transitions can behave
     inconsistently when either end of a navigation comes from bfcache
     instead of a genuine parse — the browser's native card-to-hero morph
     is pure CSS/browser behaviour with no JS hook to retrigger it (unlike
     the header fade-in above), so the only reliable fix is to prevent the
     inconsistent state from happening at all. A no-op `unload` listener is
     the standard way to opt a page out of bfcache eligibility in Chrome.
     Trade-off: back/forward navigation loses bfcache's instant restore,
     in exchange for the hero transition always firing correctly. ---- */
  window.addEventListener('unload', () => {});

  document.addEventListener('DOMContentLoaded', () => {
    startClock();
    initHomeNav();
    initSelectedWorkControls();
    initCardTilt();
    initSwipeCards();
    initAllWorkFilters();
    initCsHeaderEnter();
  });
})();
