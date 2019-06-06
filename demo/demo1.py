#!/usr/bin/env python
# coding=utf-8

import math

#math.pi为Π,3.1415926
radius=float(input('请输入圆的半径：'))
perimeter=2*math.pi*radius
area=math.pi * radius * radius
print ('周长: %.2f' % perimeter)
print ('面积: %.2f' % area)
