# noamankhalil.com

Personal site for Noaman Khalil. The layout follows [attacomsian.com](https://attacomsian.com/): a narrow column, a sticky bar, project tiles, a short archive, a now page, and an about page. The words, products, and portrait are Noaman’s.

Pages:

- `/` home
- `/blog` writing, with topic filters and ⌘K search
- `/now` what is actually in progress
- `/judging` how he reviews a product, past events (2023 CODiE Awards, EdAI in Berkeley), and how to invite him
- `/about`
- six notes under `/blog/`

Open it with any static server from this folder:

```bash
python3 -m http.server 4173
```

Regenerate the HTML after editing `scripts/build_site.py`:

```bash
python3 scripts/build_site.py
```

Figures on the now page are dated November 1, 2026 and cite trybondi.app, wigglemac.com, or GitHub. Bondi’s price and launch day follow the product page. If those change, update the generator and rebuild.
