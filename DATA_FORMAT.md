# Data format and schema

## Storage format

The dataset is exported using Hugging Face `datasets` `save_to_disk()` format.
After download, it can be loaded with `datasets.load_from_disk()`.

## Splits

- `train` split is provided for v1.
(If additional splits are released, they will be described in `CHANGELOG.md`.)

## Schema (features)

The dataset has the following columns:

- `informal_statement_en` (string)
- `formal_statement` (string)
- `informal_statement_ru` (string)
- `formula_md` (string)
- `formula_md_illustration` (string)
- `keywords_en` (string or list of strings; see Notes below)
- `keywords_ru` (string or list of strings; see Notes below)

### Notes on keywords

Depending on the preprocessing pipeline version, keywords may be stored either as:
- a single delimited string, or
- a list of strings.

The loader normalizes both variants to Python lists when `normalize=True`.

## Known limitations (v1)

- v1 does not include pre-rendered formula images. LaTeX was rendered on-the-fly during training/processing.
- Some rows may contain empty keyword fields depending on source metadata availability.

## Recommended usage

- Semantic search / retrieval (informal ↔ formal)
- Multilingual retrieval (RU/EN)
- Formula-conditioned retrieval (via `formula_md`)