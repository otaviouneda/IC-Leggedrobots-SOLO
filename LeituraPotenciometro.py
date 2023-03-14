#Teste Python Potenciômetro de corda

import serial
import time 
import matplotlib.pyplot as plt
import numpy as np
import struct


arduino=serial.Serial('COM4',9600,timeout=1)
x=np.linspace(0,1,100)
dados=[]

time.sleep(2)
for i in range(100):
    line = (arduino.readline())
    string=line.decode()
    stripped_string=string.strip()
    if stripped_string=='':
        stripped_string='0.00'
        num_float=float(stripped_string)
    else:
        num_float=float(stripped_string) 
    #print(num_float)
    print(num_float)
    dados.append(1.156-num_float) #A altura do chão até a base do potenciômetro é 115.6 cm

plt.plot(x,dados)
plt.grid(True)
plt.ylim(0,1.156)
plt.yscale('linear')
plt.xscale('linear')
plt.ylabel('Altura(m)')
plt.title('Leitura potenciômetro de corda ')
plt.show()
arduino.close()
  
 