## Addressline

The Addressline project receives an address as a string, parses it and returns the street and housenumber fields.

**Input:** string of address

**Output:** string of street and string of street-number as JSON object

**Examples:**
1. Simple cases
   1. `"Winterallee 3"` -> `{"street": "Winterallee", "housenumber": "3"}`
   1. `"Musterstrasse 45"` -> `{"street": "Musterstrasse", "housenumber": "45"}`
   1. `"Blaufeldweg 123B"` -> `{"street": "Blaufeldweg", "housenumber": "123B"}`

2. Complicated cases
   1. `"Am Bächle 23"` -> `{"street": "Am Bächle", "housenumber": "23"}`
   1. `"Auf der Vogelwiese 23 b"` -> `{"street": "Auf der Vogelwiese", "housenumber": "23 b"}`

3. Complex cases
   1. `"4, rue de la revolution"` -> `{"street": "rue de la revolution", "housenumber": "4"}`
   1. `"200 Broadway Av"` -> `{"street": "Broadway Av", "housenumber": "200"}`
   1. `"Calle Aduana, 29"` -> `{"street": "Calle Aduana", "housenumber": "29"}`
   1. `"Calle 39 No 1540"` -> `{"street": "Calle 39", "housenumber": "No 1540"}`

**Solution:**
The code implements two Classes: Address and AddressParser.

It includes a test folder with a testing csv file and a python test module
### Run instructions:
1. Install package:

In the directory where setup.py is located run:
```
pip install .
```
2. Run test:
```
run_test.py
```
2. Run in command line:
```
addressline -a "address string"
```
### Usage:

```python
from addressline.src.Address import Address
from addressline.src.AddressParser import AddressParser

# Initialize AddressParser object
parser = AddressParser()
# Initialize Address object with the initial address string
address = Address('Winterallee 3')
# The parse_address method of AddressParser class will split the address string into street and housenumber components and set Address object
parser.parse_address(address)
# The to_json method will return the json object with the concatenated address
# expected output: {"street": "Winterallee", "housenumber": "3"}
address.to_json()
 ```