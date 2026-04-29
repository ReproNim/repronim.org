# Phase 0 Research: FAQ Section on Home Page

**Feature**: 001-faq-section
**Date**: 2026-04-28

The Technical Context for this feature has no `NEEDS CLARIFICATION` markers — Hugo, Hextra, the data-file pattern, and the deployment pipeline are already in use across the site. The remaining open questions are *implementation choices* that the spec leaves to planning. Each is resolved below with a decision, rationale, and the alternatives that were considered.

---

## R1. Accordion mechanism: native `<details>` vs. custom JS

**Decision**: Use the HTML5 `<details>`/`<summary>` element as the primitive for each FAQ entry, with Markdown-rendered answer content inside.

**Rationale**:
- Built-in semantics: keyboard focus, Enter/Space toggling, and `aria-expanded` state are handled by the browser. This satisfies FR-007 and SC-004 with no extra ARIA wiring.
- Zero JavaScript required for the core expand/collapse behavior. Visitors with JS disabled still get a fully functional FAQ.
- HTML5 `<details>` is supported in every browser the site targets (last two majors of Chrome, Firefox, Safari, Edge — universal since ~2020).
- Multiple entries can be open simultaneously by default, satisfying FR-003. We deliberately do **not** group entries with `name="faq"` (HTML5 exclusive accordions), because that would force collapsing one to view another.
- Theme-friendly: `<summary>` is a normal element that inherits color and font tokens from the Hextra theme; no theme-specific styling is needed beyond a small marker tweak.

**Alternatives considered**:
- *Custom `<button aria-expanded>` + `<div role="region">`*: requires hand-rolled keyboard handling and ARIA management. More code, more risk of accessibility regression. Rejected.
- *Hextra's `card` or `callout` shortcode reused as a faux accordion*: not designed for this purpose; would not collapse and would not deep-link cleanly. Rejected.
- *A third-party accordion JS library*: adds a dependency for a feature that the platform handles natively. Rejected.

---

## R2. Content storage: data file vs. Markdown shortcode-per-entry vs. content bundle

**Decision**: Store entries in **`data/faq.yaml`**, a single YAML file with an `entries:` list, each item having `question`, `answer` (Markdown string), and an optional `id` override. The shortcode reads this file via `site.Data.faq`.

**Rationale**:
- One source of truth. A maintainer adds, removes, or reorders entries by editing one file via the existing GitHub "Edit this page" workflow. Satisfies FR-005 and SC-003.
- Order in the YAML list = render order. Satisfies FR-006.
- Matches the established site precedent: `data/fellows-2024.yaml`, `data/repronim-team.yaml`, `data/publications.yaml` are all structured YAML consumed by shortcodes/partials.
- Markdown answers are rendered with Hugo's `markdownify` function, so links, lists, inline code, and emphasis work without special handling. Satisfies FR-004.
- Anchors are derived deterministically from the question via Hugo's `urlize` (or `anchorize`) function, with an explicit `id` override available for stability if a question is reworded later. Satisfies FR-010.

**Alternatives considered**:
- *Per-entry shortcode calls inside `_index.md`* (e.g., `{{< rn-faq-item q="..." >}}` with body content): more verbose, harder to reorder, mixes structure and content in a single file. Rejected.
- *Hugo content bundle under `content/faq/` with one Markdown page per entry*: overkill for a section-of-a-page feature; pulls in page-level concerns (taxonomies, list templates) that we don't need. Rejected.
- *Front matter list in `_index.md`*: works for tiny lists but conflates page metadata with body content. Rejected for clarity.

---

## R3. Deep-linking and default expansion state

**Decision**: All entries render with `<details>` collapsed (no `open` attribute) on the server. A tiny inline `<script>` inside the shortcode runs on `DOMContentLoaded` and on `hashchange`: if `window.location.hash` matches an FAQ entry's id, set its `open` attribute and scroll it into view.

**Rationale**:
- Server-rendered HTML matches FR-002a (all collapsed by default) for the no-anchor case.
- The script is ~15 lines, defer-safe, has no dependencies, and degrades gracefully — without JS, an anchor still scrolls the visitor to the closed entry; the visitor can still click to open it.
- `hashchange` handling means an in-page link to another FAQ entry also opens the target.
- This pattern is well-established (used by GitHub Markdown, MDN, and many docs sites).

**Implementation sketch** (will live inside `rn-faq.html`):

```html
<script>
(function () {
  function openFromHash() {
    var hash = window.location.hash;
    if (!hash || hash.length < 2) return;
    var el = document.getElementById(hash.substring(1));
    if (el && el.tagName === 'DETAILS') {
      el.open = true;
      el.scrollIntoView({ block: 'start' });
    }
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', openFromHash);
  } else {
    openFromHash();
  }
  window.addEventListener('hashchange', openFromHash);
})();
</script>
```

**Alternatives considered**:
- *Server-render the targeted entry with `open` based on a query param*: Hugo SSG cannot read the URL hash at build time, and using a query param instead of a hash is non-standard for in-page anchors. Rejected.
- *Open all entries when JS is disabled*: defeats the "compact by default" goal and violates FR-002a. Rejected.

---

## R4. Markdown-in-YAML answers

**Decision**: Author answers in YAML using a literal block scalar (`|`) and render with Hugo's `markdownify` function in the template.

**Example**:

```yaml
- question: How do I get started with ReproNim?
  answer: |
    See the [Getting Started](/resources/getting-started/) page for an overview,
    or jump straight to the [tools page](/resources/tools/) to find a specific tool.
```

**Rationale**:
- Block scalars preserve newlines and let authors write multi-paragraph answers naturally.
- `markdownify` is the standard Hugo function for inline Markdown rendering and supports the same Goldmark configuration as the rest of the site (including `markup.goldmark.renderer.unsafe = true` from `hugo.yaml`, which allows raw HTML if a maintainer ever needs it).
- Keeps the editing experience identical to other Markdown content on the site.

**Alternatives considered**:
- *Plain-string answers (no Markdown)*: would block links and formatting. Violates FR-004. Rejected.
- *Separate Markdown files referenced from YAML*: doubles file count per entry for marginal benefit. Rejected.

---

## R5. Anchor (id) generation

**Decision**: Default the `<details>` `id` to `faq-{{ .question | urlize }}`. If the YAML entry provides an explicit `id:` field, use that verbatim (still namespaced under the FAQ section by convention).

**Rationale**:
- `urlize` produces a slug compatible with the existing Hextra heading-anchor convention.
- The `faq-` prefix avoids id collisions with any heading anchor on the home page.
- The explicit override lets maintainers preserve a stable link if a question's wording is updated. This is the same trade-off Wikipedia uses for section-anchor stability.

**Alternatives considered**:
- *Numeric ids based on list index* (`faq-1`, `faq-2`, …): unstable across reorderings. Rejected.
- *Hash of question text*: opaque to humans; a reworded question silently breaks links anyway. Rejected.

---

## R6. Search indexing

**Decision**: Take no special action — Hextra's built-in search (Pagefind/FlexSearch via the theme) already indexes home-page content, so the rendered FAQ is included automatically. Verify in the quickstart.

**Rationale**:
- Satisfies FR-013 with zero additional configuration. The shortcode renders normal HTML (not in a Web Component, not behind JS) so the indexer reads it like any other content.

**Alternatives considered**:
- *Add explicit search metadata*: not needed; would be redundant. Rejected.

---

## R7. Empty-state behavior

**Decision**: The shortcode checks `len site.Data.faq.entries`. If there are zero entries, the shortcode emits **no output at all** (not even an empty `<section>` or heading). If there are entries, it emits the full section.

**Rationale**:
- Satisfies FR-012 directly: an empty FAQ produces no visible artifact, no broken layout, no orphan heading.
- Lets the home page exist without a `data/faq.yaml` file at all (the shortcode also defends against the entire data key being absent).

**Alternatives considered**:
- *Render heading + "Coming soon" placeholder*: worse UX than just not showing the section. Rejected.

---

## R8. Performance impact

**Decision**: No additional fetch, no new font, no new image. The shortcode contributes a small inline `<style>` block (similar in size to `rn-buttons.html`) and a ~15-line inline `<script>`. The data file is consumed at build time.

**Rationale**:
- No network requests are added beyond the home-page HTML itself, so SC-007 (LCP within 10% of pre-launch) is met by construction.
- Inline assets defeat HTTP caching but are tiny (under ~2 KB combined uncompressed) and avoid extra round trips. This matches the precedent set by other `rn-*` shortcodes.

**Alternatives considered**:
- *Move CSS/JS to `static/` files for caching*: would be the right call at much larger sizes; for ~2 KB total, the inline form is faster overall and keeps the shortcode self-contained. Reject for v1; revisit if the FAQ grows substantially.

---

## Open items

None. All resolutions are deterministic and ready for Phase 1.
