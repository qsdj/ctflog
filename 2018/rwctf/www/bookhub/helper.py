import flask
import os
import ipaddress


def op(v):
    print('-' * 30)
    print(v)
    print('-' * 30)


def ip_address_in(ip, ip_range):
    try:
        for item in ip_range.split(','):
            if ipaddress.ip_address(ip) in ipaddress.ip_network(item):
                return True
    except Exception as e:
        pass

    return False


def get_remote_addr():
    address = flask.request.headers.get(
        'X-Forwarded-For', flask.request.remote_addr)

    try:
        ipaddress.ip_address(address)
    except ValueError as e:
        op(e)
        return None
    else:
        return address
