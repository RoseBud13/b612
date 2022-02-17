"""
utils.py
- 
Created by Xiong, Kaijie on 2022-02-16.
Copyright © 2021 Xiong, Kaijie. All rights reserved.
"""

import random, string
from .models import db, Musubi, MusubiAlpha, MusubiBeta


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
    def get_ab_data(alpha_code):
        print(alpha_code)
        data_alpha = MusubiAlpha.query.filter_by(musubi_code=alpha_code).first()
        data_beta = MusubiBeta.query.filter_by(musubi_code=alpha_code).first()

        if not data_alpha and data_beta:
            return 'musubi alpha not exists'
        elif not data_beta and data_alpha:
            return 'musubi beta not exists'
        elif not data_alpha and not data_beta:
            return 'musubi code not exists'
        else:
            alpha = {'alpha': data_alpha.to_dict()}
            beta = {'beta': data_beta.to_dict()}

            ab_data = {**alpha, **beta}
            ab_data['musubi_code'] = alpha_code
            print(ab_data)
            return ab_data



# if __name__ == '__main__':
#     gen_default_musubi_code()
