#!/usr/bin/env python3
import argparse
import getpass
import yaml
from car.car_rest import RESTSession

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("username")
    args = parser.parse_args()
    username = args.username
    password = getpass.getpass()

    d = {}
    endpoints = ['vehicle_data', 'service_data', 'data_request/charge_state', 'data_request/climate_state',
                 'data_request/drive_state', 'data_request/gui_settings']

    s = RESTSession(username, password)
    r = s.get('api/1/vehicles')
    d['vehicles'] = yaml.safe_load(r.text)['response']

    d['vehicle'] = {}
    for v in d['vehicles']:
        v_id = v['id']
        entry = d['vehicle'][v_id] = {}
        for endpoint in endpoints:
            r = s.get('api/1/vehicles/{v}/{e}'.format(v=v_id, e=endpoint))
            info = yaml.safe_load(r.text)
            entry[endpoint] = info
    print(yaml.dump(d))
