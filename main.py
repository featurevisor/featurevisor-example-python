#!/usr/bin/env python3

import json
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from featurevisor import create_featurevisor

DATAFILE_URL = "https://featurevisor-example-cloudflare.pages.dev/production/featurevisor-sdk-v3.json"
CONTEXT = {
    "userId": "customer-123",
    "country": "nl",
    "locale": "nl-NL",
    "accountPlan": "pro",
}


def fetch_datafile(url: str) -> dict:
    request = Request(
        url,
        headers={
            "User-Agent": "featurevisor-example-python/1.0",
            "Accept": "application/json",
        },
    )

    try:
        with urlopen(request, timeout=10) as response:
            return json.load(response)
    except HTTPError as exc:
        raise RuntimeError(f"failed to fetch datafile: HTTP {exc.code}") from exc
    except URLError as exc:
        raise RuntimeError(f"failed to fetch datafile: {exc.reason}") from exc


def main() -> int:
    f = None

    try:
        f = create_featurevisor(
            {
                "datafile": fetch_datafile(DATAFILE_URL),
                "context": CONTEXT,
                "logLevel": "error",
            }
        )

        commerce_enabled = f.is_enabled("commerce_platform")
        checkout_variation = f.get_variation("checkout_experience")
        max_items = f.get_variable_integer("checkout_experience", "max_items")
        payment_methods = f.get_variable_array(
            "checkout_experience", "payment_methods"
        )
        endpoints = f.get_variable_object("serviceEndpoints")
        support_contact = f.get_variable_string("supportContact")

        print(f"Commerce platform enabled: {str(commerce_enabled).lower()}")
        print(f"Checkout variation: {value_or_unavailable(checkout_variation)}")
        print(f"Maximum checkout items: {value_or_unavailable(max_items)}")
        print(f"Payment methods: {payment_methods or []}")
        print(
            f"Service endpoint: {endpoints['baseUrl']} "
            f"(timeout: {endpoints['timeoutMs']} ms, retries: {endpoints['retries']})"
        )
        print(f"Support contact: {value_or_unavailable(support_contact)}")
        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    finally:
        if f is not None:
            f.close()


def value_or_unavailable(value: object) -> object:
    return "unavailable" if value is None else value


if __name__ == "__main__":
    raise SystemExit(main())
