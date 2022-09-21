'''
This file contains the followings 
    - unique Phone Number creation  
'''


import string
import random

def random_code(size=8, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_Pnumber_generate(instance):
    number = random_code()

    take = instance.__class__
    take_exits = take.objects.filter(phoneNumber=number).exists()
    if take_exits:
        return unique_Pnumber_generate(instance)
    return number