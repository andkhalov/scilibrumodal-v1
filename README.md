# SciLibRuModal (v1)

This repository provides documentation, schema, and a lightweight Python loader for the **SciLibRuModal (v1)**.

The dataset itself is **not stored in this GitHub repository**. It is hosted in public S3-compatible object storage to support large-scale distribution.

This dataset is based on the HERALD translator research: https://github.com/frenzymath/herald_translator

## Dataset summary

- **Name:** SciLibRuModal (v1)
- **Rows:** 417,729
- **Format:** Hugging Face `datasets` saved-to-disk directory (export)
- **Storage endpoint:** https://scilibrumodal-v1.object.pscloud.io/
- **Local folder name (recommended):** `data/scilibrumodal-v1-data`

### Features / columns

The dataset contains the following columns:

- `informal_statement_en` — informal statement in English
- `formal_statement` — formal statement (Lean / formal language text)
- `informal_statement_ru` — informal statement in Russian
- `formula_md` — formula in Markdown/LaTeX form (text)
- `formula_md_illustration` — Optional formula markup (fallback option)
- `keywords_en` — keywords in English
- `keywords_ru` — keywords in Russian

See [DATA_FORMAT.md](DATA_FORMAT.md) for details.

## Quickstart

### 1) Download the dataset

See [DOWNLOAD.md](DOWNLOAD.md).

### 2) Load in Python

```python
from loader.load_scilibrumodal import load_scilibrumodal_v1

ds = load_scilibrumodal_v1("./data/scilibrumodal-v1-data")
print(ds)
print(ds["train"][0])
```

## Citation

If you use the dataset, please cite it as described in [CITATION.cff](CITATION.cff).

## Licence

This dataset is released under **CC-BY-4.0**. See `LICENSE.md`.