# Marlow website

The public home page, Privacy Policy and Terms of Use for the Marlow iPhone app (called Financialyst before 20 Nov 2026), served by GitHub Pages at
https://fwh0115.github.io/marlow/ (`/privacy/` and `/terms/`). This repository is the user site
fwh0115.github.io: the site itself is in `marlow/`, and the root `index.html` only sends visitors there. The app's code lives in a separate private repo;
nothing here gives access to it.

The policies are written once, in the app repo (`ft_app/assets/legal/*.md`), and shown by both the app and this site.

To update the policies here:

1. Copy `privacy-policy.md` and `terms-of-use.md` from the app repo into `source/`.
2. Run `python3 build.py` (needs `pip install markdown`).
3. Commit and push. GitHub Pages republishes within a couple of minutes.

The home page (`marlow/index.html`) and `marlow/style.css` are edited by hand.

Keep both `googleea078d447db6bcce.html` files (the root and `marlow/`): Google Search Console checks them to keep
the site verified, which Google's sign-in branding needs.
