# Implementation Plan: Frequently Asked Questions Section on Home Page

**Branch**: `001-faq-section` | **Date**: 2026-04-28 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-faq-section/spec.md`

## Summary

Add a Frequently Asked Questions section to the ReproNim home page (`content/_index.md`), rendered by a new Hugo shortcode that reads from a single maintainer-editable data file (`data/faq.yaml`). Each entry is a question/answer pair; answers support Markdown so links, lists, and emphasis render correctly. Entries default to collapsed, support multiple open at once, expose stable URL anchors for deep-linking, and meet WCAG 2.1 AA in both light and dark themes.

The implementation leans on the **HTML5 `<details>`/`<summary>` element** for the accordion behavior so semantics, keyboard interaction, and screen-reader announcement are correct by default with zero JavaScript. A small inline progressive-enhancement script handles only the deep-linking case (open the targeted `<details>` and scroll to it on page load and on `hashchange`).

## Technical Context

**Language/Version**: Hugo 0.132.2 (extended), Hextra theme v0.8.3 (Go module)
**Primary Dependencies**: Hugo Go templates, Hextra theme; no new runtime dependencies, no JS framework, no build tooling beyond Hugo itself
**Storage**: Static; FAQ entries stored in `data/faq.yaml` (committed to the repo)
**Testing**: Manual verification via `hugo server` + an automated accessibility check (axe DevTools or Lighthouse) on the home page; no test framework added
**Target Platform**: Static site served via Netlify; supported browsers per the existing site (last two major versions of Chrome, Firefox, Safari, Edge)
**Project Type**: Static documentation/content site (Hugo + Hextra)
**Performance Goals**: Home page LCP must stay within 10% of pre-launch value (per SC-007); no additional render-blocking assets
**Constraints**: Must work without JavaScript for read-only viewing (NoJS users still see all answers when they click `<details>`); only deep-linking degrades to "anchor scrolls but entry stays closed" without JS; must honor the existing light/dark theme toggle; no changes to the top navigation
**Scale/Scope**: Single page surface; 5–8 entries at launch (per FR-014), expected to grow to ≤30 over the foreseeable life of the section

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

The repository's `.specify/memory/constitution.md` is the unfilled template — no project-specific principles have been ratified, so there are no formal gates to evaluate. Applying the workspace-level standards from `/Users/yibeichen/Documents/GitHub/CLAUDE.md` and the existing site conventions instead:

| Standard | Status | Notes |
|----------|--------|-------|
| Use existing tech stack (Hugo + Hextra) | Pass | No new framework, no JS bundle, no build step changes |
| Markdown-first content authoring | Pass | Answers authored as Markdown in YAML; rendered with `markdownify` |
| Accessibility (WCAG 2.1 AA) | Pass by design | Native `<details>`/`<summary>` carries semantics; theme contrast already AA |
| No console/debug noise in commits | Pass | Inline JS is ~15 lines, scoped, no logging |
| Conventional commits | Pass | Implementation will use `feat: …` |
| `[skip netlify]` flag awareness | N/A | Used only for non-deploy commits |

**Result**: No violations. No `Complexity Tracking` entries needed. Re-checked after Phase 1 design — still no violations.

## Project Structure

### Documentation (this feature)

```text
specs/001-faq-section/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output (how a maintainer adds an entry)
├── contracts/
│   └── faq-shortcode.md # Phase 1 output (input data schema + output HTML contract)
├── checklists/
│   └── requirements.md  # Spec quality checklist (already created)
└── tasks.md             # Phase 2 output (created later by /speckit-tasks)
```

### Source Code (repository root)

This is a Hugo static site, not a traditional code project. The feature lands in the existing site layout:

```text
repronim.org/
├── content/
│   └── _index.md                       # Home page — add {{< rn-faq >}} shortcode call
├── data/
│   └── faq.yaml                        # NEW — maintainer-edited FAQ entries
├── layouts/
│   └── shortcodes/
│       └── rn-faq.html                 # NEW — renders the FAQ section from data/faq.yaml
├── static/                             # (unchanged) inline JS lives in the shortcode
└── hugo.yaml                           # (unchanged) — no menu/config changes; stays on Home tab
```

**Structure Decision**: Add **one** new shortcode (`layouts/shortcodes/rn-faq.html`) and **one** new data file (`data/faq.yaml`). Modify **one** existing file (`content/_index.md`) to invoke the shortcode below the existing intro and `rn-buttons` block. No CSS file is added; styles are scoped inside the shortcode (matching the precedent set by `rn-buttons.html`, which inlines its `<style>`). No changes to `hugo.yaml`, navigation, or the theme module.

This is the minimum surface area that satisfies all functional requirements and matches the existing per-feature convention used by `rn-button` / `rn-buttons` / `wordpress-posts` / `people` / `fellows-resources`.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No constitution violations. Section intentionally left empty.
