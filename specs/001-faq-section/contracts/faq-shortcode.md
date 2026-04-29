# Contract: `rn-faq` Hugo Shortcode

**Feature**: 001-faq-section
**Date**: 2026-04-28

This is the public contract the FAQ shortcode exposes to the rest of the site. It defines the input it consumes, the output HTML it produces, and the interaction guarantees that downstream tests (manual + automated accessibility) can verify against.

## Invocation

In a content file (e.g., `content/_index.md`):

```markdown
{{< rn-faq >}}
```

The shortcode takes **no positional or named arguments**. All content comes from `site.Data.faq`.

Optional named argument (future-friendly, not used at v1):

| Argument | Type   | Default | Purpose |
|----------|--------|---------|---------|
| `title`  | string | `"Frequently Asked Questions"` | Override the section heading text. |

## Input contract

The shortcode reads `site.Data.faq.entries` (i.e., the `entries:` list inside `data/faq.yaml`).

- If `data/faq.yaml` does not exist, or `entries` is missing, or `entries` is empty: the shortcode emits **no output**.
- If `entries` is non-empty: each item must conform to the schema in `data-model.md`. Invalid items are skipped with a Hugo build warning; the rest still render.

## Output contract

For a non-empty `entries` list, the shortcode emits this HTML structure:

```html
<section class="rn-faq" aria-labelledby="rn-faq-heading">
  <h2 id="rn-faq-heading">Frequently Asked Questions</h2>

  <details id="faq-what-is-repronim" class="rn-faq-item">
    <summary>What is ReproNim?</summary>
    <div class="rn-faq-answer">
      <!-- markdownified answer HTML -->
    </div>
  </details>

  <details id="faq-how-do-i-get-started" class="rn-faq-item">
    <summary>How do I get started?</summary>
    <div class="rn-faq-answer">
      <!-- markdownified answer HTML -->
    </div>
  </details>

  <!-- one <details> per entry, in YAML order -->

  <style>/* scoped styles for .rn-faq, .rn-faq-item, .rn-faq-answer */</style>
  <script>/* deep-link expansion handler */</script>
</section>
```

### Guaranteed properties

- The wrapping element is a `<section>` with class `rn-faq` and an `aria-labelledby` pointing at the heading. Assistive tech announces the section as a named region.
- The heading is `<h2>` so it slots correctly under the home page's `<h1>` title.
- Each entry is a `<details>` element with:
  - A unique `id` (per `data-model.md` rules).
  - The class `rn-faq-item`.
  - A child `<summary>` containing the plain-text question.
  - A child `<div class="rn-faq-answer">` containing the rendered Markdown answer.
- No `open` attribute is set server-side — every entry renders collapsed (FR-002a).
- The `<style>` and `<script>` blocks are scoped to `.rn-faq` selectors and behavior — they do not affect the rest of the page.

### Style guarantees

The scoped CSS must:

- Inherit text color and background from the active theme so light/dark mode work without overrides (FR-009).
- Provide adequate spacing between entries (≥ 0.75 rem vertical) and a visible focus ring on `<summary>` for keyboard users.
- Maintain WCAG 2.1 AA contrast (FR-007). Don't override Hextra's link colors inside `.rn-faq-answer`.
- Replace the default disclosure triangle with a styled chevron only if the substitution preserves accessibility — otherwise leave the browser default (acceptable per FR-007).

### Script guarantees

The inline `<script>` must:

- Run on initial load and on every `hashchange`.
- If the URL hash matches the `id` of an `<details>` inside `.rn-faq`, set `open = true` and call `scrollIntoView({ block: 'start' })`.
- Do nothing else. No analytics, no state mutation outside the targeted element, no event listeners on `<summary>` (the browser handles those natively).
- Be wrapped in an IIFE to avoid leaking globals.

## Behavioral guarantees (verifiable from this contract)

| ID  | Behavior | How to verify |
|-----|----------|---------------|
| C1  | Section is hidden when no entries exist | Remove `data/faq.yaml`; rebuild; confirm no `<section class="rn-faq">` in `public/index.html`. |
| C2  | Entries render in YAML order | View page source; confirm `<details>` ids appear in the same order as YAML list. |
| C3  | Each entry collapsed by default (no anchor) | Load `/`; confirm no `<details>` has the `open` attribute. |
| C4  | Deep link opens the targeted entry | Load `/#faq-how-do-i-get-started`; confirm the matching `<details>` has `open=true` and is in view. |
| C5  | Invalid anchor is harmless | Load `/#faq-does-not-exist`; confirm the page renders normally with all entries collapsed. |
| C6  | Multiple entries can be open simultaneously | Click two `<summary>` elements; confirm both stay open. |
| C7  | Keyboard operable | Tab to a `<summary>`; press Enter or Space; confirm it expands; press again to collapse. |
| C8  | Screen-reader expanded state | Inspect with VoiceOver/NVDA; confirm `<summary>` announces expanded/collapsed correctly (provided natively by `<details>`). |
| C9  | Theme adaptation | Toggle light/dark; confirm contrast meets AA in both. |
| C10 | Markdown links in answers work | Add an answer with `[link](/about/)`; click it; confirm navigation. |
| C11 | Search indexing | Site search returns FAQ answer text when querying for a phrase that appears only in an answer. |

## Non-contract (intentionally unspecified)

These are implementation freedoms left to whoever writes the shortcode:

- The exact CSS values (colors, font sizes, spacing) — must respect theme tokens and contrast, but specific numbers are tunable.
- Whether to use a custom chevron `::after` pseudo-element or the browser default disclosure triangle.
- Whether to memoize `urlize` results across iterations (a Hugo perf detail with no observable effect).
- Future expansion: optional `title` argument and optional per-entry `tag` field for grouping. Not in v1.
