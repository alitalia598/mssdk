# -*- coding:utf-8 -*-
# /usr/bin/env python
"""
Author: qhsdk
date: 2020/2/13 21:22
desc: 存储和读取Token文件
"""
import os

import pandas as pd

from qhsdk.pro import cons


def set_token(token):
    df = pd.DataFrame([token], columns=['token'])
    user_home = os.path.expanduser('~')
    fp = os.path.join(user_home, cons.TOKEN_F_P)
    df.to_csv(fp, index=False)


def get_token():
    user_home = os.path.expanduser('~')
    fp = os.path.join(user_home, cons.TOKEN_F_P)
    if os.path.exists(fp):
        df = pd.read_csv(fp)
        return str(df.iloc[0]['token'])
    else:
        print(cons.TOKEN_ERR_MSG)
        return None


if __name__ == '__main__':
    pass