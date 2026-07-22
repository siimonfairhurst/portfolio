# -*- coding: utf-8 -*-
"""
Builds index.html and every case-studies/*.html from one data source.
Run: python3 build_site.py
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# PROJECT DATA
# Copy pulled from Simon's Notion case-study pages (source of truth) where
# they exist, cross-checked against the Figma mockups for structure/order.
# ---------------------------------------------------------------------------

PROJECTS = [
    dict(
        slug="playstation-gear", name="PlayStation Gear", category="ecommerce",
        accent="#1849E8",
        tag="Global eCommerce · Entertainment", stat="3M+ sessions, 82k monthly visits",
        agency="E3creative (now DEPT®)", role="Head of Design",
        platform="Global e-commerce, custom build (PHP, Laravel)",
        timeline="6 week MVP build, followed by years of ongoing CRO and feature work",
        ownership="UX strategy, creative direction, design system",
        team="8 people — design, copy, motion, marketing, development, PM",
        live_url="https://www.playstation.com/en-gb/horizon/merchandise/",
        headline="Built for Players, Not Just Buyers",
        overview="PlayStation Gear is the official global merchandise store for Sony PlayStation, built for an 80 million strong player base to shop official clothing, accessories and collectibles. I led design from discovery through to launch and years of post-launch iteration. It scaled to over 3 million sessions a year, cut checkout drop-off by 73%, and won four industry awards.",
        results=[
            "3M+ sessions a year (650k organic, 500k paid), up from zero search visibility pre-launch",
            "Checkout cut to 3 clicks, reducing basket drop-off by 73%",
            "2,000+ core search queries ranked, up from 250 before launch",
            "4 industry awards, including Awwwards E-commerce Platform of the Year",
        ],
        challenge=["PlayStation didn't have a proper home for its merchandise. What existed felt generic rather than built for gamers, and it wasn't doing the brand any favours. Sony needed somewhere as immersive as the products themselves, capable of handling complex global commerce and multiple brand franchises, on a tight deadline tied to E3 and Days of Play."],
        approach=[
            "As hands-on Head of Design, leading a team of 8 across design, content, motion and development, I ran a three day discovery workshop with Sony to nail down business goals, customer needs and information architecture.",
            "The standout insight: nine out of ten customers were hesitant to hand over personal details at registration, which is what led me to simplify checkout down to the bare minimum, the decision behind the project's strongest result.",
            "From there I led art direction and the design system myself, working closely with our Senior UX Designer on wireframes, building everything around atomic design so components stayed consistent but could flex for dark mode and different brand franchises like Call of Duty and Horizon.",
            "Sony's brand guidelines were strict, governing everything down to CTA styling and image crops, and I spent a fair amount of time pushing back to Sony's marketing directors and brand guardians on where those rules genuinely served the user versus where they just made the experience feel less like PlayStation Gear and more like a generic Sony page.",
            "One deliberate call I made: analytics showed only 15% of traffic was mobile, so I designed desktop first rather than defaulting to mobile first. I tested constantly throughout, using LookBack, UserTesting.com and Hotjar to validate real user behaviour, not just internal assumptions.",
            "Design itself started in Sketch and Adobe XD, moving over to Figma later as the platform's life stretched on for years.",
        ],
        outcome=[
            "The MVP launched on time for E3 and Days of Play, growing from zero search visibility to over 3 million sessions a year. The standout design metric: cutting checkout down to 3 clicks reduced basket drop-off by 73%, real evidence the UX decisions were doing the heavy lifting, not just the marketing push. Those same decisions, the simplified checkout, the flexible design system and the immersive art direction, are what the platform was recognised for, picking up four industry awards including Awwwards' E-commerce Platform of the Year.",
            "I stayed on for years after to lead conversion rate optimisation and continued feature work: game landing pages, a redesigned navigation, expanded checkout options and a full dark mode rollout once data showed 85% of customers preferred it, alongside seasonal marketing campaigns for Black Friday and Valentine's Day that kept the platform evolving well beyond the initial launch.",
        ],
        reflection=["What stands out most looking back is how much of the long term success traced back to a single insight from those first three days of workshops, not a redesign years later, but the decision to simplify checkout based on what customers told me upfront. It's the project that shaped how I still work now: dig for the real friction before touching a single screen, then defend that decision through whatever constraints come after, whether that's a brand guideline or a stakeholder who'd rather play it safe."],
        order_allwork=1, order_selected=1,
    ),
    dict(
        slug="outside-in", name="Outside-In", category="ecommerce",
        accent="#BEAC8E", card_dark_text=True,
        tag="eCommerce · D2C Beauty", stat="+441% gross sales growth",
        agency="Series Eight", role="Design Director",
        platform="D2C beauty e-commerce (Shopify)",
        timeline="6 weeks",
        ownership="UX strategy, Information Architecture, design system",
        team="Design (with one supporting designer), Development, PM",
        live_url="https://theoutsidein.com/",
        headline="A Shade Finder That Shaped Everything",
        overview="Outside In is a premium beauty brand launching into a crowded D2C market. The site made $60k in revenue in its first 7 days. I led design end to end, from discovery through to launch, working alongside one supporting designer, with development, PM, copywriting and marketing collaborating through delivery. The brand's core problem wasn't traffic, it was confidence. Customers didn't trust they'd picked the right foundation shade without seeing it in person, and that uncertainty was sending people in-store instead of online.",
        results=[
            "$60k revenue in first 7 days",
            "441% growth in gross sales post-launch ($432K)",
            "60% increase in returning customers",
            "98.5% of testers felt more confident choosing a shade",
        ],
        challenge=["Launching a premium beauty brand into a saturated market is hard enough. Outside In's specific problem was shade selection. Marketing was driving a highly engaged social audience to the site, but customers weren't confident enough in choosing the right foundation shade to commit to a purchase. Small swatch elements weren't giving people enough to go on, so a meaningful chunk of demand was leaking to physical retail instead."],
        approach=[
            "I started with a visual audit against the brand's new positioning, \u201cExperience Light\u201d, testing accessibility and contrast early to define the colour and type direction. A competitor and aspirational-brand review surfaced a clear gap: everyone was relying on small, low-context swatches to sell a highly personal decision.",
            "To validate that, I spoke to 30+ existing customers about what stopped them buying online. The answer was consistent: shade confidence. That finding reshaped the project. Shade selection stopped being a UI detail and became the site's central feature.",
            "Information Architecture stayed deliberately lean, a visually-led homepage, focused collection pages, and a brand story page, since marketing was handled entirely off-platform and the site's only job was converting that traffic. I made the call to skip wireframes and go straight into UI exploration, a decision that worked because the scope was narrow enough to validate against the real experience rather than a low-fidelity one, and it kept the project moving against a hard deadline.",
            "I led creative direction across four visual routes, then built a fully documented atomic design system in Figma, working sprint by sprint so design and system stayed in step. The centrepiece was the shade finder: individual model shots for every shade, built into an interactive slider with development. It tested well, 98.5% of over 30 testers said it made them feel more confident choosing a shade than on any other site they'd used.",
        ],
        outcome=[
            "Post-launch performance held up well beyond the initial spike. Gross sales grew 441% ($432K), orders were up 498% (4,363), and sessions grew 503% (149K) against the prior period. Revenue and traffic scaled almost in lockstep, so growth wasn't just riding a paid or PR bump.",
            "The number I'd point to first is returning customers, up 60% and now 10.2% of the base. That's the shade finder doing its job beyond the initial purchase, giving people enough confidence to come back. Product pages alone pulled 95K+ sessions as the top acquisition entry point.",
        ],
        reflection=["This project is a good example of research directly reshaping scope. The shade finder wasn't in the original brief, it came out of listening to customers and being willing to make it the centre of the site rather than a nice-to-have feature."],
        order_allwork=2, order_selected=2,
    ),
    dict(
        slug="nikon", name="Nikon", category="ecommerce",
        accent="#F5D900",
        tag="Global eCommerce · Enterprise", stat="36 markets unified",
        agency="DEPT®", role="Head of Design",
        platform="Web — custom commerce build on Sitecore",
        timeline="2021–2022",
        ownership="Creative direction, UX strategy, Information Architecture, design system, cross-market platform consolidation, CRO",
        team="Designer, two UX designers, project manager, internal data team",
        live_url="https://www.nikon.co.uk/en_GB",
        headline="36 Markets, One Design System",
        overview="Nikon's European operation was running off 36 separate regional sites, each with its own journeys and inconsistent standards. As Head of Design I set the creative direction and led the consolidation into a single, unified commerce and content platform, working hands on across the key flows, pages and design system alongside the wider team. The result was a 36% lift in conversion rate and an ~18% increase in average order value.",
        results=[
            "+36% conversion rate",
            "+~18% average order value through checkout upselling",
            "36 regional markets unified under one platform",
            "New B2B purchasing capability built alongside consumer journey",
            "One design system governing all markets",
        ],
        challenge=[
            "Nikon Europe's digital presence had grown market by market with no shared structure, so every region had its own version of the journey, its own inconsistencies, and almost no visibility across the business as a whole. Each market also had its own regional manager with their own priorities and opinions on how their site should work, so getting everyone aligned behind one shared platform was as much a stakeholder challenge as a design one.",
            "The brand guidelines we had to work from were also badly out of date, which meant pushing for a more modern direction while still keeping things recognisably Nikon. On top of that, B2B was the core business driver behind the whole rebuild — so this wasn't just a redesign, it meant building genuinely new commerce capability into the front and back end from scratch. It was one of the largest projects in scope I worked on at DEPT®.",
        ],
        approach=[
            "Given the scale, I broke the project into four phases, each with its own sprints, so the team could tackle the workload without losing momentum or control: Phase 1 — core site rebuild and ecommerce foundations, Phase 2 — Schools section and Account, Phase 3 — checkout journey, Phase 4 — B2B portals and purchasing systems.",
            "Getting 36 regional managers to align behind one shared structure meant the design system also had to work as a negotiation tool — a way to show each market what they'd gain from standardising, not just what they'd be giving up.",
            "I set the early creative concepts and direction, then worked hands on with the team on the most complex flows, the design system and key pages, while overseeing the rest of the design output as Head of Design. The design system was treated as the backbone of the project rather than a side deliverable — it's what kept design and development aligned across a build of this size and let standardised journeys scale across 36 markets instead of being rebuilt market by market.",
            "We worked closely with an internal data team throughout, using their insight to prioritise CRO opportunities on key pages. One of the clearest wins came in checkout, where introducing relevant accessory upsells lifted average order value by around 18%. We backed decisions like this with user testing and A/B testing rather than relying on instinct alone.",
        ],
        outcome=["The 36 separate market sites became one unified, scalable commerce platform, with new B2B purchasing capability built in alongside the consumer journey — centralised governance cut operational overhead across all markets, and A/B testing plus user testing are now baked in as an ongoing CRO foundation."],
        reflection=["This is one of the clearest examples of how a design system pays for itself on a big enough project, and how pairing strong creative direction with real data and testing turns a consolidation project into something that keeps improving long after launch."],
        order_allwork=3, order_selected=3,
    ),
    dict(
        slug="notwoways", name="NoTwoWays", category="ecommerce",
        accent="#E94E1A",
        tag="D2C · Fashion Drop", stat="5,000 pairs sold in 11 minutes",
        agency="Series Eight", role="Design Director",
        platform="Shopify, D2C fashion e-commerce, drop based",
        timeline="6 weeks for the initial release, plus ongoing support across multiple future drops",
        ownership="Creative direction, UX, release flows",
        team="Design Director (hands-on) + 1 Senior Designer, 1 Developer, 1 Project Manager, 1 Copywriter",
        live_url="https://www.notwoways.com/",
        headline="Sold Out In 11 Minutes",
        overview="NoTwoWays, the sneaker brand founded by YouTuber Callux (of the Sidemen) and designer Rocky Princely, needed a drop experience built to handle a fanbase in the millions. I led creative direction and UX for the launch of the ARW Subsolar, built on Shopify, balancing storytelling with a checkout that couldn't buckle under pressure. The result: 5,000 pairs sold out in 11 minutes, generating £500k in revenue, success that led to an ongoing relationship supporting several more releases.",
        results=[
            "5,000 pairs sold out in 11 minutes (£500k revenue)",
            "150% more stock supported vs the previous drop",
            "37k+ pre-launch views via creator and Hypebeast traffic",
            "Contributed to a £2.3m investment round later that year",
        ],
        challenge=["NoTwoWays had already built a loyal following through fast, high-demand drops, early releases had sold out hundreds of pairs in under a minute. The ARW Subsolar release needed to go further: support significantly more stock, hold up against a much bigger traffic spike driven by Callux's creator audience and Hypebeast coverage, and still feel like an event rather than just a queue. Getting the balance wrong meant either lost sales or a site crashing in front of millions of fans."],
        approach=[
            "The client came to us as Shopify experts, and building the drop on Shopify gave us a strong performance foundation to work with, which mattered a lot given the traffic spikes a release like this would pull in.",
            "On top of that platform, the brand had serious in-house media firepower, videographers and content creators producing high volumes of hype content ahead of every drop, and my job was to give that content a home without letting it get in the way of conversion. I built out a pre-launch landing experience packed with interactive features designed to build anticipation: sliders, 360º product visualisations, short film pieces, motion effects, and gamified elements that gave fans a reason to keep coming back before the drop went live.",
            "That meant working closely and iteratively with the client's content team, reviewing what they were producing, figuring out where it could sit on the site, and pushing back where a piece of content risked slowing the page down or distracting from the eventual conversion moment. A lot of this came down to stakeholder and expectation management, keeping the client's ambition for a spectacular pre-launch experience aligned with the hard requirement that the site still convert cleanly the second the drop went live.",
            "On the release side itself, I designed a stripped-back, high-speed checkout flow, deliberately separate from the immersive pre-launch experience, built to hold up under extreme concurrent traffic. With the model proven, I carried the same hands-on role, leading a small, focused team, across the Formula, Foams, ARW Afterdark, and ARW Apricity releases that followed.",
        ],
        outcome=["The drop sold out completely, all 5,000 pairs gone in 11 minutes, bringing in £500k in revenue while supporting 150% more stock than the brand's previous release, without the site buckling under the load. The pre-launch build-up did its job too, generating 37k+ views through creator and Hypebeast traffic before the drop even went live. It was enough to help NoTwoWays secure a £2.3m investment round later that year, and enough to earn an ongoing partnership with the brand, carrying the same approach through the Formula, Foams, ARW Afterdark, and ARW Apricity releases that followed."],
        reflection=["This was as much a stakeholder management job as a design one. The client had no shortage of ambition or content, my role was making sure all that energy channelled into a site that still converted cleanly the second it mattered most, a system that proved itself well enough to carry the relationship through several more releases."],
        order_allwork=4, order_selected=4,
    ),
    dict(
        slug="steamforged-games", name="Steamforged Games", category="ecommerce",
        accent="#A9ECB8",
        tag="Global eCommerce · Entertainment", stat="+261% revenue growth",
        agency="E3creative, during its transition into DEPT®", role="Head of Design",
        platform="Global e-commerce experience",
        timeline="6 months, plus ongoing post-launch support and optimisation",
        ownership="UX strategy, IA, UI design",
        team="UX Designer, Product Owner, Product Manager, Marketing, Copywriting, 2 Developers",
        live_url="https://steamforged.com/en-gb",
        headline="Cluttered Catalogues to Record Sales",
        overview="Steamforged Games is a Manchester-based tabletop publisher known for record-breaking Kickstarters and licensed adaptations like Dark Souls and Resident Evil. I led the redesign of their global e-commerce platform, restructuring how a fast-growing, licence-heavy catalogue got discovered and bought. Conversion rate jumped 126% post-launch, with e-commerce revenue up 261%.",
        results=[
            "+126% conversion rate",
            "+261% e-commerce revenue post-launch",
            "+160% pages per session",
            "+46% global sessions",
            "Awwwards Honorable Mention · The Drum Award",
        ],
        challenge=["Steamforged's catalogue was expanding fast, new licensed titles, expansions, and limited runs launching constantly, but the site couldn't keep pace. Discovery was clunky, and the structure didn't clearly separate core games, expansions, and merchandise the way fans actually shopped. Customers were also asking for details the site didn't give them: figure scale, materials, box contents, the specifics hobbyists need before committing to a purchase. That gap meant hesitant buyers and a steady stream of support tickets asking questions the product pages should have already answered."],
        approach=[
            "I started by auditing the existing site and analytics to find where discovery was breaking down, then benchmarked against other tabletop and hobby brands to see how the best in the category handled complex catalogues. Talking to Steamforged's own community surfaced the real insight: fans didn't just want a nicer-looking site, they wanted the specific product details that let them buy with confidence, figure scale, materials, box contents, the stuff hobbyists check before committing.",
            "That became the core of the redesign. I built a modular product page system anchored around a dedicated specification panel on every game, so that detail sat right alongside the immersive brand storytelling rather than replacing it. Category pages were rebuilt for scanning and filtering across franchises and product types, so browsing a catalogue that spanned dozens of licensed titles finally felt manageable. To keep the wider team shipping new titles at pace after launch, I also built out a component library in Figma, so new products could go live without design starting from scratch each time.",
        ],
        outcome=["The rebuilt platform gave Steamforged a structure that could keep pace with its release schedule. Conversion rate rose 126% and e-commerce revenue grew by 261% post-launch, with pages per session up 160% as fans explored deeper into the catalogue instead of bouncing off it, and global sessions up 46%. Support tickets tied to product clarity dropped, a direct result of the specification panels answering questions fans used to have to raise separately. The new structure also proved itself under pressure: when paid search and shopping campaigns launched around US Black Friday, the platform handled the spike and converted it, with traffic up 27% and revenue up 18% over that weekend. The work picked up an Awwwards Honorable Mention and a Drum Award."],
        reflection=["This project was a good reminder that even the most visual, brand-led experiences still need to answer specific, practical questions clearly. Storytelling and structured information aren't in competition, they need each other."],
        order_allwork=5, order_selected=5,
    ),
    dict(
        slug="triumph-motorcycles", name="Triumph Motorcycles", category="ecommerce",
        accent="#FF9595",
        tag="D2C · Automotive", stat="3D configurator, pre-dealer engagement",
        agency="DEPT®", role="Principal Designer",
        platform="D2C automotive product experience",
        timeline="Multi-phase programme (2020–2021)",
        ownership="UX strategy, Information Architecture, design systems, configurator experience, 3D art direction",
        team="Design, Unreal Engine 3D artists (directed by Simon), Development, PM — stakeholder lead: Triumph CMO",
        live_url="https://www.triumphmotorcycles.co.uk/",
        headline="From Spec Sheet to Digital Test Ride",
        overview="Triumph's Tiger range is packed with configuration options, colours, and accessories, and none of that complexity was translating online. Riders were left guessing at what a build would actually look like before they ever spoke to a dealer. I led the UX, design system, and configurator experience for a new online build tool, simplifying the decision path and pairing it with real-time 3D interaction so riders could see exactly what they were choosing, right down to finding the specific parts they needed. It gave Triumph a scalable configuration system that lifted engagement and purchase confidence ahead of dealer contact, and it went on to win DEPT® a global Sitecore Ultimate Experience Award.",
        results=[
            "Increased engagement across Tiger models and accessory exploration",
            "Reduced purchase friction via the new part finder",
            "Improved pre-dealer purchase confidence",
            "Delivered a scalable 3D configuration and design system, reusable across future launches",
            "Global Sitecore Ultimate Experience Award",
        ],
        challenge=["Configuring a Tiger motorcycle online meant working through layers of models, colourways, and accessory combinations with almost no visual feedback. Riders couldn't easily picture their build, which meant a lot of unresolved intent by the time they reached a dealer. Finding the right individual parts was just as hard, buried in dense catalogues with no clear route in. For Triumph, that was a missed opportunity to build purchase confidence earlier in the journey, and to give dealers a warmer, better-informed lead."],
        approach=[
            "I started with the task flows riders were actually trying to complete: which model, which trim, which accessories, in what order, with what dependencies. That research shaped a much simpler configuration journey, one that broke a genuinely complex product into clear, sequential decisions instead of a wall of options. I also designed a dedicated part finder, letting riders navigate visual diagrams and categories to land on the exact part for their bike rather than searching blind, cutting friction out of the purchase flow.",
            "The bigger call was pairing the configurator with real-time 3D interaction, so every choice a rider made was reflected instantly in a model they could rotate and inspect. I led, directed, and managed a team of Unreal Engine 3D artists to build fully accurate, fully customisable models of each bike, controllable down to colour and trim through a single precise render. That replaced what had been manual Photoshop edits for every trim variation with one system the wider team could keep updated indefinitely, a big shift in how Triumph could maintain the experience long after launch.",
            "None of that would have scaled without the design system underneath it. It started in Sketch and moved to Figma partway through, and getting tokens and atomic design principles properly embedded was one of the most important decisions on the project, it's what let the configurator, part finder, and 3D layer all stay consistent as the product grew. I worked directly with Triumph's CMO throughout to keep the wider stakeholder group aligned behind that system and the direction it was taking.",
            "Alongside the core build, I explored more immersive ways to bring the Tiger range to life, including interactive VR demonstrations, full 360° rotation models, and even engine audio samples, pushing the experience beyond a standard configurator into something closer to a virtual test ride. I also ran regular user testing on the configurator itself using Lookback, using what we learned to keep iterating the flow rather than treating launch as the finish line.",
        ],
        outcome=["The rebuilt configurator increased engagement across Tiger models and accessory exploration, and gave riders a clearer, more confident picture of their build before ever contacting a dealer. The part finder reduced friction in the purchase flow, and ongoing Lookback testing meant the experience kept improving after launch rather than staying static. Just as importantly, the 3D configuration system and the design system behind it were built to be reusable, giving Triumph a scalable foundation for future model launches rather than a one-off tool. The work was recognised with a global Sitecore Ultimate Experience Award, DEPT®'s only Triumph-related award win that year."],
        reflection=["This project reinforced something I come back to often: the best way to simplify a genuinely complex product isn't to strip information out, it's to sequence it, back it with a system that can scale, and let people see the consequences of their choices in real time."],
        order_allwork=6, order_selected=6,
    ),
    dict(
        slug="carv", name="Carv", category="saas",
        accent="#00FFCC", card_dark_text=True,
        tag="SaaS · Ski Tech", stat="+9% product page conversion",
        agency="Series Eight", role="Design Director",
        platform="D2C product & marketing site",
        timeline="2 week sprint, followed by 3 months of live A/B testing",
        ownership="UX strategy, IA, design system",
        team="Design and PM",
        live_url="https://getcarv.com/",
        headline="Carving a Clearer Run",
        overview="CARV, the wearable ski coach used by everyone from weekend skiers to Olympians like Ted Ligety, came to us needing to broaden its audience. The product had been built and marketed for expert skiers analysing every metric of their run, but the brand wanted to open up to a much wider, more mainstream crowd without losing the technical depth power users relied on. I led the IA restructure, content strategy and design system work behind the relaunch, driving a +9% increase in product page conversion through three months of live testing.",
        results=[
            "+9% increase in product page conversion",
            "Fewer support tickets on pricing confusion",
            "Stronger engagement across both new and expert audiences",
        ],
        challenge=["CARV's website had grown organically for years and it showed. Three overloaded pages (Sensors, Analysis, Coaching) tried to explain the product but buried the one thing that mattered most: that you could actually buy it. Information was duplicated across pages, navigation had dead links, and the tone spoke fluently to ski pros but alienated everyone else. On top of that, the subscription model (a Season Pass with free sensors versus a Daily Pass with a one-off sensor cost) confused users and even tripped up the client's own team when explaining it."],
        approach=[
            "We couldn't get direct analytics access, so discovery leaned on client walkthroughs and Hotjar heatmaps to find where people were dropping off and what they were ignoring. Since CARV had no real category competitors, I benchmarked against consumer tech brands known for making complex products feel simple: Apple Vision Pro, Meta Quest, DJI, Oura Ring, GoPro. A pattern emerged across all of them: one single source-of-truth product page, technical depth pushed into a separate tab, and benefit-led storytelling up front.",
            "That became the blueprint. I sorted the tangle of existing content into four clear buckets, physical features, technology, benefits, and technical specs, then rebuilt the sitemap around a single overview page with a dedicated specs section for the technical crowd. Pricing got the same treatment: I audited 16 subscription products (DAZN, Discovery+, F1TV, NOW TV, WeWork and others) to fix the tier terminology and move subscription info earlier in the journey.",
            "From there it was wireframes built with the copywriter and client, then UI design running in parallel with the client's engineering team, who built and live-tested components in PostHog as we designed. The output was a fully atomic design system of 15 responsive components, giving CARV a scalable toolkit to keep optimising and building new pages long after the project wrapped.",
        ],
        outcome=["Once the new structure and pricing model went live, CARV saw a 9% lift in product page conversion, plus fewer support tickets around pricing confusion and stronger session engagement across both new and expert audiences. More importantly, the brand now had a scalable system rather than a one-off redesign, letting the team keep testing and building on the same foundation."],
        reflection=["The real blocker wasn't how CARV looked, it was that users couldn't find a path to buy or understand what they were paying for. Fixing that, and borrowing visual cues from tech brands people already trusted, let CARV reach a mainstream audience without losing the expert base it was built on."],
        order_allwork=8, order_selected=1,
    ),
    dict(
        slug="splitmetrics", name="SplitMetrics", category="saas",
        accent="#A095FF",
        tag="SaaS · B2B Growth Platform", stat="6 IA restructures, built for scale",
        agency="Series Eight", role="Design Director",
        platform="Web (marketing/SaaS website)",
        timeline="February 2026 – May 2026 (design), development ongoing",
        ownership="UX strategy, discovery, information architecture, design system, art direction",
        team="Series Eight UI design support, freelance SaaS illustrator and motion designer, client's in-house development team for build",
        live_url="https://splitmetrics.com/",
        headline="Splitting SplitMetrics, On Purpose",
        overview="SplitMetrics is a mobile app growth platform and Apple Search Ads Partner, but its website hadn't kept pace: a SaaS product and a full-service agency arm were fighting for the same navigation and forms, and analytics showed people dropping off before they reached a demo booking. I led the project end to end, from a hopes-and-fears workshop with the CEO and CMO through to design system handover, anchored on one metric from session one: lead-to-demo conversion, not traffic.",
        results=[
            "6 full IA restructures to cleanly separate the SaaS product from the agency offer",
            "Book a Demo flow rebuilt to route by entry point, cutting the friction behind the drop-off",
            "200+ custom illustrated product assets, animated for web and sales collateral",
            "Full atomic design system delivered for client dev team handover",
        ],
        challenge=["SplitMetrics sells two different things to two different buyers, a self-serve SaaS product and a hands-on agency service, but its site treated them as one undifferentiated flow. The data made the cost of that clear: traffic arrived high-intent and already comparing tools, yet Google Analytics and Hotjar showed people bouncing before they ever reached a Book a Demo form that asked for more than it needed. The product wasn't helping its own case either, screenshots too small to show what the platform actually did, leaving visitors who wanted proof before talking to sales without it."],
        approach=[
            "Discovery started broad: a hopes-and-fears workshop with the CEO and CMO, a GA/Hotjar audit, and a landscape review benchmarked against SaaS leaders like Notion and Figma, not just ASO tools, so the site would read as a modern product rather than a niche one. The data threw up one surprise: Book a Demo's 61% bounce rate looked like a broken form, until the behaviour underneath showed people qualifying themselves rather than abandoning it, so I added softer exits like \u201cview pricing first\u201d instead of stripping the form back. Acquire, meanwhile, was quietly outperforming everything else, so I made it the template the rest of the site would follow.",
            "The harder problem was structural. SaaS product and agency services were genuinely intertwined, and separating them took six full restructures before it held together. What settled it was talking to the client's agency contacts and hearing how differently they ran ASO across Apple's App Store versus Google Play, proof the split needed to live in the architecture, not just the styling. That same logic reshaped Book a Demo, routing the form by entry point instead of asking everyone the same questions, before a MoSCoW workshop split the build into an MVP and future phases.",
            "Definition brought it together: creative concepts that modernised the brand for B2B SaaS without losing what made it recognisable, and a full atomic design system built in parallel so the client's own dev team could pick it up. The one gap craft alone couldn't close was proof, the product wasn't visible enough, so I commissioned 200+ custom illustrated assets and had them animated for use across the site and beyond.",
        ],
        outcome=["The site is currently in build with SplitMetrics' own development team, so there's no live conversion data yet, but what's shipping is built on evidence rather than a guess: an IA that finally separates SaaS product from agency service, a Book a Demo flow designed around the exact drop-off the data showed, and a design system built for a team other than Series Eight to build from. SplitMetrics operates at a level (Apple Search Ads Partner, SplitMetrics Optimize named ASO Tool of the Year) that needed a site holding up to a sophisticated, global audience, and the structure is built to do exactly that once it goes live."],
        reflection=["This was as much a stakeholder and structure problem as a design one. Getting six iterations deep on an IA before it was right, and building a system another team could actually build from, mattered more here than any single page design."],
        order_allwork=10, order_selected=4,
    ),
    dict(
        slug="crunchpos", name="CrunchPOS", category="saas",
        accent="#3A7CFF",
        tag="SaaS · Restaurant POS", stat="22,000+ restaurants trust the brand",
        agency="Series Eight", role="Design Director",
        platform="SaaS Website",
        timeline="Nov 2025 → Apr 2026",
        ownership="Brand strategy, tone of voice, information architecture, design system, art direction, QA",
        team="PM, Designers, Copywriter, SEO, Developer",
        live_url="",
        headline="People First, Tech Second",
        overview="Crunch is a POS and payments platform built by former restaurant owners for restaurant owners, already trusted by over 22,000 restaurants. But the brand hadn't caught up with the business, generic, jargon-heavy, and burying the \u201cbuilt by people who've run a kitchen\u201d story that made Crunch different. I led Series Eight's work to rebuild the brand and restructure the website around how customers actually think, not how the product team organised it, work that later got picked up by design publication OFFCUTS.",
        results=[
            "Competitor audit: Toast, Clover, SpotOn, SkyTab, Square",
            "Brand & TOV workshop, distilled into three tone pillars",
            "IA workshop, restructured around customer intent",
            "Full visual identity: colour, type, logo, photography",
            "System extended across web, product UI, app icon, social, OOH, packaging",
        ],
        challenge=["Crunch was competing against well-funded, polished rivals like Toast, Square, Clover, SpotOn and SkyTab, all of whom lead with trust signals, clean visual hierarchy and confident positioning. Crunch's own site buried its strongest asset, an authentic founder story, under dense, feature-led copy and a navigation structure organised around internal product names rather than what a restaurant owner would search for. The brand voice was functional but forgettable. Without a distinct identity and a site people could actually scan, Crunch risked blending into a crowded category it had every right to stand out in."],
        approach=[
            "I started with discovery: benchmarking Crunch against Toast, Clover, SpotOn, SkyTab and Square to find the category's conventions and its gaps, then ran a brand and tone-of-voice workshop with the Crunch team that distilled a \u201cBold & Powerful\u201d personality into three pillars, Empowering, Expressive and Straight-talking, anchored on the founder story and the idea of putting people before technology.",
            "In parallel, an information architecture workshop rebuilt the sitemap around how a restaurant owner actually thinks about their business, Front of House, Back of House, Office and Ecommerce, with pricing pulled out as its own destination, giving us a simplified primary nav we could benchmark directly against competitors.",
            "From there I built the visual system: a disciplined four-colour palette (Bright White, Midnight Blue, Neon Blue, Off White) chosen so blue signalled trust without losing energy, paired with Helvetica Now Display, a wordmark plus a standalone spiral \u201cC\u201d icon mark, and documentary, candid photography, real kitchens, real staff, to keep \u201cpeople first\u201d visible rather than just written down. I then extended that system across every touchpoint, web, product UI, app icon, social, out-of-home and packaging, and QA'd it throughout to keep it consistent.",
        ],
        outcome=["Crunch came out with a coherent identity built to hold its own against much bigger-budget competitors, and a website navigation restructured around customer intent rather than internal product taxonomy. The tone-of-voice framework and brand guidelines gave the wider team a documented system to apply consistently across future work, rather than relying on one-off decisions. The rebrand was recognised externally too, featured in the 2026 edition of design publication OFFCUTS. More importantly, Crunch came away with a fully optimised Craft CMS site built on solid foundations, designed to actually evolve with the business rather than need another overhaul in a year."],
        reflection=["This was as much a structural problem as a branding one. Running the IA work and the brand workshop in parallel meant the identity didn't just get applied to the site, it shaped how the site was organised in the first place."],
        order_allwork=11, order_selected=3,
    ),
    dict(
        slug="pearson-pte", name="Pearson PTE", category="saas",
        accent="#357E9F",
        tag="SaaS · EdTech", stat="23 legacy templates unified into one system",
        agency="DEPT®", role="Design Director",
        platform="Responsive website, multi-region (Australia, Canada, UK and others)",
        timeline="~12 months, discovery through to launch",
        ownership="Brand strategy, UX research, information architecture, design system, prototyping",
        team="UX researchers, brand strategists, developers, SEO specialists",
        live_url="https://www.pearsonpte.com/",
        headline="Plain English for an English Test",
        overview="Pearson's PTE Academic is one of the biggest English-language testing services in the world, used by people applying to study, work, or migrate abroad. Both Pearson's own team and the people using the site agreed on one thing: the brand felt inconsistent, corporate, and forgettable. I led the design direction on a full rebuild, from brand research through to a tested, scalable system, built to work for an audience with almost nothing in common except the test they were taking.",
        results=[
            "23 inconsistent legacy templates consolidated into 9 reusable component categories",
            "Brand perception shifted from \u201cinconsistent and corporate\u201d to distinct and human",
            "Strongest flows prototyped and user-tested before final delivery",
            "System built to scale across every regional market",
        ],
        challenge=["Internal feedback described the existing brand as confusing and lacking consistency. External feedback landed in almost the same place: inconsistent, formal, uninspiring. Underneath that was a site with around 23 different page templates that all followed the same hero-plus-components pattern, so nothing felt distinct from anything else. Meanwhile the actual audience was enormous and varied: a software consultant applying for UK settlement, a nurse in the Philippines proving language proficiency for registration, a student in Vietnam with almost no English trying to study in the US. One brand, wildly different people, and a site that wasn't speaking to any of them specifically."],
        approach=[
            "Discovery started with an audit of the existing template and component library, and real personas rather than broad segments, migrants, students, and workers split further by market and scenario, from a software consultant chasing UK settlement to a nurse in the Philippines proving language proficiency for registration.",
            "To define the tone I ran a scored competitor teardown, IELTS came out at 2 out of 10 on brand (intimidating, corporate, dated), against aspirational comparisons like Duolingo, Skillshare, Teachable, and Uber, benchmarking logo, voice, photography, and colour to see what education could borrow from other categories entirely. That research fed three genuinely different brand directions, one illustration and wordmark led, one built around bold colour and 3D characters, one led by authentic photography, put in front of stakeholders to align on together rather than defend a single option, with the shortlisted palette pushed through WCAG AA contrast testing early so nothing that looked good on a moodboard but failed in practice made it through.",
            "Once a direction was agreed, it became a proper system, nine component categories and reusable templates across every major page type, built so regional teams could assemble new pages without breaking it.",
        ],
        outcome=["What shipped was a distinct, considerably more human brand than the one Pearson started with, moving away from a generic corporate feel toward something that could actually speak to a global, wildly diverse audience without losing consistency. The strongest flows were prototyped and tested with real users before final delivery, and the system was built to scale, giving regional teams a library to build from rather than a static one-off homepage."],
        reflection=["Plenty of the people using this site had very little English, on a website for an English test. So the writing itself had to be simple enough for them to follow, or the brand had failed before they even booked the test. It's why I now think of accessibility less as a checklist, more as one question: can the weakest reader in the room actually follow this."],
        order_allwork=9, order_selected=5,
    ),
    dict(
        slug="mailboard", name="Mailboard", category="saas",
        accent="#FFF962", card_dark_text=True,
        tag="SaaS · Marketing Tool", stat="2M+ curated emails · Awwwards Honorable Mention",
        agency="Series Eight", role="Design Director",
        platform="SaaS product (web app) + marketing website, built on Craft CMS",
        timeline="Concept to launch, early 2024",
        ownership="Brand identity, product design (UX/UI), marketing website design, design direction and QA",
        team="1 brand/web designer, 1 product designer, working under my direction",
        live_url="https://mailboard-.on-forge.com/",
        headline="Inbox Chaos to Effortless Inspiration",
        overview="Mailboard is a tool Series Eight built for itself first: a place to find, save, and analyze the internet's best marketing emails, instead of drowning in screenshots and Slack threads. I directed the design across brand, product, and marketing site, setting strategy and running review and QA across two specialists while staying hands-on throughout. It picked up an Awwwards Honorable Mention and CSS Design Awards recognition within weeks of launch.",
        results=[
            "Awwwards Honorable Mention + CSS Design Awards, within 6 weeks",
            "Email library grew from 700K to 2M+ curated emails",
            "Adopted by teams at Gymshark, Patagonia, YETI, DJI, Liquid Death",
            "Named a \u201cgo-to\u201d tool by marketers and founders",
        ],
        challenge=["Every marketer and copywriter on the team, and every client we worked with, was doing the same thing: hoarding screenshots of great emails in random folders with no way to organize, share, or learn from them. Nothing on the market was built specifically for this, tools like Mailcharts and Foreplay existed for ads, not email. Series Eight decided to build the tool itself, which meant designing a brand, a product, and a marketing website from nothing, at a scale that would only get harder as the library grew."],
        approach=[
            "The first call was strategic: nobody trusts a brand-new tool over their old screenshot folders unless the brand feels more credible than the problem it replaces. I pushed for a distinctive, opinionated identity rather than the safe SaaS-blue look most tools in this space default to, then set a shared design system so that identity held together across web and product without drifting apart as two designers built in parallel.",
            "On product, the decision I backed was to get out of the way of the content. With a library headed past a million emails, the UI needed to prioritize search, filtering, and a board-based save structure over any kind of visual flourish, so the interface stayed minimal and the emails themselves stayed the focus. That's a deliberate trade-off: usability over decoration, made because the product's whole value is in the content being easy to find, not in the UI showing off.",
            "Running two specialists concurrently meant daily reviews rather than end-of-sprint check-ins, arbitrating the constant tension between brand distinctiveness (where the marketing site and identity needed to stand out) and product convention (where the app needed to just work). On the marketing site, I made the call to lead with recognizable brand logos before any feature explanation, since a tool with no track record needed borrowed credibility before it could ask for anyone's attention.",
        ],
        outcome=["Mailboard launched to an Awwwards Honorable Mention and CSS Design Awards recognition within weeks. It's since grown into a genuinely used tool in its category, now curating over 2 million emails from brands like The North Face, Patagonia, YETI, Gymshark, and Liquid Death, with real marketers and founders citing it by name as their go-to for email inspiration and competitive research."],
        reflection=["Mailboard tested my ability to direct a small, senior team through a 0-to-1 brand, product, and website launch at once, and to hold a distinctive point of view without losing sight of what the product actually needed to do at scale. That balance, knowing when to protect the brand and when to protect the user, is something I've carried into every Design Director role since."],
        order_allwork=12, order_selected=2,
    ),
    dict(
        slug="stash-finance", name="Stash Finance", category="saas",
        accent="#EECDCD",
        tag="SaaS · Fintech", stat="+40% increase in action intent",
        agency="E3creative (now DEPT®)", role="Head of Design",
        platform="Mobile app (iOS & Android), plus marketing website",
        timeline="6 week sprint",
        ownership="Brand identity, product strategy, UX/UI, design system",
        team="Design, Copywriting, Engineering, PM",
        live_url="https://moneyplusadvice.com/",
        headline="Finance That Already Knows You",
        overview="Stash is a fintech app I built from a blank page for MoneyPlus, a UK financial advisory business that wanted to turn its large database of financial information into a product for a completely new audience. The brief was to invent a sister brand from scratch, name, identity, tone of voice and a working app, that could hold its own against fintech competitors while still being trustworthy enough to hand over your bills.",
        results=[
            "+40% increase in action intent vs traditional finance journeys",
            "Up to 30% estimated annual saving opportunity per user",
            "IA and design system built to scale across the wider MoneyPlus ecosystem",
            "Full brand and product built in a 6 week sprint",
        ],
        challenge=["MoneyPlus's usual audience skewed older and less tech-savvy, but the CEO wanted to reach a younger, more digitally fluent group who wouldn't touch a traditional advisory brand. That meant starting with nothing: no name, no identity, no product, just a database of financial information and six weeks to turn it into something people would trust with their bills, their car finance and their insurance. It also had to stand apart from MoneyPlus, distinct enough to win that audience on its own terms, while still working alongside it as a partner brand rather than a rival. Get the tone wrong and it reads as another faceless fintech, get it too casual and nobody trusts it with their money."],
        approach=[
            "A discovery workshop and four user personas, from a bill-cutter to an older user just checking he wasn't overpaying, made the case for structuring the product around real-life categories (vehicle, home, utilities, telecoms, groceries, pets) rather than one generic dashboard, and I built the full app in greyscale first to pressure-test that IA before any visual treatment went near it.",
            "The key product decision was what it ran on: rather than asking users to manually enter their bills and policies, it pulled from MoneyPlus's own customer data, so the app could generate live comparisons and recommendations automatically, a financial assistant rather than a form to fill in. The vehicle journey became the reference flow for that model: look up your reg, confirm the car, get a direct comparison of what you're paying versus what you could switch to, backed by a KnowledgeHub for anyone who wanted the reasoning before acting. I also designed the marketing site to sell the app itself.",
        ],
        outcome=["The results validated the core bet: giving users a live comparison instead of a form to fill in got them to act, and the trust that came from Stash knowing their situation already, rather than asking them to prove it, carried through in testing. The IA and design system were built with headroom from day one, so MoneyPlus could extend Stash into new categories without a redesign."],
        reflection=["Stash is the project I point to when someone asks if I can build a brand and a product at the same time under real pressure. Six weeks from nothing to a full identity, a working app and a scalable system only worked because I ran brand and UX in parallel, not handed off in sequence."],
        order_allwork=7, order_selected=6,
    ),
]

PROJECTS_BY_SLUG = {p['slug']: p for p in PROJECTS}
ALLWORK_ORDER = sorted(PROJECTS, key=lambda p: p['order_allwork'])
ECOM_ORDER = sorted([p for p in PROJECTS if p['category'] == 'ecommerce'], key=lambda p: p['order_selected'])
SAAS_ORDER = sorted([p for p in PROJECTS if p['category'] == 'saas'], key=lambda p: p['order_selected'])

# Projects without a case study page yet — shown on All Work as inert (unlinked)
# cards so they're ready to wire up once the case study exists. Category
# guesses are mine from the one-line descriptions; flag any that are wrong.
PLACEHOLDERS = [
    dict(slug="destinology-travel", name="Destinology", tag="Travel booking website", category="ecommerce", live_url="https://www.destinology.co.uk/"),
    dict(slug="virgin-money-marathon", name="Virgin Money London Marathon", tag="Event booking website", category="ecommerce", live_url="https://www.londonmarathonevents.co.uk/"),
    dict(slug="smilemakers", name="SmileMakers", tag="Adult product ecommerce", category="ecommerce", live_url="https://smilemakerscollection.com/"),
    dict(slug="mgg", name="MGG", tag="Fashion ecommerce", category="ecommerce", live_url="https://mgg.ski/"),
    dict(slug="redbull-air-race", name="RedBull Air Race", tag="Event booking website", category="ecommerce", live_url="https://www.redbull.com/gb-en/tags/air-racing"),
    dict(slug="ascot-racecourse", name="Ascot Racecourse", tag="Event booking website", category="ecommerce", live_url="https://www.ascot.com/"),
    dict(slug="royal-ascot", name="Royal Ascot", tag="Event booking, day planner, experience", category="ecommerce", live_url="https://www.ascot.com/royal-ascot"),
    dict(slug="jonite", name="Jonite", tag="B2B architectural products", category="b2b", live_url="https://www.jonite.com/"),
    dict(slug="dimo", name="Dimo", tag="SaaS product website", category="saas", live_url="https://drivedimo.com/"),
    dict(slug="florence-by-mills", name="Florence by Mills Coffee", tag="Ecommerce for coffee", category="ecommerce", live_url="https://www.florencebymills.com/"),
    dict(slug="holidaily-brewery", name="Holidaily Brewery", tag="Booking, venue website and ecommerce", category="ecommerce", live_url="https://holidailybrewing.com/"),
    dict(slug="cowboy-bikes", name="Cowboy Bikes", tag="Bike ecommerce", category="ecommerce", live_url="https://cowboy.com/"),
    dict(slug="formula-e", name="Formula E", tag="SaaS product design", category="saas", live_url="https://fiaformulae.com/en"),
    dict(slug="o2-star-trader", name="O2 Star Trader", tag="B2B website and portal design", category="b2b", live_url="https://www.o2.co.uk/"),
    dict(slug="co-op-paws-think", name="Co-Op Paws & Think", tag="Product app design", category="ecommerce", live_url=""),
    dict(slug="outplay-entertainment", name="Outplay Entertainment", tag="Mobile app portfolio website", category="saas", live_url="https://www.outplay.com/"),
    dict(slug="watadventures", name="WatAdventures", tag="SaaS and ecommerce for children's books", category="ecommerce", live_url=""),
    dict(slug="liverpool-fc", name="Liverpool FC", tag="Anniversary marketing web app", category="ecommerce", live_url=""),
]
PLACEHOLDERS_BY_SLUG = {p['slug']: p for p in PLACEHOLDERS}

# Full 30-tile grid order, matching the sequence in the Figma "All Work" export.
GRID_ORDER_SLUGS = [
    "playstation-gear", "outside-in", "nikon",
    "notwoways", "steamforged-games", "triumph-motorcycles",
    "destinology-travel", "virgin-money-marathon", "stash-finance",
    "smilemakers", "mgg", "carv",
    "redbull-air-race", "ascot-racecourse", "royal-ascot",
    "jonite", "dimo", "florence-by-mills",
    "holidaily-brewery", "cowboy-bikes", "formula-e",
    "o2-star-trader", "co-op-paws-think", "outplay-entertainment",
    "watadventures", "liverpool-fc", "pearson-pte",
    "splitmetrics", "crunchpos", "mailboard",
]
GRID_ORDER = [
    (PROJECTS_BY_SLUG[s], True) if s in PROJECTS_BY_SLUG else (PLACEHOLDERS_BY_SLUG[s], False)
    for s in GRID_ORDER_SLUGS
]

print(f"Loaded {len(PROJECTS)} projects.")

# ---------------------------------------------------------------------------
# ICONS — 3 custom SVGs (document, stacked-layers, diagonal arrow) built to
# match the style guide description. TODO for Simon: swap for the exact
# Figma-exported SVGs if these don't match pixel-for-pixel.
# ---------------------------------------------------------------------------

ICON_ARROW = '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M4 12L12 4M12 4H5.5M12 4V10.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'

ICON_LAYERS = '<svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M9 2L16 6L9 10L2 6L9 2Z" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/><path d="M2 9.5L9 13.5L16 9.5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/><path d="M2 13L9 17L16 13" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/></svg>'

ICON_DOC = '<svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><rect x="3" y="2" width="12" height="14" rx="2" stroke="currentColor" stroke-width="1.3"/><path d="M6 6.5H12M6 9.5H12M6 12.5H9.5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>'

ICON_CHEVRON_LEFT = '<svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M11 3.5L5.5 9L11 14.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'

ICON_CHEVRON_RIGHT = '<svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M7 3.5L12.5 9L7 14.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'

ICON_CHEVRON_LEFT_SM = ICON_CHEVRON_LEFT.replace('width="18" height="18"', 'width="14" height="14"')
ICON_CHEVRON_RIGHT_SM = ICON_CHEVRON_RIGHT.replace('width="18" height="18"', 'width="14" height="14"')


# ---------------------------------------------------------------------------
# SHARED HEAD / CHROME
# ---------------------------------------------------------------------------

def head(title, description, css_rel="css/style.css"):
    return f'''<meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>

  <!-- Meta & SEO -->
  <meta name="description" content="{description}">

  <!-- Open Graph -->
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="TODO: URL to social share image (1200x630px recommended)">
  <meta property="og:url" content="TODO: live page URL">
  <meta property="og:type" content="website">

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="TODO: favicon.png">

  <link rel="stylesheet" href="{css_rel}">'''


def contact_href():
    # Placeholder per brief §4.1 — a proper About/CV/Contact page is a
    # separate later project. Wired as a mailto stub for now.
    return "mailto:simon.d.fairhurst@gmail.com"


def top_home_chrome(css_prefix=""):
    return f'''  <header class="topbar">
    <div class="topbar__left">
      <a class="topbar__brand" href="{css_prefix}index.html"><span class="spark">✦</span> Simon Fairhurst · 2026</a>
    </div>
    <div class="topbar__center">
      <nav class="topbar__nav" aria-label="Home sections">
        <button type="button" data-home-nav="selected" aria-current="true">Selected work</button>
        <button type="button" data-home-nav="all">All work</button>
      </nav>
    </div>
    <div class="topbar__right">
      <a class="topbar__contact" href="{contact_href()}">Contact</a>
    </div>
  </header>'''


def bottom_home_chrome():
    return f'''  <footer class="bottombar">
    <div class="bottombar__left">
      <p class="bottombar__meta">Lead Digital Product Designer · 15 years experience<br>Currently Design Director @ Series Eight</p>
    </div>
    <div class="bottombar__center">
      <div class="bottombar__toggle" role="group" aria-label="Display mode">
        <button type="button" data-display-toggle="stacked" aria-pressed="true" aria-label="Stacked view">{ICON_LAYERS}</button>
        <button type="button" data-display-toggle="swipe" aria-pressed="false" aria-label="Swipe view">{ICON_DOC}</button>
      </div>
    </div>
    <div class="bottombar__right">
      <p class="bottombar__clock" data-clock>Manchester, UK · 00:00:00</p>
    </div>
  </footer>'''


def bottom_case_study_chrome():
    return f'''  <footer class="bottombar bottombar--static">
    <div class="bottombar__left">
      <p class="bottombar__meta">Lead Digital Product Designer · 15 years experience<br>Currently Design Director @ Series Eight</p>
    </div>
    <div class="bottombar__center"></div>
    <div class="bottombar__right">
      <p class="bottombar__clock" data-clock>Manchester, UK · 00:00:00</p>
    </div>
  </footer>'''


def top_case_study_chrome(project, css_prefix=""):
    order = ALLWORK_ORDER
    idx = next(i for i, p in enumerate(order) if p['slug'] == project['slug'])
    prev_p = order[(idx - 1) % len(order)]
    next_p = order[(idx + 1) % len(order)]
    return f'''  <header class="topbar">
    <div class="topbar__left">
      <a class="topbar__brand" href="{css_prefix}index.html"><span class="spark">✦</span> Simon Fairhurst · 2026</a>
    </div>
    <div class="topbar__center">
      <nav class="switcher" aria-label="Case study switcher">
        <a href="{prev_p['slug']}.html" aria-label="Previous case study: {prev_p['name']}">{ICON_CHEVRON_LEFT_SM}</a>
        <span class="switcher__name">{project['name']}</span>
        <a href="{next_p['slug']}.html" aria-label="Next case study: {next_p['name']}">{ICON_CHEVRON_RIGHT_SM}</a>
      </nav>
    </div>
    <div class="topbar__right">
      <p class="body-sm cs-topbar-clock" data-clock>Manchester, UK · 00:00:00</p>
      <a class="topbar__contact" href="{contact_href()}">Contact</a>
    </div>
  </header>'''


# ---------------------------------------------------------------------------
# CARD RENDERERS
# ---------------------------------------------------------------------------

FAN_STEP_X = 130
FAN_STEP_Y = 40


CARD_DARK_FG = "#161616"


def card_fg_style(p):
    return f"--card-fg:{CARD_DARK_FG};" if p.get('card_dark_text') else ""


def stacked_card_html(p, index, total):
    tx, ty = index * FAN_STEP_X, index * FAN_STEP_Y
    z = total - index
    style = f"--tx:{tx}px; --ty:{ty}px; --z:{z}; {card_fg_style(p)}"
    is_first = index == 0
    return f'''      <a class="card stacked-card{' is-front' if is_first else ''}" href="case-studies/{p['slug']}.html" style="{style}">
        <img class="card__media" src="assets/cards/{p['slug']}.jpg" alt="{p['name']} case study cover" loading="lazy">
        <div class="card__overlay-top">
          <span class="card__tag"><span>{p['tag']}</span><span>{p['stat']}</span></span>
          <span class="card__arrow">{ICON_ARROW}</span>
        </div>
        <span class="card__name">{p['name']}</span>
      </a>'''


def swipe_card_html(p):
    style = card_fg_style(p)
    return f'''        <div class="swipe-card-wrap" style="{style}">
          <img class="card swipe-card" src="assets/cards/{p['slug']}.jpg" alt="{p['name']} case study cover" loading="lazy">
          <div class="card__overlay-top">
            <span class="card__tag"><span>{p['tag']}</span><span>{p['stat']}</span></span>
          </div>
          <span class="card__name">{p['name']}</span>
          <a class="swipe-cta" href="case-studies/{p['slug']}.html">Read case study {ICON_ARROW}</a>
        </div>'''


def grid_card_html(p, has_case_study):
    if has_case_study:
        style = card_fg_style(p)
        return f'''    <a class="card gridcard" href="case-studies/{p['slug']}.html" data-project-type="{p['category']}" style="{style}">
      <img class="card__media" src="assets/cards/{p['slug']}.jpg" alt="{p['name']} case study cover" loading="lazy">
      <div class="card__overlay-top">
        <span class="card__tag"><span>{p['tag']}</span><span>{p['stat']}</span></span>
      </div>
      <span class="card__name">{p['name']}</span>
    </a>'''
    else:
        if p.get('live_url'):
            return f'''    <a class="card gridcard gridcard--placeholder" href="{p['live_url']}" target="_blank" rel="noopener" data-project-type="{p['category']}" title="Case study coming soon — links to the live site for now">
      <img class="card__media" src="assets/cards/{p['slug']}.jpg" alt="{p['name']}" loading="lazy">
      <div class="card__overlay-top">
        <span class="card__tag"><span>{p['tag']}</span></span>
      </div>
      <span class="card__name">{p['name']}</span>
    </a>'''
        return f'''    <div class="card gridcard gridcard--placeholder" data-project-type="{p['category']}" title="Case study coming soon">
      <img class="card__media" src="assets/cards/{p['slug']}.jpg" alt="{p['name']}" loading="lazy">
      <div class="card__overlay-top">
        <span class="card__tag"><span>{p['tag']}</span></span>
      </div>
      <span class="card__name">{p['name']}</span>
    </div>'''


def stacked_group(projects, category):
    cards = "\n".join(stacked_card_html(p, i, len(projects)) for i, p in enumerate(projects))
    n = len(projects)
    half_x = (n - 1) * FAN_STEP_X / 2
    half_y = (n - 1) * FAN_STEP_Y / 2
    stack_style = f"--fan-half-x:{half_x}px; --fan-half-y:{half_y}px;"
    return f'''    <div class="stacked-stage" data-display="stacked" data-category-group="{category}">
      <div class="stacked-stack" style="{stack_style}">
{cards}
      </div>
    </div>'''


def swipe_group(projects, category):
    cards = "\n".join(swipe_card_html(p) for p in projects)
    return f'''    <div class="swipe-stage" data-display="swipe" data-category-group="{category}">
      <button type="button" class="swipe-chevron swipe-chevron--prev" aria-label="Previous project">{ICON_CHEVRON_LEFT}</button>
      <div class="swipe-deck" data-swipe-group>
{cards}
      </div>
      <button type="button" class="swipe-chevron swipe-chevron--next" aria-label="Next project">{ICON_CHEVRON_RIGHT}</button>
    </div>'''


# ---------------------------------------------------------------------------
# INDEX.HTML
# ---------------------------------------------------------------------------

def build_index():
    grid_cards = "\n".join(grid_card_html(p, has_cs) for p, has_cs in GRID_ORDER)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  {head("Simon Fairhurst · Design Director", "Portfolio of Simon Fairhurst — Design Director, 15 years of experience across product design, UX strategy and design systems for PlayStation, Nikon, Triumph and more.")}
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  {top_home_chrome()}

  <nav class="subnav" aria-label="Selected work category" data-view-only="selected">
    <button type="button" data-subnav="ecommerce" aria-current="true">Ecommerce</button>
    <button type="button" data-subnav="saas" aria-current="false">SaaS</button>
  </nav>
  <div class="nav-keyline" aria-hidden="true"></div>

  <main id="main">
    <section class="view" data-view="selected" data-active="true" aria-label="Selected work">
{stacked_group(ECOM_ORDER, "ecommerce")}
{stacked_group(SAAS_ORDER, "saas")}
{swipe_group(ECOM_ORDER, "ecommerce")}
{swipe_group(SAAS_ORDER, "saas")}
    </section>

    <section class="view" data-view="all" data-active="false" aria-label="All work">
      <div class="allwork">
        <div class="allwork__controls">
          <div class="filterrow">
            <span class="filterrow__label">Type</span>
            <div class="filterrow__options" role="group" aria-label="Filter by type">
              <button type="button" data-filter="all" aria-pressed="true">All</button>
              <button type="button" data-filter="ecommerce" aria-pressed="false">Ecommerce</button>
              <button type="button" data-filter="saas" aria-pressed="false">SaaS</button>
              <button type="button" data-filter="b2b" aria-pressed="false">B2B</button>
            </div>
          </div>
          <div class="filterrow">
            <span class="filterrow__label">Sort</span>
            <div class="filterrow__options" role="group" aria-label="Sort order">
              <button type="button" data-sort="recent" aria-pressed="true">Most recent</button>
              <button type="button" data-sort="impact" aria-pressed="false">Impact</button>
            </div>
          </div>
        </div>
        <div class="allwork__grid">
{grid_cards}
        </div>
        <p class="allwork__empty" style="display:none;">No projects in this category yet.</p>
      </div>
    </section>
  </main>

  {bottom_home_chrome()}

  <script src="js/main.js"></script>
</body>
</html>
'''
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote index.html")



# ---------------------------------------------------------------------------
# CASE STUDY PAGES
# ---------------------------------------------------------------------------

def paras(list_of_strings):
    return "\n".join(f"        <p>{s}</p>" for s in list_of_strings)


def results_list(items):
    lis = "\n".join(f"          <li>{i}</li>" for i in items)
    return f"        <ul>\n{lis}\n        </ul>"


def meta_row(label, value):
    if not value:
        return ""
    return f'''        <div class="cs-meta__row"><span class="cs-meta__label">{label}</span><span class="cs-meta__value">{value}</span></div>'''


def hex_to_rgba(hex_color, alpha):
    h = hex_color.lstrip('#')
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"


def build_case_study(p):
    slug = p['slug']
    assets = f"../assets/{slug}"
    glow = hex_to_rgba(p['accent'], 0.22)

    live_value = f'<a href="{p["live_url"]}" target="_blank" rel="noopener">{p["live_url"].replace("https://","").replace("http://","")} ↗</a>' if p['live_url'] else '<span style="opacity:.5">TODO — link once live</span>'

    meta_rows = "\n".join(filter(None, [
        meta_row("Agency", p['agency']),
        meta_row("Title", p['role']),
        meta_row("Platform", p['platform']),
        meta_row("Timeline", p['timeline']),
        meta_row("Ownership", p['ownership']),
        meta_row("Team", p['team']),
        meta_row("Live site", live_value),
    ]))

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  {head(p['name'] + " · Simon Fairhurst", p['overview'][:155].rsplit(' ',1)[0] + "…", css_rel="../css/style.css")}
  <style>:root{{ --accent: {p['accent']}; --accent-glow: {glow}; }}</style>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <div class="cs-glow" aria-hidden="true"></div>
  {top_case_study_chrome(p, css_prefix="../")}

  <main id="main" class="cs-wrap">
    <div class="cs-header">
      <p class="cs-header__label">{p['name']}</p>
      <h1 class="cs-header__title">{p['headline']}</h1>
      <div class="cs-header__overview-col">
        <p class="cs-header__overview">{p['overview']}</p>
        <div class="cs-results">
          <p class="cs-results__heading">Results</p>
{results_list(p['results'])}
        </div>
      </div>
      <div class="cs-meta">
{meta_rows}
      </div>
    </div>

    <div class="cs-visual">
      <img src="{assets}/hero.jpg" alt="{p['name']} — hero visual" loading="lazy">
    </div>

    <div class="cs-section">
      <h2>The Challenge</h2>
{paras(p['challenge'])}
    </div>

    <div class="cs-row2">
      <div class="cs-visual"><img src="{assets}/challenge-1.jpg" alt="{p['name']} — supporting visual" loading="lazy"></div>
      <div class="cs-visual"><img src="{assets}/challenge-2.jpg" alt="{p['name']} — supporting visual" loading="lazy"></div>
    </div>

    <div class="cs-section">
      <h2>The Approach</h2>
{paras(p['approach'])}
    </div>

    <div class="cs-visual">
      <img src="{assets}/approach-full.jpg" alt="{p['name']} — process visual" loading="lazy">
    </div>

    <div class="cs-section">
      <h2>The Outcome</h2>
{paras(p['outcome'])}
    </div>

    <div class="cs-row2">
      <div class="cs-visual"><img src="{assets}/outcome-1.jpg" alt="{p['name']} — outcome visual" loading="lazy"></div>
      <div class="cs-visual"><img src="{assets}/outcome-2.jpg" alt="{p['name']} — outcome visual" loading="lazy"></div>
    </div>

    <div class="cs-section">
      <h2>Reflection</h2>
{paras(p['reflection'])}
    </div>

    <div class="cs-row2">
      <div class="cs-visual"><img src="{assets}/reflection-1.jpg" alt="{p['name']} — final visual" loading="lazy"></div>
      <div class="cs-visual"><img src="{assets}/reflection-2.jpg" alt="{p['name']} — final visual" loading="lazy"></div>
    </div>

    <div class="cs-cta">
      <img class="cs-cta__avatar" src="../assets/headshot.png" alt="Simon Fairhurst">
      <div class="cs-cta__text">
        <p class="cs-cta__intro">I'd love to talk you through my process.</p>
        <p class="cs-cta__headline">Let's talk.</p>
        <p class="cs-cta__email"><a href="{contact_href()}">{contact_href().replace('mailto:','')}</a></p>
      </div>
    </div>
  </main>

  {bottom_case_study_chrome()}

  <script src="../js/main.js"></script>
</body>
</html>
'''
    out_dir = os.path.join(ROOT, "case-studies")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(html)


def main():
    build_index()
    for p in PROJECTS:
        build_case_study(p)
    print(f"wrote {len(PROJECTS)} case study pages")


if __name__ == "__main__":
    main()
