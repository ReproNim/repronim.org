---

description: "Task list for feature 001-faq-section"
---

# Tasks: Frequently Asked Questions Section on Home Page

**Input**: Design documents from `/specs/001-faq-section/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/faq-shortcode.md, quickstart.md

**Tests**: Automated tests are NOT requested by the spec. This is a Hugo static site with no test framework; verification is manual (`hugo server`) plus accessibility tooling (Lighthouse, axe DevTools, keyboard test). Verification tasks are explicit in the Polish phase.

**Organization**: Tasks are grouped by user story (US1, US2, US3 from spec.md) so each story can be implemented and validated as an independent increment.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependency on incomplete tasks).
- **[Story]**: User story this task belongs to (US1 = P1 visitor view, US2 = P2 maintainer editing, US3 = P3 deep-linking).
- File paths are absolute or repo-rooted as appropriate.

## Path Conventions

This is a Hugo + Hextra static site. The relevant paths are:

- `content/_index.md` — home page content
- `data/faq.yaml` — FAQ data (new file)
- `layouts/shortcodes/rn-faq.html` — FAQ shortcode (new file)
- `CONTRIBUTING.md` — existing contributor guide (will be linked, not rewritten)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Confirm the local Hugo + Hextra environment is ready. No code changes here.

- [X] T001 Verify the Hugo dev environment runs cleanly: from the repo root run `hugo server -D` and confirm the home page loads at `http://localhost:1313/` with no template errors and no missing-module warnings. If `hugo` is not installed, install Hugo extended ≥ 0.132.2 (matching `netlify.toml`) before continuing.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Create the empty file scaffolding that every user story builds on. Both files must exist before US1 work begins.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [X] T002 [P] Create the data file `data/faq.yaml` with a top-level `entries:` key holding **one placeholder item** (`question:` + `answer:` using the `|` block scalar) so the shortcode has something to read during initial wiring. The real content replaces this placeholder in T008.
- [X] T003 [P] Create the shortcode skeleton `layouts/shortcodes/rn-faq.html` with the empty-state guard only: an outer Go-template `{{ with site.Data.faq }}{{ with .entries }}` … `{{ end }}{{ end }}` block that emits nothing when `data/faq.yaml` is missing or `entries` is empty. Confirm by temporarily removing the placeholder and verifying no output is rendered, then restore it.

**Checkpoint**: Foundation ready — User Story 1 can begin.

---

## Phase 3: User Story 1 — Visitor finds answers on the home page (Priority: P1) 🎯 MVP

**Goal**: A first-time visitor lands on the home page, sees a clearly titled FAQ section below the existing intro and section buttons, can expand any question to read its answer, and can collapse it again. Multiple entries can be open at once. Section honors light/dark theme and meets WCAG 2.1 AA contrast.

**Independent Test**: Run `hugo server`, open `/`, scroll past the legacy banner / intro / `rn-buttons` block, see "Frequently Asked Questions" with 5–8 entries, click any question to expand, click again to collapse, click two questions to confirm both stay open. Toggle the site theme; verify the section reads correctly in both light and dark.

### Implementation for User Story 1

- [X] T004 [US1] In `layouts/shortcodes/rn-faq.html`, add the section wrapper: `<section class="rn-faq" aria-labelledby="rn-faq-heading">` with an `<h2 id="rn-faq-heading">Frequently Asked Questions</h2>`. Place it inside the empty-state guard from T003 so it only renders when entries exist. Reference `contracts/faq-shortcode.md` for the exact element/attribute names.
- [X] T005 [US1] In `layouts/shortcodes/rn-faq.html`, implement the entry rendering loop: `{{ range .entries }}` … `{{ end }}` emitting one `<details class="rn-faq-item" id="…">` per entry with `<summary>{{ .question }}</summary>` and `<div class="rn-faq-answer">{{ .answer | markdownify }}</div>`. Do **not** set the `open` attribute (FR-002a). Order = YAML order (FR-006).
- [X] T006 [US1] In `layouts/shortcodes/rn-faq.html`, implement anchor id generation: if `.id` is set on the entry use it verbatim; otherwise compute `printf "faq-%s" (urlize .question)`. Use the result as the `<details id="…">` value (per `data-model.md` and contract C2/C4).
- [X] T007 [US1] In `layouts/shortcodes/rn-faq.html`, append a scoped `<style>` block at the end of the section (mirroring the precedent set by `layouts/shortcodes/rn-buttons.html`). Style only `.rn-faq`, `.rn-faq-item`, `.rn-faq-item > summary`, and `.rn-faq-answer`. Required: vertical spacing ≥ 0.75rem between entries; visible focus ring on `<summary>` (`:focus-visible { outline: 2px solid currentColor; outline-offset: 2px; }`); cursor: pointer on `<summary>`; inherit color/background from the theme so light/dark both work (FR-009); do not override link colors inside `.rn-faq-answer`.
- [X] T008 [US1] In `content/_index.md`, append `{{< rn-faq >}}` on its own line **after** the closing `{{< /rn-buttons >}}` so the FAQ section sits below the existing intro and section buttons, not above them.
- [X] T009 [US1] In `data/faq.yaml`, replace the T002 placeholder with the launch starter set: 5–8 entries covering (per FR-014) "what ReproNim is", "who it is for", "how to get started", "where to find tools", "how to participate", "where to get help / office hours", and "how to apply to the fellowship." Use the YAML literal block scalar (`|`) for each `answer:`. Where natural, link to the relevant existing page (`/about/`, `/resources/getting-started/`, `/resources/tools/`, `/participate/`, `/help/`, `/fellowship/`). Reference `data-model.md` for the exact schema and `quickstart.md` for the editing pattern.
- [ ] T010 [US1] Verify US1 acceptance: from `hugo server`, load `/`, confirm the FAQ section renders below `rn-buttons` with 5–8 collapsed entries; expand one, expand a second (confirm both stay open per FR-003); collapse one; toggle the theme switcher and confirm both light and dark mode render with readable contrast.

**Checkpoint**: User Story 1 fully delivers the MVP. The home page now has a working FAQ that is visible to visitors. Could be shipped as-is.

---

## Phase 4: User Story 2 — Maintainer adds, edits, and removes entries (Priority: P2)

**Goal**: A maintainer can manage the FAQ via the existing GitHub edit workflow without touching layout code. The shortcode degrades gracefully on malformed entries and surfaces problems in the Hugo build log.

**Independent Test**: Have a maintainer (or simulate one) (a) add a new entry to `data/faq.yaml`, rebuild, confirm it appears in YAML order; (b) edit an existing entry's `answer`, rebuild, confirm only that answer changed; (c) delete an entry, rebuild, confirm it's gone and no broken anchor remains; (d) introduce a malformed entry (empty `question`), rebuild, confirm a Hugo `warnf` appears and the rest of the FAQ still renders.

### Implementation for User Story 2

- [X] T011 [US2] In `layouts/shortcodes/rn-faq.html`, add input validation inside the entry loop: skip entries where `.question` or `.answer` is empty/unset, and emit a Hugo build warning via `warnf` describing the skip. Reference `data-model.md` validation rules 1 and 2.
- [X] T012 [US2] In `layouts/shortcodes/rn-faq.html`, add duplicate-id detection: track ids seen in the current page (use a `dict`/`slice` accumulator), and on a duplicate append `-2`, `-3`, … as a suffix while emitting a `warnf`. Reference `data-model.md` validation rule 3.
- [X] T013 [US2] In `layouts/shortcodes/rn-faq.html`, validate the `id` field format when explicitly provided: if it does not match `^[a-z0-9][a-z0-9-]*$`, fall back to the auto-generated slug and emit a `warnf`. Reference `data-model.md` validation rule 4.
- [X] T014 [US2] In `data/faq.yaml`, add a header comment block (lines starting with `#`) at the top of the file documenting the schema (`question`, `answer`, optional `id`), the literal block scalar usage, and a one-line link to the maintainer guide at `specs/001-faq-section/quickstart.md`. Goal: a maintainer opening the file in GitHub sees how to add an entry without leaving the file.
- [X] T015 [US2] In `CONTRIBUTING.md`, add a short section titled "Editing the home page FAQ" with a 2–3 sentence pointer to `data/faq.yaml` and a link to `specs/001-faq-section/quickstart.md`. Place it after any existing "How to edit pages" section, or at the end if no comparable section exists. Do not duplicate the full quickstart — link to it.
- [ ] T016 [US2] Verify US2 acceptance: temporarily add an entry, edit one, delete one, and introduce a malformed entry in `data/faq.yaml`. For each step run `hugo server` (or watch the running server reload), confirm the rendered page reflects the change and the build log behaves per T011/T012/T013. Restore the file before moving on.

**Checkpoint**: User Stories 1 AND 2 both work independently. Maintainers can keep the FAQ current without engineering involvement.

---

## Phase 5: User Story 3 — Visitor deep-links to a specific question (Priority: P3)

**Goal**: A URL of the form `https://repronim.org/#<faq-anchor>` opens the home page with the targeted FAQ entry already expanded and scrolled into view. Invalid anchors degrade gracefully (page renders normally per FR-011).

**Independent Test**: With the dev server running, open `http://localhost:1313/#faq-how-do-i-get-started` (or whichever anchor maps to a real entry); confirm the matching `<details>` is `open` and visible. Then open `http://localhost:1313/#faq-does-not-exist`; confirm the page renders with all entries collapsed and no JS errors in the console.

### Implementation for User Story 3

- [X] T017 [US3] In `layouts/shortcodes/rn-faq.html`, append a scoped inline `<script>` at the end of the section. Wrap in an IIFE; define an `openFromHash` function that reads `window.location.hash`, looks up the matching `<details>` by id, sets `el.open = true`, and calls `el.scrollIntoView({ block: 'start' })`. Bind the function to `DOMContentLoaded` (or run immediately if the document is already past `loading`) and to `hashchange`. Reference the implementation sketch in `research.md` § R3.
- [ ] T018 [US3] Verify US3 acceptance: with `hugo server` running, (a) load `/#<existing-anchor>`, confirm the targeted entry opens and scrolls into view; (b) load `/#faq-does-not-exist`, confirm the page renders with no console error and all entries collapsed; (c) while on `/`, manually change the URL hash in the address bar to a different valid anchor and press Enter, confirm `hashchange` triggers expansion of the new target.

**Checkpoint**: All three user stories are complete. Feature is fully functional.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Verification against the success criteria in spec.md (SC-001 … SC-008), plus accessibility, performance, and final pre-PR checks.

- [ ] T019 [P] Run Lighthouse on `/` (Chrome DevTools → Lighthouse → Accessibility, mobile + desktop). Confirm the Accessibility score is ≥ 95 and that no findings reference elements under `.rn-faq`. (Verifies SC-005 and supports SC-004.)
- [ ] T020 [P] Run axe DevTools (browser extension) on `/`. Confirm zero violations. Pay particular attention to color-contrast rules under `.rn-faq` and `.rn-faq-answer` in both light and dark themes. (Verifies SC-005.)
- [ ] T021 [P] Keyboard-only test on `/`: Tab through the page; confirm each `<summary>` receives focus with a visible outline; press Enter on a focused `<summary>` and confirm the entry expands; press Space and confirm it collapses; Tab again and confirm focus moves into the answer's first link (when present). (Verifies SC-004.)
- [ ] T022 [P] Theme contrast check: toggle the site theme between light and dark via the theme switch in the navbar; on each, verify the FAQ heading, question text, and answer text meet WCAG AA contrast ratios (≥ 4.5:1 for body text). Use the browser's color-picker if needed. (Verifies SC-005 and FR-009.)
- [ ] T023 [P] Performance check: capture a baseline LCP for `/` against `main` (no FAQ) using Chrome DevTools Performance panel or the Web Vitals extension; capture LCP on the feature branch; confirm the new value is within 10% of baseline. (Verifies SC-007.)
- [ ] T024 [P] Search indexing check: trigger the site's search (the navbar search button) and search for a phrase that appears only inside an FAQ answer; confirm the home page is returned in results. If Hextra search needs an index rebuild step, run it. (Verifies FR-013.)
- [ ] T025 Run the maintainer flow end-to-end against `specs/001-faq-section/quickstart.md`: follow each step in the "add a new FAQ entry" section, including verifying the deep-link URL afterward. Time the experience and confirm it stays under 10 minutes (SC-003). Restore the file when done.
- [ ] T026 Confirm zero-entry behavior (FR-012): in a scratch branch (or via temporary edit), set `entries: []` in `data/faq.yaml` and reload `/`. Confirm no `<section class="rn-faq">` appears in the rendered HTML and the home page renders cleanly. Restore the file.
- [ ] T027 Open a pull request to `main` titled `feat: add Frequently Asked Questions section to home page`. PR body: link to `specs/001-faq-section/spec.md`, summarize the three user stories, and call out the verification done in T019–T026. Do NOT include `[skip netlify]` — the Netlify preview deploy is the final visual check.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies. Start immediately.
- **Phase 2 (Foundational)**: Depends on Phase 1. Blocks all user stories.
- **Phase 3 (US1)**: Depends on Phase 2. Delivers the MVP.
- **Phase 4 (US2)**: Depends on Phase 2; can layer on top of US1 work or run in parallel after T005 lands (the validation logic in T011–T013 modifies the same `rn-faq.html` file as US1, so practical ordering is US1 → US2).
- **Phase 5 (US3)**: Depends on Phase 2; the deep-link script is appended to the same shortcode, so practical ordering is US1 → US3 (US2 and US3 can swap order or interleave).
- **Phase 6 (Polish)**: Depends on Phases 3–5 being complete (or on whichever user stories you elected to ship).

### User Story Dependencies

- **US1**: No dependency on other stories. Ships alone as a complete MVP.
- **US2**: No functional dependency on US1, but practical: validation/comments are easier to add once the rendering loop exists. Can be deferred (a maintainer can already edit `data/faq.yaml` after US1).
- **US3**: No functional dependency on US1, but the deep-link script targets ids that US1 produces. Could ship without US3; deep-links would still scroll-to-anchor (browser default) but not auto-expand.

### Within a User Story

- Tasks that touch the same file (`layouts/shortcodes/rn-faq.html` is the main one) must run sequentially within a story. The task ordering above respects this.
- Verification tasks (T010, T016, T018) come last within their story.

### Parallel Opportunities

- **Phase 2**: T002 (data file) and T003 (shortcode skeleton) touch different files → both `[P]`.
- **Phase 6**: T019–T024 are all read-only verification activities against the running site → all `[P]`.
- Inside US1: T004–T007 all edit `rn-faq.html`, so they are sequential. T008 (`_index.md`) and T009 (`faq.yaml`) touch different files; either order works once T004–T007 are done.
- Across stories with multiple developers: once Phase 2 lands, US1 has to ship before US2 and US3 add their layers to `rn-faq.html`. With a single developer, the linear order in this document is the recommended path.

---

## Parallel Example: Phase 2

```bash
# Both files can be created concurrently:
Task: "Create data/faq.yaml with placeholder entry"               # T002 [P]
Task: "Create layouts/shortcodes/rn-faq.html empty-state skeleton" # T003 [P]
```

## Parallel Example: Phase 6 verifications

```bash
# All read-only checks can run concurrently against `hugo server`:
Task: "Lighthouse accessibility audit on /"                  # T019 [P]
Task: "axe DevTools scan on /"                               # T020 [P]
Task: "Keyboard-only navigation test on /"                   # T021 [P]
Task: "Theme contrast check (light + dark)"                  # T022 [P]
Task: "LCP comparison vs. baseline"                          # T023 [P]
Task: "Search indexing check"                                # T024 [P]
```

---

## Implementation Strategy

### MVP First (User Story 1 only)

1. Phase 1 (T001).
2. Phase 2 (T002, T003).
3. Phase 3 (T004 → T010).
4. **STOP and validate**: open `/`, exercise all acceptance scenarios in spec.md US1.
5. Optionally ship the MVP — the FAQ is fully usable for visitors.

### Incremental Delivery

1. MVP per above.
2. Add US2 (T011 → T016) → run the maintainer flow (T025-style mini-check) → ship.
3. Add US3 (T017 → T018) → verify deep-linking → ship.
4. Polish (T019 → T027) → open PR.

### Single-Developer Recommended Path

1. T001.
2. T002, T003 in parallel.
3. T004 → T010 sequentially.
4. T011 → T016 sequentially.
5. T017 → T018 sequentially.
6. T019 → T024 in parallel.
7. T025, T026, T027 sequentially.

---

## Notes

- This is a Hugo static site; "tasks" map to template/data edits and verification, not to traditional source code. There is no test framework to add.
- All shortcode logic lives in **one file** (`layouts/shortcodes/rn-faq.html`) by design (matches `rn-buttons.html` precedent). Keep it that way unless the file grows past ~150 lines.
- Commit after each task or each logical group. Use conventional commits (`feat:`, `docs:`, `chore:`).
- Stop at any checkpoint to demo or ship — every user story is independently shippable.
- Avoid: adding a JS framework, adding a CSS file, modifying `hugo.yaml` navigation, modifying the Hextra theme module.
