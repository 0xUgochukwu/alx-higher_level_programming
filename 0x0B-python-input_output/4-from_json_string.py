#!/usr/bin/python3
""" Convert JSON to object"""
import json


def from_json_string(my_str):
    """ Convert JSON to object"""
    return json.loads(my_str)
