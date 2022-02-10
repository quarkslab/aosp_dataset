# Building a Commit-level Dataset of Real-world Vulnerabilities

This repository is the companion for the paper Building a Commit-level Dataset
of Real-world Vulnerabilities published in CODASPY 2022.


## Installation of the helpers

You can install the code of the helpers by cloning this repository and using `pip install .` (he trailing dot is important).


Note that the code targets `Python 3.10+` and has only been tested on `Debian`.

## Commit level vulnerabilities

This dataset contains 1900 vulnerabilities information at a fix commit level for
the Android Open Source Project. The information are available in directory
[`cves/`](cves/) using one file per vulnerability. The schema used is described
in this [file](schemas/AospCve.schema.json) and an helper Python class is
available [here](src/aospcve.py).

### Usage

```python
import json
import aosp_dataset

cve_2012_6701 = aosp_dataset.AospCve(
    json.load(open("cves/CVE-2012-6701.json"))
)
```

## Compiled dataset
For some vulnerabilities, the pre-compiled binaries are also available. The
links are found in the precompiled [directory](precompiled/links.json) and the
schema is available [here](schemas/precompiled.schema.json). An helping class is
also available [here](src/compiled.py)

The complete dataset is around ~120 Gb with about 700 precompiled CVEs.

### Compiled CVE Layout

For each tuple (CVE-ID, commit), the files are four directories, with two
subdirectories each. In the `vuln` one, binaries before the fix commit was
applied and in the `fix` one after the fixing commit.

Each binary is prefixed by its hash to prevent names collision. Some directories may be empty if the build was incomplete.


### Usage of the helper class

```python
import json
import aosp_dataset

precompiled_dataset = aosp_dataset.PrecompiledDataset(
    json.load(open("precompiled/links.json"))
)
```

### Compilation information

Every CVE was compiled with the default build options of AOSP.


### Example
```console
$ tree 017838585617f0e492ede866750fcfb8ed77830b
017838585617f0e492ede866750fcfb8ed77830b
├── arm
│   ├── fix
│   │   ├── 4d7eb89a9529df46d1ae0b1039594705c4a4b6725e09268d97ae85dc467b15c0_libnfc_nci_jni.so
│   │   ├── afe25ad8735bf7e78ba45d39387dd4316c20f885c2883732a1c8894b0a2f85dc_libnfc_nci_jni.so
│   │   └── files.json
│   └── vuln
│       ├── 92aaa2a42659571150c4331ac22b89d5390ea1bf3956e37f7d8fec5a9d740908_libnfc_nci_jni.so
│       ├── d15122acd2474f7a24674a5ea732276396a31c402852f493f1a0d7558853f840_libnfc_nci_jni.so
│       └── files.json
├── arm64
│   ├── fix
│   │   ├── 2980aa7fc0735dd0cc6ba946ba3632e787d3eae557cc4f86375323fd55869636_libnfc_nci_jni.so
│   │   ├── f921f272f78c3e99a6196d4e99eff2a1abfc2aff00a315bde681ca1fb22ff859_libnfc_nci_jni.so
│   │   └── files.json
│   └── vuln
│       ├── 63143671c7616c85ad1215f53e60c4da978f9c78b09e7cca6f347edab39ce7ff_libnfc_nci_jni.so
│       ├── 8e4ce03aaef50adab4b1e1d168fe6ca6eafd5b59a3b61d4ada6abf79ade473d3_libnfc_nci_jni.so
│       └── files.json
├── functions.json
├── x64
│   ├── fix
│   │   ├── 1e9ea23155ce81bddcd2179dd5ceaea748c18fa20e8b901f4836c62095301e24_libnfc_nci_jni.so
│   │   ├── c2e8f6ef9fb081b2b817fcfc36176cf333992987ee17b7ff49d2861e053550a8_libnfc_nci_jni.so
│   │   └── files.json
│   └── vuln
│       ├── 30611971a2dab970a1ed6e3a8da88ac61b45c59aedfc90432488c0b9532326a4_libnfc_nci_jni.so
│       ├── 440cfd9abd9feda87be89c7ed97aad776ac884ce8ee723235e0d5f9b200d4c1c_libnfc_nci_jni.so
│       └── files.json
└── x86
    ├── fix
    │   ├── 48f844d1e6909da7ff0a2ae7e4e03c81e8b2d854048c86e9dc10e2af528ee6ab_libnfc_nci_jni.so
    │   ├── e7d7162d279595bfba5f724fa2ad7941d6223b4c1ede6ba1228831193477a70f_libnfc_nci_jni.so
    │   └── files.json
    └── vuln
        ├── 182f7ce7eab20238d6bb83d57227212f1b964c512c70761f26117e22b9ca753b_libnfc_nci_jni.so
        ├── f76e2bff59ae3bd91b41a23285b4402284b563647ce84f553ea328709470f3a4_libnfc_nci_jni.so
        └── files.json

```

