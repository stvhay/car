"""vehicle.py"""
import argparse
import yaml

import car


def main():
    """
    Main function reads Tesla car API and outputs Yaml.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', help='Specify username')
    parser.add_argument('-i', '--id', help='Specify vehicle id')
    args = parser.parse_args()

    try:
        with open('.id') as f:
            id_ = yaml.safe_load(f.read())
            if args.id:
                id_ = args.id
    except IOError:
        id_ = args.id

    s = car.RESTSession(*car.get_credentials(args))
    r = s.get('api/1/vehicles/{}'.format(id_))
    d = yaml.safe_load(r.text)['response']
    print(yaml.dump(d))


if __name__ == '__main__':
    main()
