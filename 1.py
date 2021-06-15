#1090752
import matplotlib.pyplot as plt
from math import e
import numpy as np
def d_dt(t, y):
    dydt = np.zeros(len(y))
    for i in range(1,len(t)-1):
        dt = t[i+1] - t[i-1]
        dydt[i] = (y[i+1] - y[i-1]) / dt
    dydt = np.delete(dydt, [0, len(dydt)-1])
    return (t[1 : len(t) - 1],dydt)

def smooth(t, y):
    ysm = np.zeros(len(y))
    for i in range(2, len(t)-2):
        ysm[i] = (y[i-2] + 2*y[i-1] + 2*y[i] + 2*y[i] + 2*y[i+1] + 2*y[i+2]) / 8.0
    ysm = np.delete(ysm, [0,1,len(y)-2, len(y)-1])
    return (t[2:len(t)-2],ysm)

name = str(input("請輸入資料檔的檔名： \n"))
file = open(name,"r")
counter = 0
rate = 10000
r = 10e3
c = 100e-6
tc = 1.0 / (r * c * rate)
x_lst = []
y_lst = []
t_lst = []

for i in file:
    counter += 1
    i = i.strip()
    i_sp = i.split('\t')
    if counter == 1:
        header = i_sp
    else:
        x_lst.append(float(i_sp[0]))
        y_lst.append(float(i_sp[1]))
        
for n in range(len(x_lst)):
    t = n / rate
    t_lst.append(t)
        

sum = 0.0
for i in range(len(t_lst)):
    sum += t_lst[i]
    
tau = round( sum / len(t_lst), 4 )

print("tau: ",tau)
        
x = np.array(x_lst)
y = np.array(y_lst)
s_y, s_x = smooth(y, x)
new_y, new_x = d_dt(s_y, s_x)


file.close()
plt.figure()

plt.xlabel(header[0])
plt.ylabel(header[1])
plt.plot(x, y)

plt.show()


