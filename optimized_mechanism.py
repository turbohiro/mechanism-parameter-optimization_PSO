# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 14:35:38 2018

@author: cwktu
"""
from math import sqrt
#1.创建适应度函数RMSE或dice coefficient;其中a,b均为集合,a为简化机理预测值，b为详细机理实际值
def dice_coefficient(a, b):
    """dice coefficient 2nt/na + nb."""
    a_bigrams = set(a)
    b_bigrams = set(b)
    overlap = len(a_bigrams & b_bigrams)
    return 1-(overlap * 2.0/(len(a_bigrams) + len(b_bigrams)))

def error(a,b):
    error=[]
    for i in range(len(a)):
        error.append(a[i]-b[i])
    me = abs(sum(error)/len(error))
    return me

def Mean_squared_error(a,b):
    error=[]
    for i in range(len(a)):
        error.append((a[i]-b[i])*(a[i]-b[i]))
    mse = sum(error)/len(error)
    rmse = sqrt(mse)
    return rmse

a=[17095.64,5173.39,2402.288,1772.75,1734.265,1750.991,1369.507,729.579,347.7536,167.2902,85.36655,28.50332,12.82532]
b=[17520.84,5256.147,2392.014,1708.796,1622.097,1645.656,1241.479,667.9609,329.3767,163.8509,85.25904,27.75821,11.70666]

print(error(a,b))
#print(dice_coefficient(a,b))
print(Mean_squared_error(a,b))

#%%
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
    elif m==14:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#14_(sec)'][i]
            timex2 = data['Time_Soln#14_(sec)'][i+1]
            tempy1 = data[' Pressure_Soln#14_(dyne/cm2)'][i]
            tempy2 = data[' Pressure_Soln#14_(dyne/cm2)'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i
    elif m==15:
        for i in range(len(data)-1):
            timex1 = data['Time_Soln#15_(sec)'][i]
            timex2 = data['Time_Soln#15_(sec)'][i+1]
            tempy1 = data[' Pressure_Soln#15_(dyne/cm2)'][i]
            tempy2 = data[' Pressure_Soln#15_(dyne/cm2)'][i+1]
            k = (tempy2-tempy1)/(timex2-timex1)
            if  k>slope_max:
                slope_max = k
                time= i

    return slope_max,time
#%%读取bat文件，并得到简化机理随着温度变化的着火时间数据  条件：40atm_当量比1.5--->time为简化机理结果列表
import subprocess
path="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\C18H34O2"
p = subprocess.Popen(path+'\ST.bat',shell=True,stdout=subprocess.PIPE)
out,err = p.communicate()
#%%
import pandas as pd
#from All_data import combustion_time
#path="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\C12_simplified"
path="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\C18H34O2"

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
data14 = pd.read_csv(path+"/CKSoln_solution_no_14.csv")
data15 = pd.read_csv(path+"/CKSoln_solution_no_15.csv")
#求解13个data的着火时间

time_simplified=[]
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

k1,i = combustion_time(data14,14)
time14 = data14['Time_Soln#14_(sec)'][i]

k1,i = combustion_time(data15,15)
time15 = data15['Time_Soln#15_(sec)'][i]

time_simplified.extend([time1,time2,time3,time4,time5,time6,time7,time8,time9,time10,time11,time12,time13,time14,time15])
#%%同理，可得到详细机理随着温度变化的着火时间数据  条件：40atm_当量比1.5
import subprocess
import pandas as pd
from All_data import combustion_time

path2="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\C12_detailed"
p = subprocess.Popen(path2+'\ST.bat',shell=True,stdout=subprocess.PIPE)
out,err = p.communicate()
#%%
path2="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\C12_detailed"
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
#%%融合三列数据
temperature = [700,750,800,850,900,950,1000,1050,1100,1150,1200,1300,1400]
Ignition_time = {"Temp":temperature,"simplified":time_simplified,"detailed":time_detailed}
data = pd.DataFrame(Ignition_time)
#%%对数据进行绘图对比分析
import matplotlib.pyplot as plt
import numpy as np

data["Temp2"]=data["Temp"].map(lambda x: 1000/x)
data["simplified2"] = data["simplified"].map(lambda x: x*1000000)
data["detailed2"] = data["detailed"].map(lambda x: x*1000000)

plt.plot(data["Temp2"],data["simplified2"],color='red',linestyle='--',label='chem299')
plt.plot(data["Temp2"],data["detailed2"],color='green',label='detailed')

plt.yscale('log')
plt.xlim((0.5,1.5))
plt.ylim((10,100000))
plt.xlabel('1000/T')
plt.ylabel('Ignition delay time(us)')
plt.legend(loc='lower right')
plt.title("40atm_$\phi$=1.5'")

print(Mean_squared_error(data["simplified2"],data["detailed2"]))
print(error(data["simplified2"],data["detailed2"]))
#%%开始算法优化
#算法参数设定
class PSO:
    def __init__(self):
            self.w = self.getweight()
            self.lr = self.getlearningrate()
            self.maxgen = self.getmaxgen()
            self.sizepop = self.getsizepop()
            self.rangepop_x,self.rangepop_y,self.rangepop_z = self.getrangepop()
            self.rangespeed_x,self.rangespeed_y,self.rangespeed_z = self.getrangespeed()

    def getweight(self):
        # 惯性权重
        weight = 1
        return weight

    def getlearningrate(self):
        # 分别是粒子的个体和社会的学习因子，也称为加速常数
        lr = (0.49445,1.49445)
        return lr

    def getmaxgen(self):
        # 最大迭代次数
        maxgen = 300
        return maxgen

    def getsizepop(self):
        # 种群规模
        sizepop = 20
        return sizepop

    def getrangepop(self):
        # 粒子的位置的范围限制,x、y.z方向的限制相同      ##x,y、z即为我们要设定的参数A,b,E这三个参数的变化区间
        rangepop_x = (-2,2)
        rangepop_y = (-2,2)
        rangepop_z = (-2,2)
        return rangepop_x,rangepop_y,rangepop_z

    def getrangespeed(self):
        # 粒子的速度范围限制
        rangespeed_x = (-0.5,0.5)
        rangespeed_y = (-0.5,0.5)
        rangespeed_z = (-0.5,0.5)
        return rangespeed_x,rangespeed_y,rangespeed_z
        
    #定义适应度函数并实现种群初始化
    def fitness_func(self,data,label=True):
        '''x为集合，即输入的粒子位置（即参数的变化区间）
        '''
        if(label==True):
            y=Mean_squared_error(data["simplified2"],data["detailed2"])
        else:
            y=error(data["simplified2"],data["detailed2"])
        
        return y
    
    def init(self,sizepop):  #假设每个粒子只有三个未知数（位置）
        pop = np.zeros((sizepop,3))
        v = np.zeros((sizepop,3))
        fitness = np.zeros(sizepop)     #20个粒子，每个粒子都有一定的初始的适应度
        
        for i in range(sizepop):
            pop[i] = [(np.random.rand()-0.5)*self.rangepop_x[0]*2,(np.random.rand()-0.5)*self.rangepop_y[1]*2,(np.random.rand()-0.5)*self.rangepop_z[0]*2]   #保证20个粒子的随机位置仍在[-2，2]之间,三个未知数的变化区间不同
            v[i] = [(np.random.rand()-0.5)*self.rangespeed_x[0]*2,(np.random.rand()-0.5)*self.rangespeed_y[1]*2,(np.random.rand()-0.5)*self.rangespeed_z[1]*2]
            """
            将初始化的20个粒子的位置和速度值代入简化机理反应式中，得出data
            path3 = "C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\IC16_simplified"
            IC16_file = open(path3+'\IC16.inp')
            lines = IC16_file.readlines()
            IC16_file.close()
            
            pop1=str(pop[i][0])
            pop2=str(pop[i][1])
            pop3=str(pop[i][2])
            
            a='O2+IC16H33=>2IC8H16+HO2    '+pop1+' '+ pop2+' '+pop3
            lines[52] = a
            
            IC16_newfile = open(path3+'\IC16_optimized.inp','w')
            for newline in lines:
                IC16_newfile.write(newline)
            
            IC16_newfile.close()
            """
            fitness[i] = self.fitness_func(data[i])    #得到20个初始化粒子的简化机理着火时间数据后，与详细机理的着火时间数据进行比较，得到适应度
        
        return pop,v,fitness
    
    #寻找初始化后的极值
    def getinitbest(self,fitness,pop):
        #群体最优的粒子位置和适应度值;;寻找最小值，使得适应度函数最小
        gbestpop,gbestfitness = pop[fitness.argmin()].copy(),fitness.min()
        
        #个体最优的粒子位置及其适应度值
        pbestpop,pbestfitness = pop.copy(),fitness.copy()
        
        return gbestpop,gbestfitness,pbestpop,pbestfitness
        
    
    #迭代寻优
    def run(self):
        pop,v,fitness = self.init(self.sizepop)
        gbestpop,gbestfitness,pbestpop,pbestfitness = self.getinitbest(fitness,pop)
        
        result = np.zeros(self.maxgen)
        for i in range(self.maxgen):
            #速度更新
            for j in range(self.sizepop):
                v[j] = v[j]*self.w +self.lr[0]*np.random.rand()*(pbestpop[j]-pop[j])+self.lr[1]*np.random.rand()*(gbestpop-pop[j])##不使用固定权重，加了一个[0,1]之间随机变化的权重
            v[v[j][0]<self.rangespeed_x[0]] = self.rangespeed_x[0]
            v[v[j][1]<self.rangespeed_y[0]] = self.rangespeed_y[0]
            v[v[j][2]<self.rangespeed_z[0]] = self.rangespeed_z[0]
            
            v[v[j][0]>self.rangespeed_x[1]] = self.rangespeed_x[1]
            v[v[j][1]>self.rangespeed_y[1]] = self.rangespeed_y[1]
            v[v[j][2]>self.rangespeed_z[1]] = self.rangespeed_z[1]
                
            #位置更新
            for j in range(self.sizepop):
                pop[j] +=0.5*v[j]
            pop[pop[j][0]<self.rangepop_x[0]] = self.rangepop_x[0]
            pop[pop[j][1]<self.rangepop_y[0]] = self.rangepop_y[0]
            pop[pop[j][2]<self.rangepop_z[0]] = self.rangepop_z[0]
            
            pop[pop[j][0]>self.rangepop_x[1]] = self.rangepop_x[1]
            pop[pop[j][1]>self.rangepop_y[1]] = self.rangepop_y[1]
            pop[pop[j][2]>self.rangepop_z[1]] = self.rangepop_z[1]
            
            #适应度更新
        """
        将更新后的20个粒子的位置和速度值代入简化机理反应式中，得出data
        """
            for j in range(self.sizepop):
                fitness[j] = self.fitness_func(data[j])
            
            for j in range(self.sizepop):
                if fitness[j]<pbestfitness[j]:
                    pbestfitness[j] = fitness[j]
                    pbestpop[j] = pop[j].copy()
            if pbestfitness.min()<gbestfitness:
                gbestfitness = pbestfitness.min()
                gbestpop = pop[pbestfitness.argmin()].copy()
                print(gbestfitness,gbestpop)
            
            result[i]= gbestfitness
        
        return result

#%%
import matplotlib.pyplot as plt
import numpy as np

pso = PSO()
result = pso.run()
plt.figure()
plt.plot(result)
plt.show()
#%%修改IC16.inp文件
path3 = "C:\\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\C12_simplified"
IC16_file = open(path3+'\\NC12.inp')
lines = IC16_file.readlines()
#%%
IC16_file.close()

pop1=str(2.5)
pop2=str(0.0)
pop3=str(3.5E3)

a='O2+NC12-QOOH=NC12-OOQOOH	   '+pop1+' 0.0  0.0'
b='NC12-QOOH=>NC5H10+CH2O+C2H4+NC4H8+OH    '+pop2+' 0.0 1.41E4'
lines[59] = a
lines[65] = b

IC16_newfile = open(path3+'\\C12_optimized.inp','w')
for newline in lines:
    IC16_newfile.write(newline)

IC16_newfile.close()

#%%
import pandas as pd
data={}
d1 = {'col1': [1, 2], 'col2': [3, 4]}
d2 = {'col1': [1, 2], 'col2': [3, 4]}
d3 = {'col1': [1, 2], 'col2': [3, 4]}
data[1] = pd.DataFrame(d1)
data[2] = pd.DataFrame(d2)
data[3] = pd.DataFrame(d3)
#
#import matplotlib.pyplot as plt
#plt((data[1].col1).tolist(),(data[1].col2).tolist())
x=list(data[1]['col1'])
plt.plot(list(data[1]['col1']),list(data[1]['col2']))


#%%
rangespeed_x = (-0.2,0.2)
rangespeed_y = (-0.2,0.2)
rangepop_x = (-1,1)
rangepop_y = (-1,1)
sizepop =500
pop = np.zeros((sizepop,2))
pop_r = np.zeros((sizepop,2))
v = np.zeros((sizepop,2))
fitness = np.zeros(sizepop)     #20个粒子，每个粒子都有一定的初始的适应度
data={}

for i in range(500):
    #A:5e8--5e11;E:2.15e3--2.15e5
    pop[i] = [(np.random.uniform()-0.5)*2*rangepop_x[1],(np.random.uniform()-0.5)*2*rangepop_y[1]]   #保证20个粒子的随机位置仍在[-2，2]之间,三个未知数的变化区间不同

    v[i] = [(np.random.uniform()-0.5)*2*rangespeed_x[1],(np.random.uniform()-0.5)*2*rangespeed_y[1]]
    
    # 加载svm.pickle
    with open('svm.pickle', 'rb') as fr:
        new_svm = pickle.load(fr)
        pop_new = pop[i].tolist()
        data[i]=new_svm.predict(pop_new)
#            
    print("第%d个粒子初始化数据完成." %(i))
#%%
data = list(data.values())
#%%
pop = pop.tolist()
#%%
k=[]
E=[]
for i in range(500):
    k.append(pop[i][0])
    E.append(pop[i][1])
Data = {"fitness":data,"k":k,"E":E}
Data = pd.DataFrame(Data)
Data.to_csv("data.csv")















