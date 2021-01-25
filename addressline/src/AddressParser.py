import re

from addressline.src.Address import Address


class AddressParser:
    """
    This class takes as input a string of address and parses it.
    The output is a string of street and a string of street-number as JSON object
    """

    def __init__(self):
        pass

    def parse_address(self, address):
        """
         This functions extracts street and housenumber from an address string based on different possible cases.
        :param address: Address class object
        :return: string of street and string of street-number as JSON object
        """
        # removing comma from input address string
        address.full_address = address.full_address.replace(",", "")

        # find the number of numerical parts in address
        digits = self.digits_in_address(address.full_address)

        # check if address starts with a number
        if self.address_start_with_number(address.full_address):
            # check if address contains more than one numerical parts
            if len(digits) > 1:
                # check if the first address part is ordinal (1st, 2nd, 3rd, 5th etc.)
                if self.ordinal_in_street(address.full_address):
                    # check if the address contains Number or No and split there otherwise split in first number
                    # occurred
                    if "No" in address.full_address:
                        splitter = "No"
                    if "Number" in address.full_address:
                        splitter = "Number"
                    else:
                        splitter = digits[1]
                    split_address = address.full_address.split(splitter)
                    housenumber = splitter + split_address[-1]
                    street = split_address[0]
                else:
                    housenumber = address.full_address.split(" ")[0]
                    street = address.full_address[len(housenumber) + 1:]
            else:
                # if only one numerical part exists then it is the housenumber
                housenumber = address.full_address.split(" ")[0]
                street = address.full_address[len(housenumber) + 1:]
        # if address does not start with number
        else:
            # check if address contains more than one numerical parts
            if len(digits) > 1:
                # first numerical is street, second is the housenumber
                street_digit = digits[0]
                street_str_end = address.full_address.index(street_digit) + len(street_digit)
                street = address.full_address[:street_str_end]
                housenumber = address.full_address[street_str_end + 1:]

            # if address contains only one numerical part
            else:
                # find the numeric part
                res = re.findall(r'[0-9]+', address.full_address)
                # check if the address contains Number or No and split there otherwise split in first number
                # occurred
                if "No" in address.full_address:
                    splitter = "No"
                if "Number" in address.full_address:
                    splitter = "Number"
                else:
                    splitter = res[0]
                split_address = address.full_address.split(splitter)
                housenumber = splitter + split_address[-1]
                street = split_address[0]
        # set street and housenumber found by above cases in Address object
        address.set_street(street.strip())
        address.set_number(housenumber.strip())
        # return output json

    def digits_in_address(self, full_address):
        """
        find numeric parts of address
        :param full_address: address string
        :return: list of numeric parts in address
        """
        digits = []
        for substring in full_address.split(" "):
            contains_digit = any(map(str.isdigit, substring))
            if contains_digit:
                digits.append(substring)
        return digits

    def address_start_with_number(self, full_address):
        """
        check if address string starts with number and return True, otherwise False
        :param full_address: address string
        :return: True/False
        """
        if full_address[0].isdigit():
            return True
        return False

    def ordinal_in_street(self, full_address):
        """
        check if ordinal number exists in address string and returns True, otherwise False
        :param full_address: address string
        :return: True/False
        """
        return any(x in full_address.split(" ")[0] for x in ['st', 'nd', 'rd', 'th'])
