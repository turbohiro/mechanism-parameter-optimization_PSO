# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 16:16:09 2018
1.  0.28410760178591277 3190.0751749837323 767276.0387534217
"""
import pandas as pd
from All_data import combustion_time
import matplotlib.pyplot as plt
import numpy as np
import subprocess
from math import sqrt
import os

class PSO:
    def __init__(self):
            self.w = self.getweight()
            self.lr = self.getlearningrate()
            self.maxgen = self.getmaxgen()
            self.sizepop = self.getsizepop()
            self.rangepop_x,self.rangepop_y = self.getrangepop()
            self.rangespeed_x,self.rangespeed_y = self.getrangespeed()

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
        maxgen = 10
        return maxgen

    def getsizepop(self):
        # 种群规模
        sizepop = 40
        return sizepop

    def getrangepop(self):
        # 粒子的位置的范围限制,x、y.z方向的限制相同      ##x,y、z即为我们要设定的参数A,b,E这三个参数的变化区间5e11,2.15e4
        rangepop_x = (-1,1)
        rangepop_y = (-1,1)
        return rangepop_x,rangepop_y

    def getrangespeed(self):
        # 粒子的速度范围限制
        rangespeed_x = (-0.2,0.2)
        rangespeed_y = (-0.2,0.2)
        return rangespeed_x,rangespeed_y
    
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
    def fitness_func(self,data,label=False):
        if(label==True):
            data["simplified2"] = data["simplified"].map(lambda x: x*1000000)
            y=self.Mean_squared_error(list(data["simplified2"]),list(data["detailed"]))
        else:
            data["simplified2"] = data["simplified"].map(lambda x: x*1000000)
            y=self.error(list(data["simplified2"]),list(data["detailed"]))
        
        return y
    
    def init(self,sizepop):  #假设每个粒子只有三个未知数（位置）
        pop = np.zeros((sizepop,2))
        pop_r = np.zeros((sizepop,2))
        v = np.zeros((sizepop,2))
        fitness = np.zeros(sizepop)     #20个粒子，每个粒子都有一定的初始的适应度
        data={}
        data2={}
        data3={}
        data4={}

        for i in range(sizepop):
            #A:5e8--5e11;E:2.15e3--2.15e5
            pop[i] = [(np.random.uniform()-0.5)*2*self.rangepop_x[1],(np.random.uniform()-0.5)*2*self.rangepop_y[1]]   #保证20个粒子的随机位置仍在[-2，2]之间,三个未知数的变化区间不同

            v[i] = [(np.random.uniform()-0.5)*2*self.rangespeed_x[1],(np.random.uniform()-0.5)*2*self.rangespeed_y[1]]
            
            #将参数数据放入IC16_optimized.input文件中
            path3 = "C:\\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\C12_simplified"
            IC16_file = open(path3+'\\NC12.inp')
            lines = IC16_file.readlines()
            IC16_file.close()
            
            pop_r[i][0] = 5000*pop[i][0]+5000
            pop_r[i][1] = 1000**pop[i][1]*1.2e7
            #pop_r[i][0] = (10**pop[i][0]*1.5e5)/np.exp(-pop_r[i][1]/(1.98718*700))
            pop1=str(pop_r[i][0])
            pop2=str(pop_r[i][1])
            
            #a='O2+NC12-QOOH=NC12-OOQOOH	   '+pop1+'  0.0  0.0'
            #b='NC12-QOOH=>NC5H10+CH2O+C2H4+NC4H8+OH    '+pop2+'  0.0  '+pop1
            b='NC12-OOQOOH=>NC12-OQOOH+OH   '+pop2+'  0.0  '+pop1
            #lines[59] = a
            #lines[65] = b
            lines[62] = b

            
            IC16_newfile = open(path3+'\\C12_optimized.inp','w')
            for newline in lines:
                IC16_newfile.write(newline)
            IC16_newfile.close()
            
            ##多目标工况优化：40atm_1.5,40atm_0.5,10atm_0.5,10atm_1.5三种工况的最优值
            #对20atm_1.0工况简化机理进行计算
            path="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\C12_simplified"
            p = subprocess.Popen(path+'\ST.bat',shell=True,stdout=subprocess.PIPE)
            out,err = p.communicate()
            
            time_simplified = self.mechanism_computation(path) 
            #压力20atm,化学当量比0.5
            time_detailed_20atm = [4994.202,1956.661,1520.135,1754.401,2130.096,2729.143,2261.967,1323.475,686.5373,343.5532,173.2118,4.70E+01,1.45E+01]
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
            
            print("第%d个粒子初始化数据完成." %(i))
            
            fitness[i] = self.fitness_func(data[i])
            
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
        pop_r = np.zeros((self.sizepop,2))
        result = np.zeros(self.maxgen)
        data={}
        data2={}
        data3 = {}
        data4={}
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
            #v[v[j][0]<self.rangespeed_x[0]*2.5e11] = self.rangespeed_x[0]
            #v[v[j][1]<self.rangespeed_y[0]*3.5e3] = self.rangespeed_y[0]
            
            #v[v[j][0]>self.rangespeed_x[1]*2.5e11] = self.rangespeed_x[1]
            #v[v[j][1]>self.rangespeed_y[1]*3.5e3] = self.rangespeed_y[1]
                
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
                path3 = "C:\\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\C12_simplified"
                IC16_file = open(path3+'\\NC12.inp')
                lines = IC16_file.readlines()
                IC16_file.close()
                
                pop_r[j][0] = 5000*pop[j][0]+5000
                pop_r[j][1] = 1000**pop[j][0]*1.2e7
                #pop_r[i][0] = (10**pop[i][0]*1.5e5)/np.exp(-pop_r[i][1]/(1.98718*700))
                pop1=str(pop_r[j][0])
                pop2=str(pop_r[j][1])
                
                #a='O2+NC12-QOOH=NC12-OOQOOH	   '+pop1+'  0.0  0.0'
                #b='NC12-QOOH=>NC5H10+CH2O+C2H4+NC4H8+OH    '+pop2+'  0.0  '+pop1
                b='NC12-OOQOOH=>NC12-OQOOH+OH   '+pop2+'  0.0  '+pop1
                #lines[59] = a
                #lines[65] = b
                lines[62] = b
                
                IC16_newfile = open(path3+'\\C12_optimized.inp','w')
                for newline in lines:
                    IC16_newfile.write(newline)
                IC16_newfile.close()
                
#                #对40atm_1.5简化机理进行计算
                path="C:\E_Disk\Ansys_software\ANSYS Chemkin Pro 17.0 Release 15151 Win\workplace\C12_simplified"
                p = subprocess.Popen(path+'\ST.bat',shell=True,stdout=subprocess.PIPE)
                out,err = p.communicate()
                
                time_simplified = self.mechanism_computation(path) 
#                #压力40atm,化学当量比1.5
                time_detailed_20atm = [4994.202,1956.661,1520.135,1754.401,2130.096,2729.143,2261.967,1323.475,686.5373,343.5532,173.2118,4.70E+01,1.45E+01]
                temperature = [700,750,800,850,900,950,1000,1050,1100,1150,1200,1300,1400]
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
                os.remove(path+"/CKSoln_solution_no_9.csv")
                os.remove(path+"/CKSoln_solution_no_10.csv")
                os.remove(path+"/CKSoln_solution_no_11.csv")
                os.remove(path+"/CKSoln_solution_no_12.csv")
                os.remove(path+"/CKSoln_solution_no_13.csv")
    #            
    
                print('第%d次迭代第%d个粒子更新数据完成.' % (i+1,j))
                
                
                fitness[j] = self.fitness_func(data[j])
            for j in range(self.sizepop):
                if fitness[j]<pbestfitness[j]:
                    pbestfitness[j] = fitness[j]
                    pbestpop[j] = pop[j].copy()
                    
            if pbestfitness.min()<gbestfitness:
                gbestfitness = pbestfitness.min()
                gbestpop = pop[pbestfitness.argmin()].copy()
            
            print(gbestfitness,(5000*gbestpop[0]+5000),(1000**gbestpop[1]*1.2e7))
            result[i]= gbestfitness
        
        return result

pso = PSO()
result = pso.run()
#%%
plt.figure()
plt.plot(result)
plt.show()
