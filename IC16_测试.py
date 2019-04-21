# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 14:45:07 2019

@author: cwktu
"""

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
#%%读取bat文件，并得到简化机理随着温度变化的着火时间数据  条件：40atm_当量比1.5--->time为简化机理结果列表
import subprocess
path="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\IC16_simplified"
p = subprocess.Popen(path+'\ST.bat',shell=True,stdout=subprocess.PIPE)
out,err = p.communicate()
#%%
import pandas as pd
#from All_data import combustion_time
path="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\IC16_simplified"

data1 = pd.read_csv(path+"/CKSoln_solution_no_1.csv")
data2 = pd.read_csv(path+"/CKSoln_solution_no_2.csv")
data3 = pd.read_csv(path+"/CKSoln_solution_no_3.csv")
data4 = pd.read_csv(path+"/CKSoln_solution_no_4.csv")
data5 = pd.read_csv(path+"/CKSoln_solution_no_5.csv")
data6 = pd.read_csv(path+"/CKSoln_solution_no_6.csv")
data7 = pd.read_csv(path+"/CKSoln_solution_no_7.csv")
data8 = pd.read_csv(path+"/CKSoln_solution_no_8.csv")
#data9 = pd.read_csv(path+"/CKSoln_solution_no_9.csv")
#data10 = pd.read_csv(path+"/CKSoln_solution_no_10.csv")
#data11 = pd.read_csv(path+"/CKSoln_solution_no_11.csv")
#data12 = pd.read_csv(path+"/CKSoln_solution_no_12.csv")
#data13 = pd.read_csv(path+"/CKSoln_solution_no_13.csv")

#求解13个data的着火时间
time_simplified1=[]
k1,i = combustion_time(data1,1)
time1 = data1['Time_Soln#1_(sec)'][i]

k1,i = combustion_time(data2,2)
time2 = data2['Time_Soln#2_(sec)'][i]

k1,i = combustion_time(data3,3)
time3 = data3['Time_Soln#3_(sec)'][i]

k1,i = combustion_time(data4,4)
time4 = data4['Time_Soln#4_(sec)'][i]

k1,i = combustion_time(data5,5)
time5 = data5['Time_Soln#5_(sec)'][i]

k1,i = combustion_time(data6,6)
time6 = data6['Time_Soln#6_(sec)'][i]

k1,i = combustion_time(data7,7)
time7 = data7['Time_Soln#7_(sec)'][i]

k1,i = combustion_time(data8,8)
time8 = data8['Time_Soln#8_(sec)'][i]
##
#k1,i = combustion_time(data9,9)
#time9 = data9['Time_Soln#9_(sec)'][i]
#
#k1,i = combustion_time(data10,10)
#time10 = data10['Time_Soln#10_(sec)'][i]
#
#k1,i = combustion_time(data11,11)
#time11 = data11['Time_Soln#11_(sec)'][i]
#
#k1,i = combustion_time(data12,12)
#time12 = data12['Time_Soln#12_(sec)'][i]
#
#k1,i = combustion_time(data13,13)
#time13 = data13['Time_Soln#13_(sec)'][i]

#time_simplified1.extend([time1,time2,time3,time4,time5,time6,time7,time8,time9,time10,time11,time12])
time_simplified1.extend([time1,time2,time3,time4,time5,time6,time7,time8])
#time_simplified.extend([time1,time2,time3,time4,time5,time6])
#%%
#time_simplified.extend([time1,time2,time3,time4,time5,time6])
path3 = "C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\IC16_simplified"
IC16_file = open(path3+'\CW55.inp',encoding='UTF-8')
lines = IC16_file.readlines()
#%%
import subprocess
path="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\IC16_simplified"
p = subprocess.Popen(path+'\ST.bat',shell=True,stdout=subprocess.PIPE)
out,err = p.communicate()
#%%
import pandas as pd
path2="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\IC16_simplified"
data1 = pd.read_csv(path2+"/CKSoln_solution_no_1.csv")
data2 = pd.read_csv(path2+"/CKSoln_solution_no_2.csv")
data3 = pd.read_csv(path2+"/CKSoln_solution_no_3.csv")
data4 = pd.read_csv(path2+"/CKSoln_solution_no_4.csv")
data5 = pd.read_csv(path2+"/CKSoln_solution_no_5.csv")
data6 = pd.read_csv(path2+"/CKSoln_solution_no_6.csv")
data7 = pd.read_csv(path2+"/CKSoln_solution_no_7.csv")
data8 = pd.read_csv(path2+"/CKSoln_solution_no_8.csv")
data9 = pd.read_csv(path2+"/CKSoln_solution_no_9.csv")
data10 = pd.read_csv(path2+"/CKSoln_solution_no_10.csv")
data11 = pd.read_csv(path2+"/CKSoln_solution_no_11.csv")
data12 = pd.read_csv(path2+"/CKSoln_solution_no_12.csv")
data13 = pd.read_csv(path2+"/CKSoln_solution_no_13.csv")

#求解13个data的着火时间
time_detailed=[]
k1,i = combustion_time(data1,1)
time1 = data1['Time_Soln#1_(sec)'][i]

k1,i = combustion_time(data2,2)
time2 = data2['Time_Soln#2_(sec)'][i]

k1,i = combustion_time(data3,3)
time3 = data3['Time_Soln#3_(sec)'][i]

k1,i = combustion_time(data4,4)
time4 = data4['Time_Soln#4_(sec)'][i]

k1,i = combustion_time(data5,5)
time5 = data5['Time_Soln#5_(sec)'][i]

k1,i = combustion_time(data6,6)
time6 = data6['Time_Soln#6_(sec)'][i]

k1,i = combustion_time(data7,7)
time7 = data7['Time_Soln#7_(sec)'][i]

k1,i = combustion_time(data8,8)
time8 = data8['Time_Soln#8_(sec)'][i]

k1,i = combustion_time(data9,9)
time9 = data9['Time_Soln#9_(sec)'][i]

k1,i = combustion_time(data10,10)
time10 = data10['Time_Soln#10_(sec)'][i]

k1,i = combustion_time(data11,11)
time11 = data11['Time_Soln#11_(sec)'][i]

k1,i = combustion_time(data12,12)
time12 = data12['Time_Soln#12_(sec)'][i]

k1,i = combustion_time(data13,13)
time13 = data13['Time_Soln#13_(sec)'][i]

time_detailed.extend([time1,time2,time3,time4,time5,time6,time7,time8,time9,time10,time11,time12,time13])
print("40atm1.0, T=1000K时，前因子放大10倍后的着火时间：%d",time_detailed[6]*1000000)
print("40atm1.0, T=1200K时，前因子放大10倍后的着火时间：%d" ,time_detailed[10]*1000000)