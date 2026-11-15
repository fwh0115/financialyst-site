# Financialyst website

The public home page, Privacy Policy and Terms of Use for the Financialyst iPhone app, served by GitHub Pages at
https://fwh0115.github.io/financialyst/ (`/privacy/` and `/terms/`). The app's code lives in a separate private repo;
nothing here gives access to it.

The policies are written once, in the app repo (`ft_app/assets/legal/*.md`), and shown by both the app and this site.

To update the policies here:

1. Copy `privacy-policy.md` and `terms-of-use.md` from the app repo into `source/`.
2. Run `python3 build.py` (needs `pip install markdown`).
3. Commit and push. GitHub Pages republishes within a couple of minutes.

The home page (`index.html`) and `style.css` are edited by hand.
