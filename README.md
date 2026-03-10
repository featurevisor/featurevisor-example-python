# featurevisor-example-python

Tiny example application using the Featurevisor Python SDK.

It mirrors the Go example by:

- fetching a remote Featurevisor datafile,
- creating a Featurevisor instance,
- setting evaluation context inside the script,
- printing whether a feature is enabled.

The example uses this datafile:

[https://featurevisor-example-cloudflare.pages.dev/production/featurevisor-tag-all.json](https://featurevisor-example-cloudflare.pages.dev/production/featurevisor-tag-all.json)

## Requirements

- Python 3.10+

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## What It Does

The script fetches the remote datafile, builds a Featurevisor instance, sets this default context, and evaluates a feature:

```json
{
  "userId": "123",
  "deviceId": "device-23456",
  "country": "nl"
}
```

It evaluates `my_feature`, which exists in the sample datafile.
