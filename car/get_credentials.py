"""Get credentials function."""
import getpass
import yaml


def get_credentials(args):
    """
    Load credentials from file or arguments.
    :param password: Password string.
    @return: (username, password)
    """
    try:
        with open('.credentials') as f:
            c = yaml.safe_load(f.read())
            password = c.get('password')
            if not password:
                getpass.getpass("Password")
            username = c.get('username')
            if not username:
                username = input("Username: ")
            if args.username:
                username = args.username
    except IOError:
        username = args.username
        password = getpass.getpass()
    return username, password
