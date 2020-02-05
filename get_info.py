#!/usr/bin/env python3
import sys
import yaml
from car_rest import RESTSession

if __name__ == '__main__':
    username = 'hay.steve@gmail.com'
    print("Password:")
    password = sys.stdin.readline().strip()

    endpoints = ['vehicle_data', 'service_data', 'data_request/charge_state', 'data_request/climate_state',
                 'data_request/drive_state', 'data_request/gui_settings']

    s = RESTSession(username, password)
    r = s.get('api/1/vehicles')
    vehicles = yaml.safe_load(r.text)
    print()
    print("Vehicle List")
    print(yaml.dump(vehicles))

    for v in vehicles['response']:
        print()
        v_id = v['id']
        for endpoint in endpoints:
            r = s.get('api/1/vehicles/{}/{}'.format(v_id, endpoint))
            info = yaml.safe_load(r.text)
            print("Endpoint: {}".format(endpoint))
            print(yaml.dump(info))
