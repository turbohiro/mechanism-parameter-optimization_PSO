# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 20:45:14 2019

@author: cwktu
"""

import pandas as pd
from All_data import combustion_time
import matplotlib.pyplot as plt
import numpy as np
import subprocess
from math import sqrt
import os
from scipy import interpolate
from datetime import datetime

class PSO:
    def __init__(self):
            self.w = self.getweight()
            self.lr = self.getlearningrate()
            self.maxgen = self.getmaxgen()
            self.sizepop = self.getsizepop()
            self.rangepop_x,self.rangepop_y,self.rangepop_z = self.getrangepop()
            self.rangespeed_x,self.rangespeed_y,self.rangespeed_z = self.getrangespeed()
            self.temperature1 = [953,968,972,986,1039,1074,1083,1195]   #40atm,1.0
            self.temperature2 = [1033,1053,1086,1129,1169,1279,1350,1394]   #10atm,0.5
            self.temperature3 = [957,1025,1060,1095,1132,1159,1206,1300]  #10atm 1.5

    def getweight(self):
        # 惯性权重
        weight = 0.8
        return weight

    def getlearningrate(self):
        # 分别是粒子的个体和社会的学习因子，也称为加速常数
        lr = (0.495,1.2)
        return lr

    def getmaxgen(self):
        # 最大迭代次数
        maxgen = 15
        return maxgen

    def getsizepop(self):
        # 种群规模
        sizepop = 100
        return sizepop

    def getrangepop(self):
        # 粒子的位置的范围限制,x、y.z方向的限制相同      ##x,y、z即为我们要设定的参数A,b,E这三个参数的变化区间5e11,2.15e4
        rangepop_x = (-1,1)
        rangepop_y = (-1,1)
        rangepop_z = (-1,1)
        return rangepop_x,rangepop_y,rangepop_z

    def getrangespeed(self):
        # 粒子的速度范围限制
        rangespeed_x = (-0.1,0.1)
        rangespeed_y = (-0.1,0.1)
        rangespeed_z = (-0.1,0.1)
        return rangespeed_x,rangespeed_y,rangespeed_z
    
    def error(self,a,b):
        error=[]
        for i in range(len(a)):
            error.append(abs((a[i]-b[i])/b[i]))
        relative_error = sum(error)/len(error)
        return relative_error

    def Mean_squared_error(self,a,b):
        error=[]
        for i in range(len(a)):
            error.append((a[i]-b[i])*(a[i]-b[i]))
        mse = sum(error)/len(error)
        rmse = sqrt(mse)
        return rmse
    

    
    def mechanism_computation(self,path):
        data1 = pd.read_csv(path+"/CKSoln_solution_no_1.csv")
        data2 = pd.read_csv(path+"/CKSoln_solution_no_2.csv")
        data3 = pd.read_csv(path+"/CKSoln_solution_no_3.csv")
        data4 = pd.read_csv(path+"/CKSoln_solution_no_4.csv")
        data5 = pd.read_csv(path+"/CKSoln_solution_no_5.csv")
        data6 = pd.read_csv(path+"/CKSoln_solution_no_6.csv")
        data7 = pd.read_csv(path+"/CKSoln_solution_no_7.csv")
        data8 = pd.read_csv(path+"/CKSoln_solution_no_8.csv")
        
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
    
        time_simplified.extend([time1,time2,time3,time4,time5,time6,time7,time8])
        
        return time_simplified
    
    #计算物种浓度的误差
    def JSR_concentration_error(self,path,status):    #计算物种浓度的误差
        "将ST中得到的CW55转移到JSR中，并计算JSR中CO,H20,CO2的总误差"
        mean_error = 0
        JSR_data = pd.read_csv(path + "/CKSoln_solution_vs_solution_number.csv")
        CO2 = JSR_data[' Mole_fraction_CO2_()']
        CO = JSR_data[' Mole_fraction_CO_()']
        H2O = JSR_data[' Mole_fraction_H2O_()']
        
        CO2_exp = [[1.00E-05,2.31E-04,9.17E-04,0.00169,0.00281,0.004,0.00484,0.00607],[8.00E-06,1.90E-05,1.46E-04,3.43E-04,4.97E-04,6.39E-04,6.90E-04,7.56E-04]]
        CO_exp = [[2.85E-05,0.00184,0.00479,0.00587,0.00628,0.00563,0.00467,0.00351],[7.50E-06,2.18E-04,0.00195,0.00353,0.00441,0.00494,0.00502,0.0051]]
        H2O_exp = [[2.67E-04,0.00235,0.00505,0.00639,0.00763,0.00817,0.0082,0.00837],[1.81E-04,5.36E-04,0.00216,0.00339,0.00399,0.0042,0.004,0.00377]]
        
        CO2_2 = CO2.tolist()
        CO_2 = CO.tolist()
        H2O_2 = H2O.tolist()
        if(status  == 0.5):
            mean_error = (self.error(CO2_2,CO2_exp[0]) + self.error(CO_2,CO_exp[0]) + self.error(H2O_2,H2O_exp[0]))/3
        else:
            mean_error = (self.error(CO2_2,CO2_exp[1]) + self.error(CO_2,CO_exp[1]) + self.error(H2O_2,H2O_exp[1]))/3
        
        return mean_error
    
    #定义适应度函数并实现种群初始化
    def fitness_func(self,data,label=False):
        if(label==True):
            data["simplified2"] = data["simplified"].map(lambda x: x*1000000)
            y=self.Mean_squared_error(list(data["simplified2"]),list(data["detailed"]))
        else:
            data["simplified2"] = data["simplified"].map(lambda x: x*1000000)
            y=self.error(list(data["simplified2"]),list(data["detailed"]))
        
        return y
    
    def init(self,sizepop):  #假设每个粒子只有三个未知数（位置）
        pop = np.zeros((sizepop,3))
        pop_r = np.zeros((sizepop,3))
        v = np.zeros((sizepop,3))
        fitness = np.zeros(sizepop)     #20个粒子，每个粒子都有一定的初始的适应度
        data={}
        data2={}
        data3={}
        data4={}
        data5 = {}
        
        for i in range(sizepop):
            #A:5e8--5e11;E:2.15e3--2.15e5
            pop[i] = [(np.random.uniform()-0.5)*2*self.rangepop_x[1],(np.random.uniform()-0.5)*2*self.rangepop_y[1],(np.random.uniform()-0.5)*2*self.rangepop_z[1]]   #保证20个粒子的随机位置仍在[-2，2]之间,三个未知数的变化区间不同
           
            v[i] = [(np.random.uniform()-0.5)*2*self.rangespeed_x[1],(np.random.uniform()-0.5)*2*self.rangespeed_y[1],(np.random.uniform()-0.5)*2*self.rangespeed_z[1]]
            
            #将参数数据放入IC16_optimized.input文件中
            path3 = "C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\IC16_simplified"
            IC16_file = open(path3+'\CW54.inp',encoding='UTF-8')
            lines = IC16_file.readlines()
            IC16_file.close()
            
            pop_r[i][0] = 10**pop[i][0]*8e12   #JSR对抗反应中缓慢反应的系数 
            pop_r[i][1] = 50**pop[i][1]*8.62e5
            pop_r[i][2] = 50**pop[i][2]*4e13
           
            
            pop1=str(pop_r[i][0])
            pop2=str(pop_r[i][1])
            pop3=str(pop_r[i][2])
            
            
            a = 'HO2+iC4H7=>CH2O+CH3COCH3      ' + pop1 + '    0.0  0.0E0' 
            b = 'IC16H34+HO2=>H2O2+IC16H33       ' + pop2 + '    2.000     11887.73 '
            c = 'IC16H33=>iC4H8+2C2H4+DC8H17     ' + pop3 + '    0.000     29000.00'
            
            
            lines[465] = c
            lines[461] = b
            lines[414] = a
            
            IC16_newfile = open(path3+'\CW55.inp','w',encoding='UTF-8')
            for newline in lines:
                IC16_newfile.write(newline)
            IC16_newfile.close()
            
            path4 = "C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\JSR_IC16"
            JSR16_newfile = open(path4+'\CW55.inp','w',encoding='UTF-8')
            for newline in lines:
                JSR16_newfile.write(newline)
            JSR16_newfile.close()
            
            ##多目标工况优化：40atm_1.5,40atm_0.5,10atm_0.5,10atm_1.5三种工况的最优值
#            对20atm_1.0工况简化机理进行计算
            path="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\IC16_simplified"
            p = subprocess.Popen(path+'\ST_high_1.bat',shell=True,stdout=subprocess.PIPE)
            out,err = p.communicate()
            
            time_simplified = self.mechanism_computation(path) 

            #压力40atm,化学当量比1.0
            time_detailed_20atm = [1151.670483,906.728824,666.4479367,645.1824505,248.8656125,140.928986,127.2535978,44.60056861]
            temperature = self.temperature1
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

            
            #压力10atm,化学当量比0.5
            path="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\IC16_simplified"
            p = subprocess.Popen(path+'\ST_high_2.bat',shell=True,stdout=subprocess.PIPE)
            out,err = p.communicate()
            
            time_simplified = self.mechanism_computation(path) 
            time_detailed_20atm = [1400.609017,1078.035022,729.2187811,477.1796207,296.8906564,131.0479985,70.65109065,55.94778429]
            temperature = self.temperature2
            Ignition_time = {"Temp":temperature,"simplified":time_simplified,"detailed":time_detailed_20atm}
            data2[i] = pd.DataFrame(Ignition_time)
            os.remove(path+"/CKSoln_solution_no_1.csv")
            os.remove(path+"/CKSoln_solution_no_2.csv")
            os.remove(path+"/CKSoln_solution_no_3.csv")
            os.remove(path+"/CKSoln_solution_no_4.csv")
            os.remove(path+"/CKSoln_solution_no_5.csv")
            os.remove(path+"/CKSoln_solution_no_6.csv")
            os.remove(path+"/CKSoln_solution_no_7.csv")
            os.remove(path+"/CKSoln_solution_no_8.csv")

            
            #压力10atm,化学当量比1.5
            path="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\IC16_simplified"
            p = subprocess.Popen(path+'\ST_high_3.bat',shell=True,stdout=subprocess.PIPE)
            out,err = p.communicate()
            
            time_simplified = self.mechanism_computation(path)
            time_detailed_20atm = [1970.158462,777.7193035,528.8228692,426.2059505,263.727987,255.0080316,164.9708062,98.88140227]
            temperature = self.temperature3
            Ignition_time = {"Temp":temperature,"simplified":time_simplified,"detailed":time_detailed_20atm}
            data3[i] = pd.DataFrame(Ignition_time)
            os.remove(path+"/CKSoln_solution_no_1.csv")
            os.remove(path+"/CKSoln_solution_no_2.csv")
            os.remove(path+"/CKSoln_solution_no_3.csv")
            os.remove(path+"/CKSoln_solution_no_4.csv")
            os.remove(path+"/CKSoln_solution_no_5.csv")
            os.remove(path+"/CKSoln_solution_no_6.csv")
            os.remove(path+"/CKSoln_solution_no_7.csv")
            os.remove(path+"/CKSoln_solution_no_8.csv")
            
            ##定义值得得到计算JSR误差的函数  JSR0.5
            path="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\JSR_IC16"
            p = subprocess.Popen(path+'\JSR_0.5.bat',shell=True,stdout=subprocess.PIPE)
            out,err = p.communicate()
            
            data4[i] = self.JSR_concentration_error(path,0.5)
            os.remove(path+"/CKSoln_solution_vs_solution_number.csv")
            
            #
            path="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\JSR_IC16"
            p = subprocess.Popen(path+'\JSR_2.0.bat',shell=True,stdout=subprocess.PIPE)
            out,err = p.communicate()
            
            data5[i] = self.JSR_concentration_error(path,2.0)
            os.remove(path+"/CKSoln_solution_vs_solution_number.csv")


##
            print("第%d个粒子初始化数据完成." %(i))
            
            fitness[i] = (self.fitness_func(data[i]) + self.fitness_func(data2[i]) +self.fitness_func(data3[i]) + 2*(data4[i] + data5[i]))/5    #得到30个初始化粒子的简化机理着火时间数据后，与详细机理的着火时间数据进行比较，得到适应度
            #fitness[i] = self.fitness_func(data[i])
            
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
        pop_r = np.zeros((self.sizepop,3))
        result = np.zeros(self.maxgen)
        data={}
        data2={}
        data3 = {}
        data4={}
        data5 = {}
        for i in range(self.maxgen):
            #速度更新
            for j in range(self.sizepop):
                v[j] =v[j]*self.w + self.lr[0]*np.random.rand()*(pbestpop[j]-pop[j])+self.lr[1]*np.random.rand()*(gbestpop-pop[j])##不使用固定权重，加了一个[0,1]之间随机变化的权重
                if v[j][0]<self.rangespeed_x[0]:
                    v[j][0] = self.rangespeed_x[0]
                if v[j][1]<self.rangespeed_y[0]:
                    v[j][1] = self.rangespeed_y[0]
                if v[j][0]>self.rangespeed_x[1]:
                    v[j][0] = self.rangespeed_x[1]
                if v[j][1]>self.rangespeed_y[1]:
                    v[j][1] = self.rangespeed_y[1]

            #位置更新
            for j in range(self.sizepop):
                pop[j] += v[j]
                if pop[j][0]<self.rangepop_x[0]:
                    pop[j][0] = self.rangepop_x[0]
                if pop[j][1]<self.rangepop_y[0]:
                    pop[j][1] = self.rangepop_y[0]
                if pop[j][0]>self.rangepop_x[1]:
                    pop[j][0] = self.rangepop_x[1]
                if pop[j][1]>self.rangepop_y[1]:
                    pop[j][1] = self.rangepop_x[1]
            
            #适应度更新
          #将参数数据放入IC16_optimized.input文件中
            for j in range(self.sizepop):
                path3 = "C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\IC16_simplified"
                IC16_file = open(path3+'\CW54.inp',encoding='UTF-8')
                lines = IC16_file.readlines()
                IC16_file.close()
                
                pop_r[j][0] = 10**pop[j][0]*8e12   #JSR对抗反应中缓慢反应的系数 
                pop_r[j][1] = 50**pop[j][1]*8.62e5
                pop_r[j][2] = 50**pop[j][2]*4e13
               
                
                pop1=str(pop_r[j][0])
                pop2=str(pop_r[j][1])
                pop3=str(pop_r[j][2])
                
                
                a = 'HO2+iC4H7=>CH2O+CH3COCH3      ' + pop1 + '    0.0  0.0E0' 
                b = 'IC16H34+HO2=>H2O2+IC16H33       ' + pop2 + '    2.000     11887.73 '
                c = 'IC16H33=>iC4H8+2C2H4+DC8H17     ' + pop3 + '    0.000     29000.00'
                
                
                lines[465] = c
                lines[461] = b
                lines[414] = a
                            
                
                IC16_newfile = open(path3+'\CW55.inp','w',encoding='UTF-8')
                for newline in lines:
                    IC16_newfile.write(newline)
                IC16_newfile.close()
                
                path4 = "C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\JSR_IC16"
                JSR16_newfile = open(path4+'\CW55.inp','w',encoding='UTF-8')
                for newline in lines:
                    JSR16_newfile.write(newline)
                JSR16_newfile.close()
                
                
    #                #压力10atm,化学当量比2.0
                path="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\IC16_simplified"
                p = subprocess.Popen(path+'\ST_high_1.bat',shell=True,stdout=subprocess.PIPE)
                out,err = p.communicate()
                
                time_simplified = self.mechanism_computation(path) 
    
                #压力40atm,化学当量比1.0
                time_detailed_20atm = [1151.670483,906.728824,666.4479367,645.1824505,248.8656125,140.928986,127.2535978,44.60056861]
                temperature = self.temperature1
                Ignition_time = {"Temp":temperature,"simplified":time_simplified,"detailed":time_detailed_20atm}
                data[j] = pd.DataFrame(Ignition_time)
                os.remove(path+"/CKSoln_solution_no_1.csv")
                os.remove(path+"/CKSoln_solution_no_2.csv")
                os.remove(path+"/CKSoln_solution_no_3.csv")
                os.remove(path+"/CKSoln_solution_no_4.csv")
                os.remove(path+"/CKSoln_solution_no_5.csv")
                os.remove(path+"/CKSoln_solution_no_6.csv")
                os.remove(path+"/CKSoln_solution_no_7.csv")
                os.remove(path+"/CKSoln_solution_no_8.csv")
    
                
                #压力10atm,化学当量比0.5
                path="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\IC16_simplified"
                p = subprocess.Popen(path+'\ST_high_2.bat',shell=True,stdout=subprocess.PIPE)
                out,err = p.communicate()
                
                time_simplified = self.mechanism_computation(path) 
                time_detailed_20atm = [1400.609017,1078.035022,729.2187811,477.1796207,296.8906564,131.0479985,70.65109065,55.94778429]
                temperature = self.temperature2
                Ignition_time = {"Temp":temperature,"simplified":time_simplified,"detailed":time_detailed_20atm}
                data2[j] = pd.DataFrame(Ignition_time)
                os.remove(path+"/CKSoln_solution_no_1.csv")
                os.remove(path+"/CKSoln_solution_no_2.csv")
                os.remove(path+"/CKSoln_solution_no_3.csv")
                os.remove(path+"/CKSoln_solution_no_4.csv")
                os.remove(path+"/CKSoln_solution_no_5.csv")
                os.remove(path+"/CKSoln_solution_no_6.csv")
                os.remove(path+"/CKSoln_solution_no_7.csv")
                os.remove(path+"/CKSoln_solution_no_8.csv")
    
                
                #压力10atm,化学当量比1.5
                path="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\IC16_simplified"
                p = subprocess.Popen(path+'\ST_high_3.bat',shell=True,stdout=subprocess.PIPE)
                out,err = p.communicate()
                
                time_simplified = self.mechanism_computation(path)
                time_detailed_20atm = [1970.158462,777.7193035,528.8228692,426.2059505,263.727987,255.0080316,164.9708062,98.88140227]
                temperature = self.temperature3
                Ignition_time = {"Temp":temperature,"simplified":time_simplified,"detailed":time_detailed_20atm}
                data3[j] = pd.DataFrame(Ignition_time)
                os.remove(path+"/CKSoln_solution_no_1.csv")
                os.remove(path+"/CKSoln_solution_no_2.csv")
                os.remove(path+"/CKSoln_solution_no_3.csv")
                os.remove(path+"/CKSoln_solution_no_4.csv")
                os.remove(path+"/CKSoln_solution_no_5.csv")
                os.remove(path+"/CKSoln_solution_no_6.csv")
                os.remove(path+"/CKSoln_solution_no_7.csv")
                os.remove(path+"/CKSoln_solution_no_8.csv")
#                
                print('第%d次迭代第%d个粒子更新数据完成.' % (i+1,j))
                
               ##定义值得得到计算JSR误差的函数  JSR0.5
                path="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\JSR_IC16"
                p = subprocess.Popen(path+'\JSR_0.5.bat',shell=True,stdout=subprocess.PIPE)
                out,err = p.communicate()
                
                data4[j] = self.JSR_concentration_error(path,0.5)
                os.remove(path+"/CKSoln_solution_vs_solution_number.csv")
                
                #
                path="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\JSR_IC16"
                p = subprocess.Popen(path+'\JSR_2.0.bat',shell=True,stdout=subprocess.PIPE)
                out,err = p.communicate()
                
                data5[j] = self.JSR_concentration_error(path,2.0)
                os.remove(path+"/CKSoln_solution_vs_solution_number.csv")
                #fitness[j] = self.fitness_func(data[j]) 
                fitness[j] = (self.fitness_func(data[j]) + self.fitness_func(data2[j]) +self.fitness_func(data3[j]) + 2*(data4[j] + data5[j]))/5
            for j in range(self.sizepop):
                if fitness[j]<pbestfitness[j]:
                    pbestfitness[j] = fitness[j]
                    pbestpop[j] = pop[j].copy()
                    
            if pbestfitness.min()<gbestfitness:
                gbestfitness = pbestfitness.min()
                gbestpop = pop[pbestfitness.argmin()].copy()
            
            print(gbestfitness,(10**gbestpop[0]*8e12),(50**gbestpop[1]*8.62e5),(50**gbestpop[2]*4e13))
            
            #输出到txt文件保存
            f = open('Result.txt','a')
            date="{:%Y-%m-%d_%H_%M___}".format(datetime.now())
            content = str(gbestfitness) + '__' + str(10**gbestpop[0]*8e12) + '__' + str(50**gbestpop[1]*8.62e5) + '__' + str(50**gbestpop[2]*4e13)
            new_con = date + content  +'\n'
            f.write(new_con)
            f.close()
            
            result[i]= gbestfitness
        
        return result

pso = PSO()
result = pso.run()