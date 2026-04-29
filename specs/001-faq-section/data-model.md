# Phase 1 Data Model: FAQ Entries

**Feature**: 001-faq-section
**Date**: 2026-04-28

There is one entity in this feature, stored in **`data/faq.yaml`** and consumed by the `rn-faq` Hugo shortcode.

## Entity: FAQ Entry

| Field      | Type   | Required | Description |
|------------|--------|----------|-------------|
| `question` | string | Yes      | The question text. Plain text, no Markdown (renders inside `<summary>`). Should be written naturally — sentence case, ending with `?`. |
| `answer`   | string | Yes      | The answer body. Markdown — supports paragraphs, links, lists, emphasis, inline code. Authored using a YAML literal block scalar (`|`). |
| `id`       | string | No       | Optional explicit anchor override. Lowercase, kebab-case, alphanumeric + hyphens only. If omitted, defaults to `faq-{{ urlize question }}`. |

## File: `data/faq.yaml`

The data file has a single top-level key `entries` whose value is an ordered list of FAQ Entry objects. Order in the list = render order on the page.

```yaml
entries:
  - question: What is ReproNim?
    answer: |
      ReproNim is a national biotechnology development center dedicated to
      tools and services for reproducible neuroimaging. See the
      [About page](/about/) for more.

  - question: How do I get started?
    answer: |
      Visit the [Getting Started](/resources/getting-started/) page for an
      overview, or browse the [tools page](/resources/tools/).

  - id: fellowship-apply
    question: How do I apply to the ReproNim Fellowship?
    answer: |
      Application details and the current cycle are on the
      [Fellowship page](/fellowship/).
```

## Validation rules

These are enforced by the shortcode template at render time. Failures during `hugo build` mean the home page won't deploy until the YAML is fixed — surfacing problems to the maintainer immediately.

1. **`question` is non-empty.** A blank question would produce an empty `<summary>` and an unreachable id. The shortcode skips entries with no `question` and emits a build warning.
2. **`answer` is non-empty.** A missing answer makes the entry pointless. Skipped with warning.
3. **Anchor uniqueness.** The shortcode tracks ids it has already emitted in the current page; on a duplicate, it appends `-2`, `-3`, etc. to disambiguate, and emits a build warning so the maintainer can fix the source. (Two distinct questions can occasionally produce the same slug, e.g. capitalization-only differences.)
4. **`id` format (when provided).** Must match the regex `^[a-z0-9][a-z0-9-]*$`. Invalid ids fall back to the auto-generated slug and emit a build warning.

## Anchor URL examples

For a question `"How do I get started?"` with no `id` override:

- Anchor: `faq-how-do-i-get-started`
- Deep-link URL: `https://repronim.org/#faq-how-do-i-get-started`

For an entry with `id: fellowship-apply`:

- Anchor: `fellowship-apply`
- Deep-link URL: `https://repronim.org/#fellowship-apply`

## Lifecycle

FAQ Entries have no runtime lifecycle — they are static content rebuilt each deploy. The maintainer-facing operations are:

| Operation | Action |
|-----------|--------|
| Add | Append a new list item to `data/faq.yaml`. |
| Edit | Modify the `question` or `answer` of an existing item. Editing the question changes its auto-generated anchor unless an explicit `id` is in place. |
| Reorder | Move list items up/down in the YAML. |
| Remove | Delete the list item. Outstanding deep-links to the removed anchor become inert (page loads cleanly per FR-011). |
| Add a stable anchor to an existing entry | Add an explicit `id:` field, preferably matching the previous auto-generated slug, so existing deep-links keep working. |

## Relationship to other entities

None — FAQ Entries are self-contained leaf data with no foreign keys to other site content.
