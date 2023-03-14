#include <Arduino.h>
#include <Wire.h>
#include <SPI.h>

const int readpin=A3;

void setup(){
  Serial.begin(9600);
}
 
void loop(){
  int x=analogRead(readpin);
  float y=(float)x/1023.0;
  Serial.print(y);
  Serial.print('\n'); 
  delay(100);
}

