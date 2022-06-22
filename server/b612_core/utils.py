"""
utils.py
- 
Created by Rosebud on 2022-06-13.
Copyright © 2022 Rosebud. All rights reserved.
"""

import random, string


class Tools():
    def gen_random_code(length):
        rand_code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        # print(rand_code)
        return rand_code
    
    def tuple_to_str(tuple):
        str = ''
        for item in tuple:
            str = str + item
        return str

