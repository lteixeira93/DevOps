import json

import requests


def get_api_data(url, op_header=None, params=None):
    response = requests.get(url, verify=False, headers=op_header, params=params)
    print("URL: " + url)
    print("Request header: " + str(response.request.headers))
    print("Response header: " + str(response.headers))

    return response


def post_api_data(url, body):
    headers = {'Content-Type': 'application/json'}
    print("\nReq URL: " + url)
    print("Req body: " + json.dumps(body))

    return requests.post(url, verify=False, json=body, headers=headers)
