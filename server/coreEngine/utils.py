"""
utils.py
- 
Created by Xiong, Kaijie on 2022-02-16.
Copyright © 2021 Xiong, Kaijie. All rights reserved.
"""

import random, string
from .models import db, Musubi, Reiteki


class Tools():
    def gen_default_musubi_code():
        ran_code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        print(ran_code)
        return ran_code
    
    def convert_tuple(tuple):
        str = ''
        for item in tuple:
            str = str + item
        return str


class DataHandler():
    def get_paired_reiteki(code):
        reiteki_list = Reiteki.query.filter_by(musubi_code=code).all()
        print(reiteki_list)

        if not reiteki_list:
            return 'no related reiteki exists'
        elif len(reiteki_list) != 2:
            return 'no reiteki pair exists'
        else:
            first= {'first': reiteki_list[0].to_dict()}
            second = {'second': reiteki_list[1].to_dict()}

            paired_reiteki = {**first, **second}
            paired_reiteki['musubi_code'] = code
            print(paired_reiteki)
            return paired_reiteki



# if __name__ == '__main__':
#     gen_default_musubi_code()
