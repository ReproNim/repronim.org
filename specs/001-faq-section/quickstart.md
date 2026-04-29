# Quickstart: Adding & Editing FAQ Entries

**Feature**: 001-faq-section
**Audience**: ReproNim maintainers (anyone already comfortable editing site Markdown via GitHub)
**Time to add a new entry**: ~5 minutes

This guide assumes the FAQ feature has been implemented and shipped. If it hasn't, see `tasks.md` (created by `/speckit-tasks`) for the implementation steps.

## TL;DR

To add an FAQ entry, edit one file: **`data/faq.yaml`** in the repo. Append a new list item under `entries:`, commit, and the question appears on the home page after the next Netlify deploy.

## Step-by-step: add a new FAQ entry

1. **Open `data/faq.yaml`** on GitHub. The "Edit this page" workflow that already works for site Markdown also works for data files — open the file in the GitHub UI and click the pencil icon.

2. **Append a new list item** under `entries:`. Use this template:

   ```yaml
     - question: Your question goes here?
       answer: |
         Your answer goes here. You can use **Markdown**:
         - Lists work.
         - [Links](/resources/) work.
         - `Inline code` works.
   ```

   Notes:
   - The `|` after `answer:` is YAML's literal block scalar. It lets you write multi-line Markdown naturally.
   - Indent the answer body two spaces past the `answer:` key, as shown.

3. **(Optional) Set a stable anchor** by adding an explicit `id:` field. Recommended whenever you expect the question wording might change later but you want existing deep links to keep working.

   ```yaml
     - id: fellowship-apply
       question: How do I apply to the ReproNim Fellowship?
       answer: |
         See the [Fellowship page](/fellowship/).
   ```

   Without `id:`, the anchor is auto-generated from the question slug — fine for stable wording, but a reworded question changes the URL.

4. **Commit and push.** Use a conventional-commit message such as `docs: add FAQ entry on fellowship deadlines`. A pull request triggers Netlify's preview deploy; merging to `main` triggers production.

5. **Verify.** After deploy:
   - Open `https://repronim.org/` and scroll to the FAQ section.
   - Click your new question; the answer should expand.
   - Copy the URL of the question's anchor (right-click the question → "Copy link" works in most browsers, or check the rendered page source for the `<details id="...">`).
   - Paste the deep-link URL in a new tab; confirm the page loads with your entry already expanded and scrolled into view.

## Step-by-step: edit or remove an entry

- **Edit**: Change `question` or `answer` in place. Reordering, formatting, and link changes are all in-place edits.
- **Reorder**: Move the list item up or down within `entries:`. Render order = YAML order.
- **Remove**: Delete the list item. If you anticipate that outstanding deep links exist (e.g., the question was linked from an email or another page), consider replacing it with a redirect-style answer that points to the new location instead of deleting outright.

## Anchor stability tips

- The auto-generated anchor for a question is `faq-` + the URL-friendly slug of the question. Example: `"How do I get started?"` → `faq-how-do-i-get-started`.
- To preserve a deep link across a rewording, set `id:` to the previous slug **before** changing the question text. Example: change to `id: faq-how-do-i-get-started`, then update `question:` freely.

## Common pitfalls

| Symptom | Cause | Fix |
|---------|-------|-----|
| New entry doesn't appear on the home page | YAML indentation is wrong (Netlify build will have failed) | Check the build log on Netlify for a YAML parse error; fix indentation so each list item starts with `  - question:`. |
| Answer renders as a single long line | Used `>` (folded scalar) instead of `|` (literal scalar) for `answer:` | Use `|` to preserve newlines. |
| Markdown link looks like raw text in the answer | The answer string is being treated as plain text | Confirm the YAML uses `answer: |` (with the pipe) and that the answer is indented correctly. The shortcode runs `markdownify` on the value. |
| Deep link doesn't open the entry | Hash in URL doesn't match any entry's id (typo, stale link, or entry was removed) | Verify the current id by inspecting the page or by checking `data/faq.yaml` for an `id:` override. |
| Duplicate ids warning in build log | Two questions slugify to the same anchor (e.g., differ only in punctuation) | Add an explicit `id:` to one of them. |

## Verifying accessibility (occasional check)

When the FAQ grows or styles change, run an accessibility check on the home page:

- **Lighthouse** (Chrome DevTools → Lighthouse → "Accessibility") — score should be ≥ 95 with no FAQ-related findings.
- **axe DevTools** browser extension — run on `/`; confirm no violations under the `.rn-faq` section.
- Keyboard test: Tab to a question; press Enter; press Tab again to confirm focus moves into the answer's links.

## Where the implementation lives

- Data: `data/faq.yaml`
- Shortcode template: `layouts/shortcodes/rn-faq.html`
- Invocation: `content/_index.md` (one `{{< rn-faq >}}` line below the `rn-buttons` block)

If you need to change the section heading, the styling, or the script, edit `layouts/shortcodes/rn-faq.html`. For everyday content edits, you only need `data/faq.yaml`.
