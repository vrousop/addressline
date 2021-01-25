import json
import os
import unittest
import pandas as pd

from addressline.src.Address import Address
from addressline.src.AddressParser import AddressParser
from addressline.test import __PACKAGE_DIR__


def addressline_test(address):
    parser = AddressParser()
    address_obj = Address(address)
    parser.parse_address(address_obj)
    return address_obj.to_json()


class AddresslineTest(unittest.TestCase):
    def test(self):
        test_file = os.path.join(__PACKAGE_DIR__, "addresses.csv")
        df = pd.read_csv(test_file)
        df.apply(lambda row: self.assertEqual(addressline_test(row['address']),
                                              json.dumps({"street": row['street'], "housenumber": row['housenumber']})),
                 axis=1)


if __name__ == '__main__':
    unittest.main()
