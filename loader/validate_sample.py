import argparse
from datasets import load_from_disk

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", required=True)
    args = ap.parse_args()

    ds = load_from_disk(args.path)
    if hasattr(ds, "keys") and "train" in ds:
        d = ds["train"]
    else:
        d = ds

    print(ds)
    print("num_rows:", d.num_rows)
    print("features:", list(d.features.keys()))
    print("sample[0]:", d[0])

if __name__ == "__main__":
    main()
