"""get_info.py"""
import argparse
import yaml

import car


def main():
    """
    Main function reads Tesla car API and outputs Yaml.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', help='Specify username')
    args = parser.parse_args()

    d = {}
    endpoints = ['vehicle_data', 'service_data', 'data_request/charge_state', 'data_request/climate_state',
                 'data_request/drive_state', 'data_request/gui_settings']

    s = car.RESTSession(*car.get_credentials(args))
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


if __name__ == '__main__':
    main()
