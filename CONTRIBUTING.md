# Contributing to ReproNim.org

Thank you for your interest in contributing to the `repronim.org` project!

This guide outlines how to contribute to ReproNim.org using GitHub’s web interface. The website is built with Hugo and deployed with Netlify whenever changes are merged.

1. Changes are made via [GitHub Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests).
2. Once merged, your changes are automatically deployed to the live site via Netlify.

## Contributing Without the Command Line

One option to make changes uses only the GitHub web interface—no command line required.

### 1. Make Changes

You can edit files directly in the GitHub UI:

1. Navigate to the file you want to edit.
2. Click the pencil (✏️) icon in the top right of the file view.
3. Make your changes in the text editor.
4. Scroll down to the **Commit changes** section.
   - Add a short, descriptive commit message (e.g., "Fix typo in about page").
   - Select **Create a new branch** and give it a meaningful name (e.g., `fix-typo-about`).
   - Click **Propose changes**.

### 2. Create a Pull Request (PR)

Once you've made changes, you need to request that they be merged into the main project:

1. After proposing changes, you'll be taken to a new page.
2. Click **Create pull request**.
3. Add a title and description for your PR, explaining what you've changed.
4. Click **Create pull request** again.

### 3. Wait for Review

Project maintainers will review your changes and may request modifications.
Keep an eye on the Pull Requests tab for any comments or requested changes.
Netlify automatically creates a deploy preview for each pull request, allowing you to see how your changes will appear on the live site before they are merged.
A link to the preview will be available in the PR conversation, so you can verify everything looks as expected.
Every time you add commits to the Pull Request, Netlify will automatically update the preview, be sure to use the new link each time.


### 4. Merge or Close

Once approved, a maintainer will merge your PR. If your changes need revision, follow their instructions and update your PR.

## Editing the home page FAQ

The Frequently Asked Questions section on the home page is generated from a single data file: [`data/faq.yaml`](./data/faq.yaml). To add, edit, reorder, or remove a question, edit that file directly via the GitHub web UI (no template or layout changes are needed for ordinary content edits). The file's header comment documents the schema; for a longer walkthrough see [`specs/001-faq-section/quickstart.md`](./specs/001-faq-section/quickstart.md).

## Local Development

To set up a local development environment:

1. **Install Hugo**: Use the version specified in `netlify.toml`. See [Hugo installation guide](https://gohugo.io/getting-started/installing/).

2. **Install the Theme**: This site uses the Hextra theme. Run the following command to fetch the theme:

   ```sh
   hugo mod get -u
   ```

3. **Run the Site Locally**: Start a local development server with:

   ```sh
   hugo server
   ```

   This will serve the site at `http://localhost:1313/` where you can preview your changes.

## Additional Notes

- If you're unsure about a change, open an issue first to discuss it with maintainers.
- Be respectful and follow the project's [Code of Conduct](./code-of-conduct.md).
- If you're new to GitHub, check out [GitHub Docs](https://docs.github.com/en) for more tutorials.

Happy contributing! 🎉
