import json
import traceback
import os

from .json import json_default

def http_response(status_code: int, body: str, headers: dict = None):
    """Helper function to return a HTTP Response with CORS and a given status code and body"""

    if headers is None:
        headers = {}

    return (body, status_code, headers)

def json_response(status_code: int, data: any, headers: dict = None):
    """Returns an http response with JSON encoded body"""

    if headers is None:
        headers = {}

    if isinstance(data, str):
        data = {
            'statusCode': status_code,
            'message': data
        }

    if isinstance(data, list):
        headers = {
            **headers,
            'X-Count': len(data)
        }

    return http_response(status_code, "" if data is None else json.dumps(data, default=json_default), {
        **headers,
        'Content-Type': 'application/json',
        'Docker-Distribution-Api-Version': 'registry/2.0'
    })


def ok(data: any = None, headers: dict = {}):
    """Returns a json encoded 200 OK Response"""
    return json_response(200, data, headers)