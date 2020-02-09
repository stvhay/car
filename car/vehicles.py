#!/usr/bin/env python3
import argparse
import yaml

import car
import car.car_rest


def main():
    """
    Main function reads Tesla car API and outputs Yaml.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', help='Specify username')
    args = parser.parse_args()

    s = car.car_rest.RESTSession(*car.get_credentials(args))
    r = s.get('api/1/vehicles')
    d = {'vehicles': yaml.safe_load(r.text)['response']}
    print(yaml.dump(d))


if __name__ == '__main__':
    main()
