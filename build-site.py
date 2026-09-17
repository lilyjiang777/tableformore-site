"""Builds the full tableformoreapp.com static site: index.html (marketing
homepage), privacy.html, terms.html, support.html — one shared design system,
Deep Jade / Warm Ivory, Bricolage Grotesque + Newsreader. Run from the site
repo directory: python3 build-site.py
"""
import base64
import math
from pathlib import Path

ICON_B64 = base64.b64encode(Path("/Users/lily/Project TABLEFORMORE/assets/images/icon.png").read_bytes()).decode()
ICON_URI = f"data:image/png;base64,{ICON_B64}"

CSS = """
  :root {
    --bg: #FFFCF7; --surface: #FFFFFF; --surface-2: #FBF6EC; --border: #E7E9E5;
    --ink: #202421; --ink-soft: #6F746F; --ink-mute: #A6ABA3;
    --jade: #167D6A; --jade-dark: #106456; --jade-tint: #DDF3EC;
    --gold: #D69A1E; --gold-tint: #FAF0D6;
    --coral: #C9765A; --coral-tint: #F6E4DC;
    --danger: #C23B22; --danger-soft: #F8DFD8;
    --shadow: 0 20px 50px -25px rgba(16, 100, 86, 0.35);
    --font-display: 'Bricolage Grotesque', 'Avenir Next', 'Segoe UI', system-ui, sans-serif;
    --font-body: 'Newsreader', Georgia, 'Times New Roman', serif;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --bg: #121917; --surface: #1A2320; --surface-2: #1F2A26; --border: #29332F;
      --ink: #F1F0EA; --ink-soft: #A9B1AB; --ink-mute: #707970;
      --jade: #2BB395; --jade-dark: #1E8E76; --jade-tint: #1E3A33;
      --gold: #E7BA55; --gold-tint: #3A2E15;
      --coral: #E08D6E; --coral-tint: #3A2620;
      --danger: #E2694F; --danger-soft: #3B211B;
      --shadow: 0 20px 50px -25px rgba(0, 0, 0, 0.6);
    }
  }
  :root[data-theme="dark"] {
    --bg: #121917; --surface: #1A2320; --surface-2: #1F2A26; --border: #29332F;
    --ink: #F1F0EA; --ink-soft: #A9B1AB; --ink-mute: #707970;
    --jade: #2BB395; --jade-dark: #1E8E76; --jade-tint: #1E3A33;
    --gold: #E7BA55; --gold-tint: #3A2E15;
    --coral: #E08D6E; --coral-tint: #3A2620;
    --danger: #E2694F; --danger-soft: #3B211B;
    --shadow: 0 20px 50px -25px rgba(0, 0, 0, 0.6);
  }
  * { box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body { margin: 0; background: var(--bg); color: var(--ink); font-family: var(--font-body); font-size: 17px; line-height: 1.65; }
  a { color: var(--jade); }
  strong { font-weight: 700; }
  ::selection { background: var(--jade-tint); color: var(--jade-dark); }

  header.top { border-bottom: 1px solid var(--border); position: sticky; top: 0; background: color-mix(in srgb, var(--bg) 88%, transparent); backdrop-filter: blur(10px); z-index: 10; }
  .top-inner { max-width: 1080px; margin: 0 auto; padding: 18px 24px; display: flex; align-items: center; gap: 12px; }
  .brand { display: flex; align-items: center; gap: 10px; text-decoration: none; color: var(--ink); }
  .mark { width: 32px; height: 32px; border-radius: 22.37%; flex: none; display: block; }
  .wordmark { font-family: var(--font-display); font-weight: 700; font-size: 16px; letter-spacing: -0.01em; }
  nav.crosslinks { margin-left: auto; display: flex; align-items: center; gap: 22px; }
  nav.crosslinks a { font-family: var(--font-display); font-size: 13px; font-weight: 600; color: var(--ink-soft); text-decoration: none; }
  nav.crosslinks a:hover, nav.crosslinks a:focus-visible { color: var(--jade); }
  nav.crosslinks a[aria-current="page"] { color: var(--jade); }
  .nav-cta { background: var(--jade); color: var(--bg) !important; padding: 8px 16px; border-radius: 999px; }
  .nav-cta:hover { background: var(--jade-dark); }

  main { max-width: 680px; margin: 0 auto; padding: 48px 24px 40px; }
  main.wide { max-width: 1080px; }
  .eyebrow { font-family: var(--font-display); font-size: 12px; font-weight: 700; letter-spacing: 0.09em; text-transform: uppercase; color: var(--jade); margin: 0 0 10px; }
  h1 { font-family: var(--font-display); font-weight: 800; font-size: clamp(30px, 5vw, 40px); line-height: 1.1; margin: 0 0 14px; text-wrap: balance; letter-spacing: -0.01em; }
  .meta { display: flex; flex-wrap: wrap; gap: 8px 16px; font-family: var(--font-display); font-size: 13px; color: var(--ink-mute); margin-bottom: 36px; }
  .lede { font-size: 19px; color: var(--ink-soft); margin: 0 0 8px; font-style: italic; }
  h2 { font-family: var(--font-display); font-weight: 700; font-size: 22px; color: var(--jade); letter-spacing: -0.005em; margin: 40px 0 14px; }
  h3 { font-family: var(--font-display); font-weight: 700; font-size: 17px; margin: 26px 0 8px; }
  p { margin: 0 0 16px; max-width: 66ch; }
  ul, ol { margin: 0 0 16px; padding-left: 22px; }
  li { margin-bottom: 8px; max-width: 62ch; }
  .callout { background: var(--jade-tint); border: 1px solid var(--jade); border-radius: 14px; padding: 16px 20px; margin: 24px 0; font-family: var(--font-display); font-size: 14px; color: var(--ink); }
  .callout.warn { background: var(--danger-soft); border-color: var(--danger); }
  .callout p:last-child { margin-bottom: 0; }
  .faq-item { border-top: 1px solid var(--border); padding: 24px 0; }
  .faq-item:first-of-type { border-top: none; padding-top: 0; }
  .faq-item h3 { margin-top: 0; }
  .faq-item p { margin-bottom: 0; }
  table { width: 100%; border-collapse: collapse; margin: 0 0 20px; font-family: var(--font-display); font-size: 14px; }
  th, td { text-align: left; padding: 10px 12px; border-bottom: 1px solid var(--border); vertical-align: top; }
  th { color: var(--ink-mute); font-weight: 600; font-size: 12px; text-transform: uppercase; letter-spacing: 0.04em; }
  .tablewrap { overflow-x: auto; border: 1px solid var(--border); border-radius: 12px; margin: 0 0 24px; }
  .tablewrap table { margin: 0; }
  .tablewrap th:first-child, .tablewrap td:first-child { padding-left: 16px; }

  footer.site { border-top: 1px solid var(--border); margin-top: 48px; }
  .footer-inner { max-width: 1080px; margin: 0 auto; padding: 36px 24px 48px; display: flex; flex-wrap: wrap; gap: 18px 32px; align-items: center; font-family: var(--font-display); font-size: 13px; color: var(--ink-mute); }
  .footer-inner nav { display: flex; gap: 18px; margin-left: auto; }
  .footer-inner a { color: var(--ink-soft); text-decoration: none; }
  .footer-inner a:hover { color: var(--jade); }

  /* ---- marketing homepage ---- */
  .hero { max-width: 1080px; margin: 0 auto; padding: 64px 24px 40px; display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 48px; align-items: center; }
  @media (max-width: 860px) { .hero { grid-template-columns: 1fr; padding-top: 40px; gap: 32px; } }
  .hero h1 { font-size: clamp(36px, 5.4vw, 56px); }
  .hero-emoji { font-size: 30px; letter-spacing: 0.08em; margin-bottom: 18px; }
  .hero-sub { font-size: 20px; color: var(--ink-soft); font-style: italic; max-width: 44ch; margin-bottom: 30px; }
  .badges { display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 20px; }
  .badge { font-family: var(--font-display); font-weight: 600; font-size: 14px; border: 1.5px solid var(--border); border-radius: 12px; padding: 12px 18px; display: flex; flex-direction: column; gap: 2px; color: var(--ink); text-decoration: none; background: var(--surface); transition: border-color .15s, transform .15s; }
  .badge:hover { border-color: var(--jade); transform: translateY(-1px); }
  .badge span.small { font-size: 11px; font-weight: 500; color: var(--ink-mute); text-transform: uppercase; letter-spacing: 0.05em; }
  .badge span.big { font-size: 15px; }
  .soon-note { font-family: var(--font-display); font-size: 13px; color: var(--ink-mute); }

  .hero-art { position: relative; aspect-ratio: 1; display: grid; place-items: center; }
  .hero-art svg { width: 100%; height: 100%; max-width: 420px; }

  section.band { padding: 64px 24px; }
  section.band.tint { background: var(--surface-2); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); }
  .band-inner { max-width: 1080px; margin: 0 auto; }
  .band h2.section-title { font-size: clamp(26px, 3.4vw, 34px); color: var(--ink); margin: 0 0 12px; text-wrap: balance; }
  .band .section-sub { color: var(--ink-soft); font-size: 18px; font-style: italic; max-width: 56ch; margin-bottom: 44px; }

  .steps { display: grid; grid-template-columns: repeat(4, 1fr); gap: 28px; counter-reset: step; }
  @media (max-width: 860px) { .steps { grid-template-columns: 1fr 1fr; } }
  @media (max-width: 560px) { .steps { grid-template-columns: 1fr; } }
  .step { display: flex; flex-direction: column; gap: 10px; }
  .step .num { font-family: var(--font-display); font-weight: 800; font-size: 34px; color: var(--jade); opacity: 0.35; }
  .step h3 { margin: 0; font-size: 18px; }
  .step p { font-size: 15px; color: var(--ink-soft); margin: 0; }

  .feature-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; }
  @media (max-width: 860px) { .feature-grid { grid-template-columns: 1fr 1fr; } }
  @media (max-width: 560px) { .feature-grid { grid-template-columns: 1fr; } }
  .feature { background: var(--surface); border: 1px solid var(--border); border-radius: 18px; padding: 26px 22px; display: flex; flex-direction: column; gap: 10px; }
  .feature .glyph { width: 40px; height: 40px; border-radius: 12px; display: grid; place-items: center; background: var(--jade-tint); }
  .feature .glyph svg { width: 20px; height: 20px; }
  .feature h3 { margin: 4px 0 0; font-size: 17px; }
  .feature p { font-size: 14.5px; color: var(--ink-soft); margin: 0; }

  .cta-band { text-align: left; }
  .cta-card { background: linear-gradient(155deg, var(--jade) 0%, var(--jade-dark) 100%); color: var(--bg); border-radius: 28px; padding: 52px 44px; display: grid; grid-template-columns: 1.2fr 1fr; gap: 32px; align-items: center; box-shadow: var(--shadow); }
  @media (max-width: 760px) { .cta-card { grid-template-columns: 1fr; padding: 36px 26px; } }
  .cta-card h2 { color: var(--bg); margin: 0 0 10px; }
  .cta-card p { color: color-mix(in srgb, var(--bg) 82%, transparent); margin: 0 0 24px; font-size: 17px; }
  .cta-card .badges .badge { background: rgba(255,255,255,0.08); border-color: rgba(255,255,255,0.35); color: var(--bg); }
  .cta-card .badges .badge span.small { color: color-mix(in srgb, var(--bg) 70%, transparent); }
  .cta-card .badges .badge:hover { border-color: var(--bg); }
  .cta-side { display: flex; align-items: center; justify-content: center; }
  .cta-mark { width: 140px; height: 140px; border-radius: 22.37%; box-shadow: 0 24px 60px -20px rgba(0,0,0,0.45); }

  .contact-band { display: grid; grid-template-columns: 1.2fr 1fr; gap: 40px; align-items: start; }
  @media (max-width: 760px) { .contact-band { grid-template-columns: 1fr; } }
  .contact-card { background: var(--surface); border: 1px solid var(--border); border-radius: 18px; padding: 28px; }
  .contact-card a.email { font-family: var(--font-display); font-weight: 700; font-size: 18px; color: var(--jade); text-decoration: none; }

  /* Entrance motion never starts from opacity:0 — content must be visible at
     rest (a static render, a slow first paint, a crawler all see it either
     way); the animation is a bonus transform-only rise for real browsers. */
  @media (prefers-reduced-motion: no-preference) {
    .reveal { animation: rise .6s ease-out both; }
    .reveal.d1 { animation-delay: .08s; } .reveal.d2 { animation-delay: .16s; } .reveal.d3 { animation-delay: .24s; }
    @keyframes rise { from { transform: translateY(14px); } to { transform: none; } }
    .feature, .step { transition: transform .2s ease; }
    .feature:hover { transform: translateY(-3px); }
  }
"""

HEADER_TMPL = """<header class="top">
    <div class="top-inner">
      <a class="brand" href="/">
        <img class="mark" src="{icon}" alt="">
        <span class="wordmark">Table for More</span>
      </a>
      <nav class="crosslinks" aria-label="Main">
        <a href="/#how-it-works">How it works</a>
        <a href="/support" {s_cur}>Support</a>
        <a href="/#download" class="nav-cta">Coming soon</a>
      </nav>
    </div>
  </header>"""

FOOTER = """<footer class="site">
    <div class="footer-inner">
      <span>&copy; 2026 Lily Jiang</span>
      <span>Toronto, Ontario, Canada</span>
      <nav aria-label="Legal">
        <a href="/privacy">Privacy</a>
        <a href="/terms">Terms</a>
        <a href="/support">Support</a>
        <a href="mailto:support@tableformoreapp.com">Contact</a>
      </nav>
    </div>
  </footer>"""


def doc_page(title_tag, description, eyebrow, h1, meta_html, body_html, current):
    header = HEADER_TMPL.format(icon=ICON_URI, s_cur='aria-current="page"' if current == "support" else "")
    return f"""<title>{title_tag}</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@500;600;700;800&family=Newsreader:ital,wght@0,400;0,500;0,600;1,400&display=swap">
<style>{CSS}</style>
{header}
<main>
  <p class="eyebrow">{eyebrow}</p>
  <h1>{h1}</h1>
  <div class="meta">{meta_html}</div>
  {body_html}
</main>
{FOOTER}
"""


print("template ready")

# ============================== HERO ART (custom SVG) ==============================
# A "gathering" motif: a table (large ellipse) with people/dishes (varied circles)
# around it at different distances, connected by soft threads — echoes the app
# icon's own table+badge language, scaled up into an atmospheric hero graphic
# about community forming, not a literal screenshot.
def hero_svg():
    cx, cy = 210, 210
    table_r = 92
    people = [
        (0, 150, 22, "var(--jade)"),
        (51, 150, 16, "var(--gold)"),
        (103, 150, 19, "var(--coral)"),
        (154, 150, 14, "var(--jade)"),
        (206, 150, 20, "var(--gold)"),
        (257, 150, 15, "var(--coral)"),
        (309, 150, 18, "var(--jade)"),
    ]
    lines = []
    circles = []
    for deg, dist, r, color in people:
        a = math.radians(deg - 90)
        x, y = cx + dist * math.cos(a), cy + dist * math.sin(a)
        lines.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="var(--border)" stroke-width="1.5" stroke-dasharray="1 7" stroke-linecap="round"/>')
        circles.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}" opacity="0.9"/>')
    return f"""<svg viewBox="0 0 420 420" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="An illustration of a round table with people gathered around it">
      <circle cx="{cx}" cy="{cy}" r="205" fill="var(--jade-tint)" opacity="0.5"/>
      {''.join(lines)}
      {''.join(circles)}
      <ellipse cx="{cx}" cy="{cy}" rx="{table_r}" ry="{table_r*0.62:.0f}" fill="var(--surface)" stroke="var(--border)" stroke-width="1.5"/>
      <ellipse cx="{cx}" cy="{cy+6}" rx="{table_r*0.6:.0f}" ry="{table_r*0.3:.0f}" fill="var(--jade-tint)"/>
    </svg>"""

# ============================== HOMEPAGE ==============================
hero = f"""
<section class="hero">
  <div class="reveal">
    <p class="eyebrow">Coming soon on iOS &amp; Android</p>
    <div class="hero-emoji">🍜 🍣 🌮 🍛</div>
    <h1>Try new food. Meet new people. Build a community, one table at a time.</h1>
    <p class="hero-sub">Table for More turns a meal into a real connection &mdash; join a small group at a real restaurant, or host your own, and let the conversation happen.</p>
    <div class="badges">
      <a class="badge" href="#download"><span class="small">Coming soon</span><span class="big">📱 App Store</span></a>
      <a class="badge" href="#download"><span class="small">Coming soon</span><span class="big">▶ Google Play</span></a>
    </div>
    <p class="soon-note">Currently in review &mdash; join is around the corner.</p>
  </div>
  <div class="hero-art reveal d1">{hero_svg()}</div>
</section>
"""

how_it_works = """
<section class="band" id="how-it-works">
  <div class="band-inner">
    <p class="eyebrow">How it works</p>
    <h2 class="section-title">From "I'm hungry" to "I made a friend"</h2>
    <p class="section-sub">Four real steps, no swiping, no small talk with no one listening.</p>
    <div class="steps">
      <div class="step"><span class="num">01</span><h3>Discover</h3><p>Browse real restaurants near you, or search any city &mdash; real menus, real hours, real reviews.</p></div>
      <div class="step"><span class="num">02</span><h3>Join or host</h3><p>Pull up a chair at someone else's Table, or start your own with the time and group size you want.</p></div>
      <div class="step"><span class="num">03</span><h3>Break the ice</h3><p>Your Table gets a group chat before you even sit down, with a few AI conversation starters to open with.</p></div>
      <div class="step"><span class="num">04</span><h3>Build your passport</h3><p>Every Table you finish adds to your Food Passport &mdash; the cuisines you've tried, the people you've met.</p></div>
    </div>
  </div>
</section>
"""

def glyph(path):
    return f'<div class="glyph"><svg viewBox="0 0 24 24" fill="none" stroke="var(--jade)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{path}</svg></div>'

features = f"""
<section class="band tint">
  <div class="band-inner">
    <p class="eyebrow">Built for real connection</p>
    <h2 class="section-title">A community, earned honestly</h2>
    <p class="section-sub">Every part of the app is built around one rule: nothing here should be fake, including the people.</p>
    <div class="feature-grid">
      <div class="feature">
        {glyph('<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 3v18M3 9h5"/>')}
        <h3>Real restaurants</h3>
        <p>Actual menus, real opening hours, and dietary tags &mdash; pulled from the restaurant's own website, never invented.</p>
      </div>
      <div class="feature">
        {glyph('<path d="M12 21s-7-4.5-9.5-9A5.5 5.5 0 0 1 12 6a5.5 5.5 0 0 1 9.5 6c-2.5 4.5-9.5 9-9.5 9z"/>')}
        <h3>Food Passport</h3>
        <p>A growing, private record of restaurants tried, cuisines explored, and people you've genuinely met over a meal.</p>
      </div>
      <div class="feature">
        {glyph('<path d="M12 2l2.9 6.3 6.9.9-5 4.8 1.2 6.9-6-3.3-6 3.3 1.2-6.9-5-4.8 6.9-.9z"/>')}
        <h3>Reputation you earn</h3>
        <p>Your public standing is built only by people who genuinely finished a real Table with you &mdash; never a stranger's grudge.</p>
      </div>
      <div class="feature">
        {glyph('<path d="M12 3l8 4v5c0 5-3.5 8.5-8 9-4.5-.5-8-4-8-9V7z"/>')}
        <h3>Safety first</h3>
        <p>Report anything, any time. Messages, feedback, and photos are automatically screened, not reviewed after the fact.</p>
      </div>
    </div>
  </div>
</section>
"""

download = f"""
<section class="band cta-band" id="download">
  <div class="band-inner">
    <div class="cta-card">
      <div>
        <h2>Get a seat at the table</h2>
        <p>Table for More is finishing up App Store &amp; Google Play review. Check back soon &mdash; or bookmark this page and we'll be here.</p>
        <div class="badges">
          <a class="badge" href="#"><span class="small">Coming soon</span><span class="big">📱 App Store</span></a>
          <a class="badge" href="#"><span class="small">Coming soon</span><span class="big">▶ Google Play</span></a>
        </div>
      </div>
      <div class="cta-side"><img class="cta-mark" src="{ICON_URI}" alt="Table for More app icon"></div>
    </div>
  </div>
</section>
"""

contact = """
<section class="band">
  <div class="band-inner contact-band">
    <div>
      <p class="eyebrow">Questions?</p>
      <h2 class="section-title">We're a real person away.</h2>
      <p class="section-sub">Whether it's a question before you download, feedback, or something that needs reporting &mdash; we read every message.</p>
    </div>
    <div class="contact-card">
      <p style="margin-bottom:6px;">Email us directly</p>
      <a class="email" href="mailto:support@tableformoreapp.com">support@tableformoreapp.com</a>
      <p style="margin-top:16px; margin-bottom:0;">Or see our <a href="/support">Support &amp; FAQ</a> page for answers to common questions.</p>
    </div>
  </div>
</section>
"""

homepage_header = HEADER_TMPL.format(icon=ICON_URI, s_cur="")
homepage = f"""<title>Table for More</title>
<meta name="description" content="Try new food, meet new people, and build a real community over a shared table. Coming soon on iOS and Google Play.">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@500;600;700;800&family=Newsreader:ital,wght@0,400;0,500;0,600;1,400&display=swap">
<style>{CSS}</style>
{homepage_header}
{hero}
{how_it_works}
{features}
{download}
{contact}
{FOOTER}
"""
Path("index.html").write_text(homepage)
print("index.html", len(homepage), "bytes")

# ============================== PRIVACY POLICY ==============================
privacy_meta = '<span><strong>Effective</strong> September 17, 2026</span><span><strong>Applies to</strong> the Table for More app and website</span>'

privacy_body = """
<p class="lede">Table for More is built around meeting real people over a real meal — this page explains, plainly, what we collect to make that possible and what we do with it.</p>

<h2>Who we are</h2>
<p>Table for More is operated by Lily Jiang, an individual based in Toronto, Ontario, Canada. This policy applies to the Table for More mobile app and any associated website.</p>

<h2>Information we collect</h2>
<p>You can look around the app &mdash; restaurants, cuisines, real menus &mdash; as a guest, without an account and without us collecting anything about you. Creating an account and using the social features of the app requires the following:</p>

<div class="tablewrap"><table>
<tr><th>Category</th><th>What it includes</th></tr>
<tr><td>Account info</td><td>Email address, phone number, birthday, full legal name, and a chosen username</td></tr>
<tr><td>Profile</td><td>A profile photo, an optional bio, your favorite cuisines, and &ldquo;food personality&rdquo; tags you choose</td></tr>
<tr><td>Content you create</td><td>Food photos you post, messages you send in a Table's group chat, restaurant reviews, and feedback about tablemates</td></tr>
<tr><td>Activity</td><td>Restaurants you've visited, Tables you've hosted or joined, and check-in times &mdash; this builds your private Food Passport</td></tr>
<tr><td>Location</td><td>Your device's approximate location, only while the app is open and only if you grant permission, used to find nearby restaurants</td></tr>
<tr><td>Safety reports</td><td>Reports you submit about a message, person, photo, or Table, including any details you write</td></tr>
</table></div>

<p>We do not collect health data, payment/financial information, or precise background location. We do not use advertising trackers, and Table for More does not request App Tracking Transparency permission because we don't track you across other companies' apps or websites.</p>

<h2>How we use your information</h2>
<ul>
<li>To operate the core features of the app &mdash; finding restaurants, creating and joining Tables, group chat, reviews, and your Food Passport</li>
<li>To keep the community safe &mdash; screening messages, photos, and feedback for policy violations, and acting on reports</li>
<li>To generate AI conversation starters for a Table's chat, based on the cuisines and interests of the real people attending</li>
<li>To send you account-related email (confirming your address, password resets) and local reminders on your own device (a check-in nudge after a Table starts) &mdash; we do not send marketing email</li>
<li>To prevent abuse, such as one person creating many accounts or spamming Tables</li>
</ul>

<h2>Your public profile</h2>
<p>Your name, username, avatar, favorite cuisines, food personality tags, and reputation score (built only from people who genuinely shared a finished Table with you) are visible to other signed-in members. Your email, phone number, birthday, and private dining history are never shown to other members.</p>

<h2>Third-party services we use</h2>
<p>We rely on a small number of specialized providers to run the app. None of them are permitted to use your information for their own advertising.</p>

<div class="tablewrap"><table>
<tr><th>Service</th><th>What it's used for</th><th>What it may receive</th></tr>
<tr><td>Supabase</td><td>Our database, authentication, and file storage &mdash; effectively all app data lives here</td><td>All account and content data described above</td></tr>
<tr><td>Anthropic (Claude)</td><td>Generates Table icebreakers, screens chat messages, feedback, and food photos for content that violates our guidelines, and writes restaurant descriptions from public restaurant websites</td><td>Message text, photo images, and restaurant preference data being screened or used to generate a response &mdash; never your email, phone, or full account details</td></tr>
<tr><td>Google Places</td><td>A fallback source for restaurant details (cuisine, photos, hours) when free sources don't have them</td><td>Restaurant search coordinates &mdash; not your personal account data</td></tr>
<tr><td>OpenStreetMap</td><td>The primary source of real-world restaurant listings</td><td>Restaurant search coordinates</td></tr>
<tr><td>Unsplash</td><td>Stock photography for restaurants that don't have their own photo</td><td>No personal data</td></tr>
<tr><td>Brevo</td><td>Delivers account emails (confirmation codes, password resets)</td><td>Your email address, for the message being sent</td></tr>
<tr><td>hCaptcha</td><td>Distinguishes real people from automated bots during sign-up and login</td><td>Device and browser signals, per hCaptcha's own privacy policy</td></tr>
</table></div>

<h2>Data storage &amp; security</h2>
<p>Your data is encrypted in transit and at rest. On your device, your session is stored in your phone's secure hardware keystore (Apple's Keychain or Android's Keystore), not in plain, unencrypted storage. Database access is restricted row-by-row so that, for example, one member can never read another member's email, phone number, or birthday.</p>

<h2>Your rights &amp; choices</h2>
<ul>
<li><strong>Access &amp; correction</strong> &mdash; view and edit your profile at any time from Settings.</li>
<li><strong>Location &amp; notifications</strong> &mdash; both are optional and can be turned off in your device settings; the app works without them, with reduced convenience.</li>
<li><strong>Deletion</strong> &mdash; delete your account and personal data from Settings at any time. This is not a blanket erasure of everything tied to your activity: if you hosted a Table, it stays visible to the other real people who attended (their own Food Passport and reviews depend on it), but it's no longer linked to your identity.</li>
</ul>

<h2>Children's privacy</h2>
<p>Table for More is meant for adults meeting other adults in person and is not directed at anyone under 18. We do not knowingly collect information from anyone under 18.</p>

<h2>International users</h2>
<p>Table for More is operated from Canada. If you use the app from another country, your information is transferred to and processed in Canada and in the countries where our service providers above operate.</p>

<h2>Changes to this policy</h2>
<p>If we make a material change to this policy, we'll update the effective date above and, where required by law, notify you directly.</p>

<h2>Contact us</h2>
<p>Questions about this policy or your data can be sent to <a href="mailto:support@tableformoreapp.com">support@tableformoreapp.com</a>.</p>
"""

# ============================== TERMS OF SERVICE ==============================
terms_meta = '<span><strong>Effective</strong> September 17, 2026</span><span><strong>Governing law</strong> Ontario, Canada</span>'

terms_body = """
<p class="lede">Please read these Terms carefully — they cover a service built around meeting real strangers for a real meal, so a few sections matter more than the usual boilerplate.</p>

<h2>1. Acceptance of terms</h2>
<p>By creating an account or using Table for More (&ldquo;the app,&rdquo; &ldquo;the service&rdquo;), you agree to these Terms of Service. If you don't agree, please don't use the app. The app is operated by Lily Jiang (&ldquo;we,&rdquo; &ldquo;us&rdquo;).</p>

<h2>2. Eligibility</h2>
<p>You must be at least 18 years old to create an account. By registering, you confirm that you're 18 or older and that the information you provide &mdash; including your name and date of birth &mdash; is accurate.</p>

<h2>3. Description of service</h2>
<p>Table for More helps you discover restaurants and organize or join small-group meetups (&ldquo;Tables&rdquo;) with other members. You can also browse the app without an account as a guest, with reduced functionality.</p>

<h2>4. Your account</h2>
<p>You're responsible for keeping your login credentials secure and for all activity under your account. Tell us right away at <a href="mailto:support@tableformoreapp.com">support@tableformoreapp.com</a> if you believe your account has been compromised.</p>

<h2>5. Community guidelines</h2>
<p>Table for More only works if people treat each other well. You agree not to:</p>
<ul>
<li>Harass, threaten, or discriminate against another member</li>
<li>Post content that is illegal, sexually explicit, or promotes violence</li>
<li>Impersonate another person or create a fake or duplicate account</li>
<li>Use the app to solicit, sell, or advertise outside its intended purpose</li>
<li>Attempt to circumvent our safety, moderation, or rate-limiting systems</li>
</ul>
<p>We may remove content, suspend, or terminate accounts that violate these guidelines, with or without notice, at our discretion.</p>

<h2>6. Content you post</h2>
<p>You keep ownership of the photos, messages, and reviews you post. By posting them, you give us a license to store, display, and process that content as needed to operate the app &mdash; for example, showing your food photo to other members, or screening a message for policy violations. Messages, photos, and feedback may be automatically or manually reviewed for content that violates these Terms.</p>

<div class="callout warn">
<p><strong>Tables are not restaurant reservations.</strong> Joining or hosting a Table books your spot in the social group only. It does not create, guarantee, or imply any reservation with the restaurant itself. Where we can find one, we link to the restaurant's own real reservation page &mdash; making that reservation, if you want one, is between you and the restaurant.</p>
</div>

<h2>7. Meeting other members</h2>
<div class="callout warn">
<p>Table for More helps you find and meet new people in person. We do not conduct background checks on members, and we cannot guarantee the identity, intentions, or conduct of anyone you meet through the app. You are solely responsible for your own safety when meeting another member. We encourage meeting in the public setting a Table provides, telling someone else where you're going, and using the in-app reporting tools if anything feels wrong.</p>
</div>

<h2>8. Reporting &amp; moderation</h2>
<p>You can report a message, a person, a photo, or a Table at any time from within the app. We review reports and take action we consider appropriate, which may include removing content or suspending an account, at our discretion and without obligation to explain our reasoning to any party involved.</p>

<h2>9. Third-party services &amp; links</h2>
<p>The app may link to restaurants' own websites or reservation systems, and relies on third-party data providers described in our <a href="/privacy">Privacy Policy</a>. We don't control those third parties and aren't responsible for their content, accuracy, or availability.</p>

<h2>10. Disclaimer of warranties</h2>
<p>The app is provided &ldquo;as is&rdquo; and &ldquo;as available,&rdquo; without warranties of any kind, express or implied. We don't guarantee the app will be uninterrupted, error-free, or that any restaurant information (hours, menu, availability) is perfectly current.</p>

<h2>11. Limitation of liability</h2>
<p>To the fullest extent permitted by law, Lily Jiang will not be liable for any indirect, incidental, or consequential damages arising from your use of the app, including anything arising from your interactions with other members or restaurants, whether met through the app or not.</p>

<h2>12. Indemnification</h2>
<p>You agree to indemnify and hold us harmless from any claim or demand arising from your use of the app or your violation of these Terms.</p>

<h2>13. Termination</h2>
<p>You may delete your account at any time from Settings. We may suspend or terminate your access for violating these Terms or our community guidelines.</p>

<h2>14. Changes to these terms</h2>
<p>We may update these Terms from time to time. If we make a material change, we'll update the effective date above.</p>

<h2>15. Governing law</h2>
<p>These Terms are governed by the laws of the Province of Ontario and the laws of Canada applicable therein, without regard to conflict-of-law principles.</p>

<h2>16. Contact us</h2>
<p>Questions about these Terms can be sent to <a href="mailto:support@tableformoreapp.com">support@tableformoreapp.com</a>.</p>
"""

# ============================== SUPPORT / FAQ ==============================
support_meta = '<span><strong>We usually reply within</strong> 1&ndash;2 business days</span>'

def faq(q, a):
    return f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>'

support_body = """
<p class="lede">Answers to the questions we hear most. Can't find yours? Email us at the bottom of the page.</p>
""" + "".join([
    faq("What is Table for More?", "An app for finding real restaurants near you and sharing the table with a small group of new people — you can join a Table someone else has already started, or host your own."),
    faq("Do I need an account?", "No — you can browse restaurants, cuisines, and real menus as a guest. You'll need a free account once you want to actually join or host a Table, chat, or post a food photo."),
    faq("How do Tables work?", "Pick a restaurant, then either join an existing Table with an open seat or host your own by choosing the time and group size. Everyone joining gets a group chat before the Table starts."),
    faq("What if I'm running late or can't make it?", "Mark yourself &ldquo;Running Late&rdquo; from the Table screen so the group knows — it pauses the no-show clock. If you can't make it at all, you can back out before the Table starts."),
    faq("Is booking a Table the same as a restaurant reservation?", "No. Joining or hosting a Table only books your spot in the social group. Where we've found one, we link to the restaurant's own real reservation page — making an actual reservation is between you and the restaurant."),
    faq("How do the AI conversation starters work?", "Once your Table's chat is empty and everyone's about to meet, we generate a few short icebreakers based on the restaurant and the real interests of who's coming — they disappear once anyone actually starts chatting."),
    faq("Is my location shared with other members?", "No. Your location is only used, with your permission, to show you nearby restaurants on your own device — it's never shown to other members or attached to your profile."),
    faq("How is my safety protected?", "You can report a message, a person, a photo, or a Table at any time, not just afterward. Messages, photos, and feedback are automatically screened for content that violates our guidelines, and reports are reviewed by us directly."),
    faq("How does reputation work?", "After a Table, you and your tablemates can rate each other. Your public reputation is built only from people who genuinely finished a real Table with you — a stranger can't affect your score without actually having shared a meal with you."),
    faq("How do I delete my account and data?", "Go to Settings &rarr; Delete Account. This removes your personal data; if you hosted a Table, it stays visible to the other real people who attended, since their own history depends on it, but it's no longer linked to your identity."),
    faq("I found a bug, or have feedback.", "We'd genuinely like to hear it — email us at the address below with as much detail as you can (what you were doing, what you expected, what happened instead)."),
])

# ============================== WRITE ==============================
Path("privacy.html").write_text(doc_page(
    "Privacy Policy — Table for More", "How Table for More collects, uses, and protects your data.",
    "Legal", "Privacy Policy", privacy_meta, privacy_body, "privacy"))
Path("terms.html").write_text(doc_page(
    "Terms of Service — Table for More", "The terms governing your use of Table for More.",
    "Legal", "Terms of Service", terms_meta, terms_body, "terms"))
Path("support.html").write_text(doc_page(
    "Support — Table for More", "Frequently asked questions and how to reach the Table for More team.",
    "Help", "Support &amp; FAQ", support_meta, support_body, "support"))

for f in sorted(Path(".").glob("*.html")):
    print(f.name, len(f.read_text()), "bytes")
