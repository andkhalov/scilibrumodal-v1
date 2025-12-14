import json
from pathlib import Path
from datasets import load_from_disk

def main():
    path = Path("data/scilibrumodal-v1-data")
    ds = load_from_disk(str(path))
    if hasattr(ds, "keys") and "train" in ds:
        train = ds["train"]
    else:
        train = ds

    manifest = {
        "name": "SciLibRuModal (v1)",
        "version": "1.0.0",
        "rows": int(train.num_rows),
        "features": list(train.features.keys()),
        "storage": {
            "type": "s3_public",
            "endpoint": "https://scilibrumodal-v1.object.pscloud.io/",
            "path": ""
        },
        "notes": [
            "v1 is text-only; formula images are not included as files."
        ]
    }

    Path("manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print("Wrote manifest.json")

if __name__ == "__main__":
    main()
