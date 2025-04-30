#include <Servo.h>
Servo Servo1;
Servo Servo2;

const int sensorPin = 8;
const int servPin1 = 9;
const int servPin2 = 10;

void setup()
{
  pinMode(sensorPin, INPUT);
  Servo1.attach(servPin1);
  Servo2.attach(servPin2);
}

void loop()
{
  int sensorStatus = digitalRead(sensorPin);
  if (sensorStatus == LOW)
  {
    Servo1.write(145);
    Servo2.write(35);
    return 0;
  }
}
