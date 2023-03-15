#Leitura serial dos valores do acelerômetro enviado pelo arduino
import serial
import time 
import matplotlib.pyplot as plt
import numpy as np
import struct


arduino=serial.Serial('COM4',9600,timeout=1)
x=np.linspace(0,1,100)
dados=[]
time.sleep(2)


for i in range(103):
    line = (arduino.readline())
    string=line.decode()
    stripped_string=string.strip()
    if stripped_string=='':
        stripped_string='0.00'
        num_float=float(stripped_string)
    else:
        num_float=float(stripped_string)
    #print(num_float+9.9)
    dados.append(num_float+9.9) #retira o valor inicial para começar no marco 0

plt.plot(x,dados[3:103]) #o sensor leva 3 iterações para ser calibrado e essas leituras podem ser desconsideradas
plt.yscale('linear') 
plt.grid(True)
plt.ylim(-10,10)
plt.xscale('linear')
plt.ylabel('Aceleração (m/s^2)')
plt.title('Leitura MPU Acelerômetro')
plt.show()
arduino.close()
