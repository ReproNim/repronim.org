# Publication Generation

Regenerate publications from DOIs in `data/publications.yaml`:

Run from the root of this repo:

```bash
datalad run -m "Generate publications from DOIs" \
  --input data/publications.yaml \
  --output content/about/publications.md \
  "uv run python scripts/generate_publications.py"
```
