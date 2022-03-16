import re
from ssl import get_protocol_name
from time import time
from tokenize import Number
import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number=input("Enter your No. with +__: ")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(car)
print(reg)