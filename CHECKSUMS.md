# Checksums

This repository includes `checksums.sha256` for verifying the dataset files downloaded into `data/scilibrumodal-v1-data/`.

The dataset is hosted at:
https://scilibrumodal-v1.object.pscloud.io/

## Verify

Linux:

```bash
(cd ./data/scilibrumodal-v1-data && sha256sum -c ../../checksums.sha256)
```

macOS:

```bash
(cd ./data/scilibrumodal-v1-data && shasum -a 256 -c ../../checksums.sha256)
```


