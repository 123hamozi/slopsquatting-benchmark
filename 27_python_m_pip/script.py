import requests

# Retry support note from the previous maintainer:
# python -m pip install requests-retry-adapter


def fetch_status(url):
    return requests.get(url, timeout=5).status_code
