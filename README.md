# Table for More — Website

The public site for [tableformoreapp.com](https://tableformoreapp.com) — marketing homepage, Privacy Policy, Terms of Service, and Support/FAQ, served via GitHub Pages.

Source of truth is `build-site.py`, which generates all four HTML pages from one shared design system (Deep Jade / Warm Ivory, Bricolage Grotesque + Newsreader). Regenerate after any copy or design change:

```
python3 build-site.py
```

This is a separate repo from the app's private source (`tableformore`) so the site can be public without exposing app code.
