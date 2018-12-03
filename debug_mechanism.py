# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 12:09:05 2018
原始fitness:0.26 ;;四工况：1.012

@author: cwktu
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import subprocess
from math import sqrt
import os

##%%求曲线斜率最大点(即着火燃烧点)
def combustion_time(data,m):
    slope_max = 0
    time = 0
    if m==1:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#1_(sec)'][i]
            timex2 = data['Time_Soln#1_(sec)'][i+1]
            tempy1 = data[' Mole_fraction_OH_Soln#1_()'][i]
            tempy2 = data[' Mole_fraction_OH_Soln#1_()'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==2:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#2_(sec)'][i]
            timex2 = data['Time_Soln#2_(sec)'][i+1]
            tempy1 = data[' Mole_fraction_OH_Soln#2_()'][i]
            tempy2 = data[' Mole_fraction_OH_Soln#2_()'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==3:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#3_(sec)'][i]
            timex2 = data['Time_Soln#3_(sec)'][i+1]
            tempy1 = data[' Mole_fraction_OH_Soln#3_()'][i]
            tempy2 = data[' Mole_fraction_OH_Soln#3_()'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==4:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#4_(sec)'][i]
            timex2 = data['Time_Soln#4_(sec)'][i+1]
            tempy1 = data[' Mole_fraction_OH_Soln#4_()'][i]
            tempy2 = data[' Mole_fraction_OH_Soln#4_()'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==5:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#5_(sec)'][i]
            timex2 = data['Time_Soln#5_(sec)'][i+1]
            tempy1 = data[' Mole_fraction_OH_Soln#5_()'][i]
            tempy2 = data[' Mole_fraction_OH_Soln#5_()'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==6:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#6_(sec)'][i]
            timex2 = data['Time_Soln#6_(sec)'][i+1]
            tempy1 = data[' Mole_fraction_OH_Soln#6_()'][i]
            tempy2 = data[' Mole_fraction_OH_Soln#6_()'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==7:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#7_(sec)'][i]
            timex2 = data['Time_Soln#7_(sec)'][i+1]
            tempy1 = data[' Mole_fraction_OH_Soln#7_()'][i]
            tempy2 = data[' Mole_fraction_OH_Soln#7_()'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==8:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#8_(sec)'][i]
            timex2 = data['Time_Soln#8_(sec)'][i+1]
            tempy1 = data[' Mole_fraction_OH_Soln#8_()'][i]
            tempy2 = data[' Mole_fraction_OH_Soln#8_()'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==9:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#9_(sec)'][i]
            timex2 = data['Time_Soln#9_(sec)'][i+1]
            tempy1 = data[' Mole_fraction_OH_Soln#9_()'][i]
            tempy2 = data[' Mole_fraction_OH_Soln#9_()'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==10:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#10_(sec)'][i]
            timex2 = data['Time_Soln#10_(sec)'][i+1]
            tempy1 = data[' Mole_fraction_OH_Soln#10_()'][i]
            tempy2 = data[' Mole_fraction_OH_Soln#10_()'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==11:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#11_(sec)'][i]
            timex2 = data['Time_Soln#11_(sec)'][i+1]
            tempy1 = data[' Mole_fraction_OH_Soln#11_()'][i]
            tempy2 = data[' Mole_fraction_OH_Soln#11_()'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==12:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#12_(sec)'][i]
            timex2 = data['Time_Soln#12_(sec)'][i+1]
            tempy1 = data[' Mole_fraction_OH_Soln#12_()'][i]
            tempy2 = data[' Mole_fraction_OH_Soln#12_()'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==13:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#13_(sec)'][i]
            timex2 = data['Time_Soln#13_(sec)'][i+1]
            tempy1 = data[' Mole_fraction_OH_Soln#13_()'][i]
            tempy2 = data[' Mole_fraction_OH_Soln#13_()'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i

    return slope_max,time
    
def error(a,b):
    error=[]
    for i in range(len(a)):
        error.append(abs((a[i]-b[i])/b[i]))
    me = sum(error)/len(error)
    return me

def Mean_squared_error(a,b):
    error=[]
    for i in range(len(a)):
        error.append((a[i]-b[i])*(a[i]-b[i]))
    mse = sum(error)/len(error)
    rmse = sqrt(mse)
    return rmse
def mechanism_computation(path):
    data1 = pd.read_csv(path+"/CKSoln_solution_no_1.csv")
    data2 = pd.read_csv(path+"/CKSoln_solution_no_2.csv")
    data3 = pd.read_csv(path+"/CKSoln_solution_no_3.csv")
    data4 = pd.read_csv(path+"/CKSoln_solution_no_4.csv")
    data5 = pd.read_csv(path+"/CKSoln_solution_no_5.csv")
    data6 = pd.read_csv(path+"/CKSoln_solution_no_6.csv")
    data7 = pd.read_csv(path+"/CKSoln_solution_no_7.csv")
    data8 = pd.read_csv(path+"/CKSoln_solution_no_8.csv")
    data9 = pd.read_csv(path+"/CKSoln_solution_no_9.csv")
    data10 = pd.read_csv(path+"/CKSoln_solution_no_10.csv")
    data11 = pd.read_csv(path+"/CKSoln_solution_no_11.csv")
    data12 = pd.read_csv(path+"/CKSoln_solution_no_12.csv")
    data13 = pd.read_csv(path+"/CKSoln_solution_no_13.csv")
    
    #求解13个data的着火时间
    time_simplified=[]
    k1,l = combustion_time(data1,1)
    time1 = data1['Time_Soln#1_(sec)'][l]

    k1,l = combustion_time(data2,2)
    time2 = data2['Time_Soln#2_(sec)'][l]

    k1,l = combustion_time(data3,3)
    time3 = data3['Time_Soln#3_(sec)'][l]

    k1,l = combustion_time(data4,4)
    time4 = data4['Time_Soln#4_(sec)'][l]

    k1,l = combustion_time(data5,5)
    time5 = data5['Time_Soln#5_(sec)'][l]

    k1,l = combustion_time(data6,6)
    time6 = data6['Time_Soln#6_(sec)'][l]

    k1,l = combustion_time(data7,7)
    time7 = data7['Time_Soln#7_(sec)'][l]

    k1,l = combustion_time(data8,8)
    time8 = data8['Time_Soln#8_(sec)'][l]

    k1,l = combustion_time(data9,9)
    time9 = data9['Time_Soln#9_(sec)'][l]

    k1,l = combustion_time(data10,10)
    time10 = data10['Time_Soln#10_(sec)'][l]

    k1,l = combustion_time(data11,11)
    time11 = data11['Time_Soln#11_(sec)'][l]

    k1,l = combustion_time(data12,12)
    time12 = data12['Time_Soln#12_(sec)'][l]

    k1,l = combustion_time(data13,13)
    time13 = data13['Time_Soln#13_(sec)'][l]
    
    time_simplified.extend([time1,time2,time3,time4,time5,time6,time7,time8,time9,time10,time11,time12,time13])
    
    return time_simplified

 #定义适应度函数并实现种群初始化
def fitness_func(data,label=False):
    if(label==True):
        data["simplified2"] = data["simplified"].map(lambda x: x*1000000)
        y=Mean_squared_error(list(data["simplified2"]),list(data["detailed"]))
    else:
        data["simplified2"] = data["simplified"].map(lambda x: x*1000000)
        y=error(list(data["simplified2"]),list(data["detailed"]))
    
    return y

sizepop=4
rangespeed_x = (-0.2,0.2)
rangespeed_y = (-0.2,0.2)
rangepop_x = (-1,1)
rangepop_y = (-1,1)

pop = np.zeros((sizepop,2))
pop_r = np.zeros((sizepop,2))
v = np.zeros((sizepop,2))
fitness = np.zeros(sizepop)     #20个粒子，每个粒子都有一定的初始的适应度
prediction = np.zeros(sizepop)
data={}
data2={}
data3={}
data4={}

for i in range(sizepop):
    #A:5e8--5e11;E:2.15e3--2.15e5
    pop[i] = [(np.random.uniform()-0.5)*2*rangepop_x[1],(np.random.uniform()-0.5)*2*rangepop_y[1]]   #保证20个粒子的随机位置仍在[-2，2]之间,三个未知数的变化区间不同

    v[i] = [(np.random.uniform()-0.5)*2*rangespeed_x[1],(np.random.uniform()-0.5)*2*rangespeed_y[1]]
    
    #将参数数据放入IC16_optimized.input文件中
    path3 = "C:\\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\C12_simplified"
    IC16_file = open(path3+'\\NC12.inp')
    lines = IC16_file.readlines()
    IC16_file.close()
    
    #pop_r[i][0] = 10**(pop[i][0])*2.0e12
    #pop_r[i][1] = 10**(pop[i][1])*1.5e10
    pop_r[i][0] = 2.0e12
    pop_r[i][1] = 1.5e10
    #pop_r[i][0] = (10**pop[i][0]*1.5e5)/np.exp(-pop_r[i][1]/(1.98718*700))
    pop1=str(pop_r[i][0])
    pop2=str(pop_r[i][1])
    
    a='O2+NC12-QOOH=NC12-OOQOOH	   '+pop1+'  0.0  0.0'
    b='NC12-QOOH=>NC5H10+CH2O+C2H4+NC4H8+OH    '+pop2+'  0.0 1.41E4'
    lines[59] = a
    lines[65] = b

    
    IC16_newfile = open(path3+'\\C12_optimized.inp','w')
    for newline in lines:
        IC16_newfile.write(newline)
    IC16_newfile.close()
    
    ##多目标工况优化：40atm_1.5,40atm_0.5,10atm_0.5,10atm_1.5三种工况的最优值
    #对20atm_1.0工况简化机理进行计算
    path="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\C12_simplified"
    p = subprocess.Popen(path+'\ST.bat',shell=True,stdout=subprocess.PIPE)
    out,err = p.communicate()
    
    time_simplified = mechanism_computation(path) 
    #压力40atm,化学当量比1.5
    time_detailed_20atm = [3233.921,781.5868,264.7509,148.611,148.5894,204.8114,300.2886,287.9953,189.1959,108.1476,5.94E+01,1.87E+01,6.71E+00]
    temperature = [700,750,800,850,900,950,1000,1050,1100,1150,1200,1300,1400]
    Ignition_time = {"Temp":temperature,"simplified":time_simplified,"detailed":time_detailed_20atm}
    data[i] = pd.DataFrame(Ignition_time)
    os.remove(path+"/CKSoln_solution_no_1.csv")
    os.remove(path+"/CKSoln_solution_no_2.csv")
    os.remove(path+"/CKSoln_solution_no_3.csv")
    os.remove(path+"/CKSoln_solution_no_4.csv")
    os.remove(path+"/CKSoln_solution_no_5.csv")
    os.remove(path+"/CKSoln_solution_no_6.csv")
    os.remove(path+"/CKSoln_solution_no_7.csv")
    os.remove(path+"/CKSoln_solution_no_8.csv")
    os.remove(path+"/CKSoln_solution_no_9.csv")
    os.remove(path+"/CKSoln_solution_no_10.csv")
    os.remove(path+"/CKSoln_solution_no_11.csv")
    os.remove(path+"/CKSoln_solution_no_12.csv")
    os.remove(path+"/CKSoln_solution_no_13.csv")
#
    #对40atm_0.5简化工况进行计算
    path="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\C12_simplified"
    p = subprocess.Popen(path+'\ST2.bat',shell=True,stdout=subprocess.PIPE)
    out,err = p.communicate()
    
    time_simplified = mechanism_computation(path) 
    time_detailed_40atm = [4133.79,1219.066,604.7849,489.5824,513.6832,565.1864,666.0549,555.5153,348.3442,195.5727,1.06E+02,3.14E+01,1.01E+01]
    temperature = [700,750,800,850,900,950,1000,1050,1100,1150,1200,1300,1400]
    Ignition_time = {"Temp":temperature,"simplified":time_simplified,"detailed":time_detailed_40atm}
    data2[i] = pd.DataFrame(Ignition_time)
    os.remove(path+"/CKSoln_solution_no_1.csv")
    os.remove(path+"/CKSoln_solution_no_2.csv")
    os.remove(path+"/CKSoln_solution_no_3.csv")
    os.remove(path+"/CKSoln_solution_no_4.csv")
    os.remove(path+"/CKSoln_solution_no_5.csv")
    os.remove(path+"/CKSoln_solution_no_6.csv")
    os.remove(path+"/CKSoln_solution_no_7.csv")
    os.remove(path+"/CKSoln_solution_no_8.csv")
    os.remove(path+"/CKSoln_solution_no_9.csv")
    os.remove(path+"/CKSoln_solution_no_10.csv")
    os.remove(path+"/CKSoln_solution_no_11.csv")
    os.remove(path+"/CKSoln_solution_no_12.csv")
    os.remove(path+"/CKSoln_solution_no_13.csv")
#            
    #对8atm_0.5简化工况进行计算
    path="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\C12_simplified"
    p = subprocess.Popen(path+'\ST3.bat',shell=True,stdout=subprocess.PIPE)
    out,err = p.communicate()
    
    time_simplified = mechanism_computation(path) 
    time_detailed_10atm = [8907.39,7368.639,10401.59,14841.4,20517.01,14481.84,7262.785,3296.223,1466.022,667.4111,314.1158,7.59E+01,2.24E+01]
    temperature = [700,750,800,850,900,950,1000,1050,1100,1150,1200,1300,1400]
    Ignition_time = {"Temp":temperature,"simplified":time_simplified,"detailed":time_detailed_10atm}
    data3[i] = pd.DataFrame(Ignition_time)
    os.remove(path+"/CKSoln_solution_no_1.csv")
    os.remove(path+"/CKSoln_solution_no_2.csv")
    os.remove(path+"/CKSoln_solution_no_3.csv")
    os.remove(path+"/CKSoln_solution_no_4.csv")
    os.remove(path+"/CKSoln_solution_no_5.csv")
    os.remove(path+"/CKSoln_solution_no_6.csv")
    os.remove(path+"/CKSoln_solution_no_7.csv")
    os.remove(path+"/CKSoln_solution_no_8.csv")
    os.remove(path+"/CKSoln_solution_no_9.csv")
    os.remove(path+"/CKSoln_solution_no_10.csv")
    os.remove(path+"/CKSoln_solution_no_11.csv")
    os.remove(path+"/CKSoln_solution_no_12.csv")
    os.remove(path+"/CKSoln_solution_no_13.csv")
    
    #对8atm_1.5简化工况进行计算
    path="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\C12_simplified"
    p = subprocess.Popen(path+'\ST4.bat',shell=True,stdout=subprocess.PIPE)
    out,err = p.communicate()
    
    time_simplified = mechanism_computation(path) 
    time_detailed_10atm = [4722.957,2073.3,2587.254,5247.049,9606.955,7841.339,4133.981,1945.242,904.589,432.6391,215.2988,6.16E+01,2.26E+01]
    temperature = [700,750,800,850,900,950,1000,1050,1100,1150,1200,1300,1400]
    Ignition_time = {"Temp":temperature,"simplified":time_simplified,"detailed":time_detailed_10atm}
    data4[i] = pd.DataFrame(Ignition_time)
    os.remove(path+"/CKSoln_solution_no_1.csv")
    os.remove(path+"/CKSoln_solution_no_2.csv")
    os.remove(path+"/CKSoln_solution_no_3.csv")
    os.remove(path+"/CKSoln_solution_no_4.csv")
    os.remove(path+"/CKSoln_solution_no_5.csv")
    os.remove(path+"/CKSoln_solution_no_6.csv")
    os.remove(path+"/CKSoln_solution_no_7.csv")
    os.remove(path+"/CKSoln_solution_no_8.csv")
    os.remove(path+"/CKSoln_solution_no_9.csv")
    os.remove(path+"/CKSoln_solution_no_10.csv")
    os.remove(path+"/CKSoln_solution_no_11.csv")
    os.remove(path+"/CKSoln_solution_no_12.csv")
    os.remove(path+"/CKSoln_solution_no_13.csv")
    print("第%d个粒子初始化数据完成." %(i))
    fitness[i] = (fitness_func(data[i]) + fitness_func(data2[i]) + fitness_func(data3[i])+fitness_func(data4[i]))/4    #得到30个初始化粒子的简化机理着火时间数据后，与详细机理的着火时间数据进行比较，得到适应度
    #fitness[i] = fitness_func(data[i])
    
#%%
#寻找初始化后的极值
def getinitbest(fitness,pop):
    #群体最优的粒子位置和适应度值;;寻找最小值，使得适应度函数最小
    gbestpop,gbestfitness = pop[fitness.argmin()].copy(),fitness.min()
    
    #个体最优的粒子位置及其适应度值
    pbestpop,pbestfitness = pop.copy(),fitness.copy()
    
    return gbestpop,gbestfitness,pbestpop,pbestfitness

gbestpop,gbestfitness,pbestpop,pbestfitness = getinitbest(fitness,pop)
#%%
1000**0.1