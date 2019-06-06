#!/usr/bin/env python
# coding=utf-8

from random import randint

face=randint(1,6)
if face==1:
    result='自己'
elif face==2:
    result='下家'
elif face==3:
    result='对门'
elif face==4:
    result='上家'
elif face==5:
    result='自己'
else:
    result='下家'

print result
