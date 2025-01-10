# /// script
# dependencies = [
#   "requests==2.32.3",
#   "mistletoe==1.4.0",
# ]
# ///

import sys
from mistletoe import Document, span_token, ast_renderer
import requests
import unicodedata

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
SUCCESS_EMOJI = unicodedata.lookup('White Heavy Check Mark')
FAILURE_EMOJI = unicodedata.lookup('Cross Mark')

if len(sys.argv) != 2:
    print('Usage: uv run checklinks.py README.md')
    sys.exit(1)

urls = []

def walk(token):
    if hasattr(token, 'content'):
        # Skip RawText objects, as they have no children
        # https://github.com/miyuchina/mistletoe/issues/31
        return
    for child in token.children:
        if isinstance(child, span_token.Link):
            if child.target.startswith('http'):
                # Only check http[s] links
                urls.append(child.target)
        walk(child)

with open(sys.argv[1], 'r') as f:
    # Extract links from Markdown
    walk(Document(f.read()))

    # Request links and log results
    session = requests.Session()
    session.headers.update({'User-Agent': USER_AGENT})
    for url in urls:
        try:
            r = session.get(url, timeout=10)
        except requests.exceptions.ReadTimeout:
            print(f'{FAILURE_EMOJI} {url} connection timeout')
            continue
        except requests.exceptions.ConnectionError:
            print(f'{FAILURE_EMOJI} {url} connection error')
            continue
        if r.status_code not in [200]:
            print(f'{FAILURE_EMOJI} {url} responded with HTTP {r.status_code}')
            continue
        print(f'{SUCCESS_EMOJI} {url}')
