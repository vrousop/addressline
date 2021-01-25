import json


class Address:
    """
    Address class: contains the street and housenumber of an address and creates the json output
    """
    def __init__(self, full_address, street=None, number=None):
        self.full_address = full_address
        self.street = street
        self.housenumber = number

    def set_street(self, street):
        """
        set function for the Address' street
        :param street: string
        :return: None
        """
        self.street = street

    def get_street(self):
        """
        get function for the Address' street
        :return: street string
        """
        return self.street

    def set_number(self, number):
        """
        set function for the Address' housenumber
        :param number: sting
        :return: None
        """
        self.housenumber = number

    def get_housenumber(self):
        """
        get function for the Address' housenumber
        :return: housenumber string
        """
        return self.housenumber

    def print_address(self):
        """
        the function prints the concatenated address json
        :return: None
        """
        print(self.to_json())

    def to_json(self):
        """
        the function creates the concatenated address json
        :return: json object of address street and housenumber
        """
        address = {"street": self.street,
                   "housenumber": self.housenumber}
        return json.dumps(address)


