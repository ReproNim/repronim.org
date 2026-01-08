#!/usr/bin/env python3
"""
Generate publications.md from list of DOIs using duecredit/citeproc-py.

This script reads DOIs from data/publications.yaml and generates
formatted citations in APA style, writing to content/about/publications.md
"""

import sys
import yaml
from pathlib import Path
from duecredit.io import format_bibtex, import_doi, BibTeX


def fetch_citation(doi):
    """
    Fetch and format a single citation from a DOI.

    Args:
        doi: DOI string (e.g., "10.1038/s41597-025-05503-w")

    Returns:
        Formatted citation string in APA style, or None if fetch failed
    """
    try:
        # Add https://doi.org/ prefix if not present
        doi_url = doi if doi.startswith('http') else f'https://doi.org/{doi}'

        # Fetch citation data and format as APA
        bibtex_data = BibTeX(import_doi(doi_url))
        citation = format_bibtex(bibtex_data, style='apa', formatter='html')

        return citation
    except Exception as e:
        print(f"Warning: Failed to fetch DOI {doi}: {e}", file=sys.stderr)
        return None


def generate_publications_markdown(dois, output_path):
    """
    Generate the publications markdown file from a list of DOIs.

    Args:
        dois: List of DOI strings
        output_path: Path to write the generated markdown file
    """
    # Frontmatter for the markdown file
    frontmatter = """---
Title: ReproNim Publications
linkTitle: "Publications"
type: docs
weight: 60
---
"""

    citations = []
    failed_dois = []

    print(f"Fetching {len(dois)} publications...")

    for i, doi in enumerate(dois, 1):
        print(f"  [{i}/{len(dois)}] Fetching {doi}...", end=' ')
        citation = fetch_citation(doi)

        if citation:
            citations.append(citation)
            print("✓")
        else:
            failed_dois.append(doi)
            print("✗")

    # Write the markdown file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter)

        for i, citation in enumerate(citations, 1):
            f.write(f"{i}. {citation}\n\n")

    print(f"\nGenerated {len(citations)} citations to {output_path}")

    if failed_dois:
        print(f"\nWarning: {len(failed_dois)} DOIs failed to fetch:")
        for doi in failed_dois:
            print(f"  - {doi}")


def main():
    # Paths
    repo_root = Path(__file__).parent.parent
    doi_yaml = repo_root / 'data' / 'publications.yaml'
    output_md = repo_root / 'content' / 'about' / 'publications.md'

    # Load DOIs from YAML
    print(f"Loading DOIs from: {doi_yaml}")
    with open(doi_yaml, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        dois = data.get('publication-dois', [])

    if not dois:
        print("Error: No DOIs found in publications.yaml", file=sys.stderr)
        sys.exit(1)

    # Optional: limit number of DOIs for testing (use first argument)
    if len(sys.argv) > 1:
        limit = int(sys.argv[1])
        print(f"Testing mode: processing first {limit} DOIs only")
        dois = dois[:limit]

    # Generate publications
    generate_publications_markdown(dois, output_md)

    print("\nDone! To add new publications:")
    print(f"  1. Add DOI to {doi_yaml}")
    print(f"  2. Run: uv run python scripts/generate_publications.py")


if __name__ == '__main__':
    main()
