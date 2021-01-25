import argparse

from addressline.src.Address import Address
from addressline.src.AddressParser import AddressParser


def parse_args(*args):
    """
    Command Line Argument parser.
    """
    parser = argparse.ArgumentParser(
        description="""
        The input argument is a string address
        """
    )
    parser.add_argument(
        '-a',
        '--address',
        type=str,
        help="""
        Insert address string
        """,
        required=True
    )
    return parser.parse_args(*args)


def main(*args):
    """
    The function takes the input address, implements the AddressParser class in order to concatenate the address to
    street and housenumber strings and prints the json output
    :param args: -a addressline string
    :return: None
    """
    args = parse_args(*args)
    parser = AddressParser()
    address = Address(args.address)
    parser.parse_address(address)
    print(address.to_json())
