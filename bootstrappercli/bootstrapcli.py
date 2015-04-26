#!/usr/bin/env python

import requests
import json

BOOTSTRAPPER__PROD_URL = "http://prod.example.com:8000"
BOOTSTRAPPER_STAGING_URL = "http://staging.example.com:8000"

def get_url(infra_env):
    if infra_env == "prod":
        return BOOTSTRAPPER__PROD_URL
    else:
        return BOOTSTRAPPER_STAGING_URL

def bootstrap(ans_host, ans_role, ans_env):
    base_url = get_url(ans_env)
    req_url = base_url + '/ansible/roles/'
    resp = requests.post(req_url, data={'host': ans_host, 'role': ans_role, 'env': ans_env})
    return [resp.status_code, resp.text]

def adhoc(ans_host, ans_mod, ans_arg, ans_env):
    base_url = get_url(ans_env)
    req_url = base_url + '/ansible/adhoc/'
    if ans_arg is None:
        resp = requests.get(req_url, params={'host': ans_host, 'mod': ans_mod})
    else:
        resp = requests.get(req_url, params={'host': ans_host, 'mod': ans_mod, 'arg': ans_arg})
    return [resp.status_code, resp.text]

def adhocj(ans_host, ans_mod, ans_arg, ans_env):
    base_url = get_url(ans_env)
    req_url = base_url + '/ansible/adhoc/job/'
    if ans_arg is None:
        resp = requests.get(req_url, params={'host': ans_host, 'mod': ans_mod})
    else:
        resp = requests.get(req_url, params={'host': ans_host, 'mod': ans_mod, 'arg': ans_arg})
    return [resp.status_code, resp.text]

def result(ans_jid, ans_env):
    base_url = get_url(ans_env)
    req_url = base_url + '/ansible/results/' + ans_jid
    resp = requests.get(req_url)
    return [resp.status_code, resp.text]
