# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 16:05:33 2018

@author: cwktu
"""
"""
详细机理和简化机理在Chemkin中计算得到13组数据，温度分别为700
、750、800、850、900、950、1000、1050、1100、1150、1200、1300、1400K
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



##%%求曲线斜率最大点(即着火燃烧点)
def combustion_time(data,m):
    slope_max = 0
    time = 0
    if m==1:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#1_(sec)'][i]
            timex2 = data['Time_Soln#1_(sec)'][i+1]
            tempy1 = data[' Pressure_Soln#1_(dyne/cm2)'][i]
            
            tempy2 = data[' Pressure_Soln#1_(dyne/cm2)'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==2:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#2_(sec)'][i]
            timex2 = data['Time_Soln#2_(sec)'][i+1]
            tempy1 = data[' Pressure_Soln#2_(dyne/cm2)'][i]
            tempy2 = data[' Pressure_Soln#2_(dyne/cm2)'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==3:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#3_(sec)'][i]
            timex2 = data['Time_Soln#3_(sec)'][i+1]
            tempy1 = data[' Pressure_Soln#3_(dyne/cm2)'][i]
            tempy2 = data[' Pressure_Soln#3_(dyne/cm2)'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==4:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#4_(sec)'][i]
            timex2 = data['Time_Soln#4_(sec)'][i+1]
            tempy1 = data[' Pressure_Soln#4_(dyne/cm2)'][i]
            tempy2 = data[' Pressure_Soln#4_(dyne/cm2)'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==5:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#5_(sec)'][i]
            timex2 = data['Time_Soln#5_(sec)'][i+1]
            tempy1 = data[' Pressure_Soln#5_(dyne/cm2)'][i]
            tempy2 = data[' Pressure_Soln#5_(dyne/cm2)'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==6:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#6_(sec)'][i]
            timex2 = data['Time_Soln#6_(sec)'][i+1]
            tempy1 = data[' Pressure_Soln#6_(dyne/cm2)'][i]
            tempy2 = data[' Pressure_Soln#6_(dyne/cm2)'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==7:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#7_(sec)'][i]
            timex2 = data['Time_Soln#7_(sec)'][i+1]
            tempy1 = data[' Pressure_Soln#7_(dyne/cm2)'][i]
            tempy2 = data[' Pressure_Soln#7_(dyne/cm2)'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==8:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#8_(sec)'][i]
            timex2 = data['Time_Soln#8_(sec)'][i+1]
            tempy1 = data[' Pressure_Soln#8_(dyne/cm2)'][i]
            tempy2 = data[' Pressure_Soln#8_(dyne/cm2)'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==9:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#9_(sec)'][i]
            timex2 = data['Time_Soln#9_(sec)'][i+1]
            tempy1 = data[' Pressure_Soln#9_(dyne/cm2)'][i]
            tempy2 = data[' Pressure_Soln#9_(dyne/cm2)'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==10:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#10_(sec)'][i]
            timex2 = data['Time_Soln#10_(sec)'][i+1]
            tempy1 = data[' Pressure_Soln#10_(dyne/cm2)'][i]
            tempy2 = data[' Pressure_Soln#10_(dyne/cm2)'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==11:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#11_(sec)'][i]
            timex2 = data['Time_Soln#11_(sec)'][i+1]
            tempy1 = data[' Pressure_Soln#11_(dyne/cm2)'][i]
            tempy2 = data[' Pressure_Soln#11_(dyne/cm2)'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==12:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#12_(sec)'][i]
            timex2 = data['Time_Soln#12_(sec)'][i+1]
            tempy1 = data[' Pressure_Soln#12_(dyne/cm2)'][i]
            tempy2 = data[' Pressure_Soln#12_(dyne/cm2)'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==13:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#13_(sec)'][i]
            timex2 = data['Time_Soln#13_(sec)'][i+1]
            tempy1 = data[' Pressure_Soln#13_(dyne/cm2)'][i]
            tempy2 = data[' Pressure_Soln#13_(dyne/cm2)'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i

    return slope_max,time

#%%
b=10**((21684.188-21500)/10000)*1.12