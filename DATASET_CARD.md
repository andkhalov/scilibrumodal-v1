# SciLibRuModal (v1) — Dataset Card

## Motivation

The SciLibRuModal (v1) is designed for research on multilingual and formal/informal alignment in mathematical knowledge representation. It supports tasks such as cross-lingual retrieval (RU/EN), informal-to-formal mapping, and formula-conditioned retrieval.

## Composition

- **Size:** 417,729 rows
- **Unit of data:** a statement-level sample containing informal (RU/EN), formal representation, formula markup, and keywords.
- **Splits:** train (v1)

## Columns

- `informal_statement_en`: Natural language statement in English.
- `informal_statement_ru`: Natural language statement in Russian.
- `formal_statement`: Formal statement text (formal language / proof assistant representation).
- `formula_md`: Formula markup (Markdown/LaTeX text).
- `formula_md_illustration`: Optional formula markup (fallback option).
- `keywords_en`, `keywords_ru`: Keywords aligned with the statements.

## Collection process

The dataset was constructed from structured metadata and statement-level sources. The initial release (v1) focuses on text modalities; image rendering of formulas was performed on-the-fly in downstream training and is not included as files in the dataset export.

Upstream research/codebase used during preparation:
https://github.com/frenzymath/herald_translator

## Intended use

- Multimodal / multilingual retrieval baselines
- Formalization assistance (informal → formal)
- Keyword and formula-conditioned indexing

## Limitations

- No pre-rendered formula images in v1.
- Some fields may be missing/empty depending on upstream metadata coverage.

## Hosting

The dataset files are hosted in S3-compatible object storage:
https://scilibrumodal-v1.object.pscloud.io/
