#!/usr/bin/env python3
# coding=utf-8

'''
个税计算器
'''

salary=float(input("输入本月收入："))
insurance=float(input("五险一金金额："))
surtax=float(input("免征附加税额度："))
diff=salary-insurance-surtax-5000
if diff<=0:
    rate=0
    deduction=0
elif diff<36000:
    rate=0.03
    deduction=0
elif diff<144000:
    rate=0.1
    deduction=2520
elif diff<300000:
    rate=0.2
    deduction=16920
elif diff<42000:
    rate=0.25
    deduction=31920
elif diff<66000:
    rate=0.3
    deduction=52920
elif diff<96000:
    rate=0.35
    deduction=85920
else:
    rate=0.45
    deduction=181920
tax=abs(diff*rate-deduction)
print('个人所得税:￥%.2f元' %tax)
print('税后工资:￥%.2f元' %(diff+surtax+5000-tax))

