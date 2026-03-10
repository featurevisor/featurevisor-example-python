# featurevisor-example-python

Tiny example application using the [Featurevisor Python SDK](https://github.com/featurevisor/featurevisor-python).

Learn more about Featurevisor at [featurevisor.com](https://featurevisor.com).

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

## Featurevisor project

Uses this Featurevisor project to fetch the configuration from: https://github.com/featurevisor/featurevisor-example-cloudflare
