#!/bin/env python
import json
import sys
try:
    import requests
except ImportError:
    print ("Please install the python-requests module.")
    sys.exit(-1)

UB_API = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q=surfing&key="
SSL_VERIFY = True

def get_json(url):
    # Performs a GET using the passed URL location
    r = requests.get(url, verify=SSL_VERIFY)
    return r.json()

def get_results(url):
    jsn = get_json(url)
    if jsn.get('error'):
        print ("Error: " + jsn['error']['message'])
    else:
        if jsn.get('results'):
            return jsn['results']
        elif 'results' not in jsn:
            return jsn
        else:
            print ("No results found")
    return None

def display_all_results(url):
    results = get_results(url)
    if results:
        print (json.dumps(results, indent=4, sort_keys=True))

def main():
    display_all_results(UB_API)


if __name__ == "__main__":
    main()
