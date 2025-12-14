from __future__ import annotations
from typing import Optional, List, Any
from datasets import load_from_disk, DatasetDict

def _normalize_keywords(x: Any) -> List[str]:
    if x is None:
        return []
    if isinstance(x, list):
        return [str(i).strip() for i in x if str(i).strip()]
    # string case: split on common delimiters
    s = str(x).strip()
    if not s:
        return []
    # heuristic delimiters
    for delim in [";", ",", "|"]:
        if delim in s:
            return [p.strip() for p in s.split(delim) if p.strip()]
    return [s]

def load_scilibrumodal_v1(
    path: str,
    normalize: bool = True,
) -> DatasetDict:
    """
    Load SciLibRuModal (v1) from a local HF datasets save_to_disk directory.

    Args:
        path: Local path, e.g. ./data/scilibrumodal-v1
        normalize: If True, normalizes keywords_* into lists of strings.

    Returns:
        datasets.DatasetDict
    """
    ds = load_from_disk(path)

    # ds may be Dataset or DatasetDict depending on how it was saved
    if hasattr(ds, "keys") and "train" in ds:
        dsd = ds
    else:
        dsd = DatasetDict({"train": ds})

    if normalize:
        def _map(row):
            row["keywords_en"] = _normalize_keywords(row.get("keywords_en"))
            row["keywords_ru"] = _normalize_keywords(row.get("keywords_ru"))
            return row

        dsd = dsd.map(_map, desc="Normalizing keywords", num_proc=1)

    return dsd
