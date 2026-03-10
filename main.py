#!/usr/bin/env python3

import json
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from featurevisor import create_instance

DATAFILE_URL = "https://featurevisor-example-cloudflare.pages.dev/production/featurevisor-tag-all.json"
FEATURE_KEY = "my_feature"
CONTEXT = {
    "userId": "123",
    "deviceId": "device-23456",
    "country": "nl",
}


def fetch_datafile(url: str) -> dict:
    try:
        request = Request(
            url,
            headers={
                "User-Agent": "featurevisor-example-python/1.0",
                "Accept": "application/json",
            },
        )
        with urlopen(request) as response:
            return json.load(response)
    except HTTPError as exc:
        raise RuntimeError(f"failed to fetch datafile: HTTP {exc.code}") from exc
    except URLError as exc:
        raise RuntimeError(f"failed to fetch datafile: {exc.reason}") from exc


def main() -> int:
    try:
        datafile = fetch_datafile(DATAFILE_URL)
        f = create_instance({"datafile": datafile, "logLevel": "error"})
        f.set_context(CONTEXT)
        enabled = f.is_enabled(FEATURE_KEY)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Datafile revision: {f.get_revision()}")
    print(f"Context: {json.dumps(CONTEXT)}")
    print(f"Feature '{FEATURE_KEY}' enabled: {enabled}")
    print(f"All evaluations: {json.dumps(f.get_all_evaluations(), sort_keys=True)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
