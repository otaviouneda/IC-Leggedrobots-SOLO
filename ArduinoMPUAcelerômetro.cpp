#include <Arduino.h>
#include <MPU9250.h>
#include <Wire.h>

MPU9250 IMU(Wire,0x68);


void setup() {
  Serial.begin(9600);
  IMU.begin();
}

void loop() {
  IMU.readSensor();
  Serial.print(IMU.getAccelY_mss(), 6);
  Serial.print('\n');
  delay(100);
}
