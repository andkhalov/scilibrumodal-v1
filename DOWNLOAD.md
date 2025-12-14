# Download instructions

The dataset is hosted in public S3-compatible object storage:

https://scilibrumodal-v1.object.pscloud.io/

The recommended download method is **rclone**.

## Option A — rclone (recommended)

### Install rclone
- macOS (Homebrew): `brew install rclone`
- Linux: follow `rclone.org/install`

### Download (sync) the dataset folder

```bash
mkdir -p data

rclone sync \
  :http: --http-url https://scilibrumodal-v1.object.pscloud.io \
  ./data/scilibrumodal-v1-data \
  --progress
```

This mirrors the remote dataset directory locally.

## Option B — direct HTTP download (advanced)

If you need a single file download workflow, you can fetch individual files via `curl/wget`.
However, because the dataset is a directory export (multiple files), rclone is strongly preferred.

### Verify the download (optional but recommended)

Verify with the checksums shipped in this repository:

```bash
# Linux (coreutils):
(cd ./data/scilibrumodal-v1-data && sha256sum -c ../../checksums.sha256)

# macOS:
(cd ./data/scilibrumodal-v1-data && shasum -a 256 -c ../../checksums.sha256)
```

Alternatively, use the validation script:

```bash
python loader/validate_sample.py --path ./data/scilibrumodal-v1-data
```