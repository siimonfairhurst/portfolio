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
        g.style.display = matches ? (g.dataset.display === 'swipe' ? 'flex' : 'block') : 'none';
      });
    }

    subButtons.forEach((b) => b.addEventListener('click', () => { category = b.dataset.subnav; render(); }));
    toggleButtons.forEach((b) => b.addEventListener('click', () => { mode = b.dataset.displayToggle; render(); }));
    window.addEventListener('resize', render);
    render();
  }

  /* ---- Stacked cards: hover/focus lift handled entirely by CSS (see .stacked-card:hover).
     Base fan positions are set inline per-card at build time via --tx/--ty/--rot/--z. ---- */

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

      cards.forEach((wrap) => {
        let startX = null;
        let dragging = false;

        wrap.addEventListener('pointerdown', (e) => {
          if (e.target.closest('.swipe-cta')) return;
          if (!wrap.classList.contains('is-top')) return;
          startX = e.clientX;
          dragging = true;
          wrap.classList.add('is-dragging');
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

  document.addEventListener('DOMContentLoaded', () => {
    startClock();
    initHomeNav();
    initSelectedWorkControls();
    initSwipeCards();
    initAllWorkFilters();
  });
})();
