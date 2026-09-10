# Mintlify migration report

This folder is a first-pass conversion of the GitBook export to Mintlify.

## Conversion

- GitBook Markdown pages converted to `.mdx` so Mintlify callout components can be used.
- `.gitbook/assets` copied to `assets/` with URL-safe filenames.
- GitBook `hint` blocks converted to Mintlify callouts (`Info`, `Warning`, etc.).
- GitBook `code` wrappers removed while preserving fenced code blocks.
- GitBook `content-ref` blocks converted to normal internal links.
- GitBook `file` reference converted to a direct asset download link.
- GitBook figures converted to Markdown images.
- `SUMMARY.md` retained as `SUMMARY.gitbook.md`; `docs.json` is now the navigation source.

## Items requiring manual review

- Two GitBook `/broken/files/...` image references had no matching asset in the export and were replaced with an explicit screenshot-unavailable note.
- One GitBook `/broken/spaces/...` link had no exported target; it was mapped to the local Custom AI Algorithms technical requirements page as the closest available guidance.
- The GitBook export contains duplicate `Appendix 2` titles; the content should be reviewed before final publication.
- Some original HTML (tables, `<br>`, etc.) is intentionally preserved because it is valid in MDX and avoids changing content semantics.
- Navigation is intentionally conservative: top-level GitBook sections are Mintlify groups, while nested pages are flattened within each group. This is a safe first deployment; the sidebar can be refined later in the Mintlify editor.

## Counts

- Source Markdown pages: 85
- Assets copied: 56
- Navigation groups: 17
- Source pages containing broken GitBook references: 3

