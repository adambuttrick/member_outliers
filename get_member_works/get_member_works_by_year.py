import argparse
import os
import requests
import time
import json


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--member_id", type=int, required=True)
    parser.add_argument("-y", "--year", type=int, required=True)
    parser.add_argument('-u', '--user_agent', type=str,
                    help='User Agent for the request (mailto:name@email)')
    parser.add_argument("-t", "--token", type=str,
                        help='Crossref Metadata Plus API token')
    return parser.parse_args()


def download_json(member_id, year, headers, rows=1000):
    BASE_URL = "https://api.crossref.org/members/{}/works".format(member_id)
    directory_name = f"member_{member_id}_{year}"
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    cursor = '*'
    page_num = 1
    while True:
        response = requests.get(BASE_URL, params={
            "filter": f"from-pub-date:{year}",
            "cursor": cursor,
            "rows": rows
        }, headers=headers)
        if response.status_code != 200:
            break
        items = response.json().get('message', {}).get('items',[])
        if not items:
            break
        with open(f"{directory_name}/page_{page_num}.json", "w") as file:
            json.dump(response.json(), file)
        cursor = response.json().get('message', {}).get('next-cursor', None)
        if not cursor:
            break
        page_num += 1
        time.sleep(1)


def main():
    args = parse_arguments()
    headers = {}
    if args.token:
        headers['Crossref-Plus-API-Token'] = args.token
    if args.user_agent:
        headers['User-Agent'] = args.user_agent
    download_json(args.member_id, args.year, headers)


if __name__ == "__main__":
    main()
