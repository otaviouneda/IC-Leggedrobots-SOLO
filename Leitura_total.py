#Libraries
import serial
import time 
import matplotlib.pyplot as plt
import numpy as np
import struct

#
arduino=serial.Serial('COM4',9600,timeout=1)
x=np.linspace(0,1,200)
dados1=[]
dados2=[]
time.sleep(2)



for i in range(203):
    read_data=arduino.readline().decode('ascii')
    if read_data!=(''):
        print(read_data)
        new=read_data.split(",")
        read_data1=float(new[0])
        read_data2=float(new[1])
        dados1.append(1.156-read_data1)
        dados2.append(-(9.9+read_data2))
    else:
        i=i-1



plt.plot(20*x,dados1[0:203]) #o sensor leva 3 iterações para ser calibrado e essas leituras podem ser desconsideradas
plt.yscale('linear') 
plt.grid(True)
plt.ylim(0,1.156)
plt.xscale('linear')
plt.ylabel('Altura (m)',fontsize=17)
plt.xlabel('Tempo(s)',fontsize=17)
plt.title('Leitura Potenciômetro de corda',fontsize=17)
plt.show()
arduino.close()

plt.plot(20*x,dados2[0:203]) #o sensor leva 3 iterações para ser calibrado e essas leituras podem ser desconsideradas
plt.yscale('linear') 
plt.grid(True)
plt.ylim(-15,15)
plt.xscale('linear')
plt.ylabel('Aceleração (m/s^2)',fontsize=17)
plt.xlabel('Tempo(s)',fontsize=17)
plt.title('Leitura MPU Acelerômetro',fontsize=17)
plt.show()
arduino.close() 
