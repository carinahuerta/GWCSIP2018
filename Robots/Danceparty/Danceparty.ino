#include <Servo.h>                           // Include servo library

Servo servoLeft;                             // Declare left servo signal
Servo servoRight;                            // Declare right servo signal

int PIEZOPIN = 12;  // Declare pin that the piezo is connected to.

void setup()
{
  pinMode(11, OUTPUT);
  servoLeft.attach(13);                      // Attach left signal to pin 13
  servoRight.attach(12);                     // Attach right signal to pin 12
  servoLeft.writeMicroseconds(0);        // Calibrate left servo
  servoRight.writeMicroseconds(1700);   //backwards
  delay (1000);
  servoLeft.writeMicroseconds (200); //turns right
  servoRight.writeMicroseconds (0);
  delay (1000);
  servoLeft.writeMicroseconds(1700);     //forwards   
  servoRight.writeMicroseconds(0);
  pinMode (6,OUTPUT); 

}

void loop()
{
  // Code for testing servos. 
  // Tinker with the numbers to see how they work!
  // For help, visit https://learn.parallax.com/tutorials/robot/shield-bot/robotics-board-education-shield-arduino/chapter-2-shield-lights-servo-4. 
  //servoLeft.writeMicroseconds(1700);        
  //servoRight.writeMicroseconds(0);
  delay(500);
  tone(11, 622, 500);
  delay(1000);
  tone(11, 700, 500);
  delay (1000);
  tone(11, 500, 500);
  delay(1000);
  tone(11, 650, 500);
  delay (1000);
   digitalWrite (6, HIGH);
   delay (500);
   digitalWrite (6, LOW);
   delay (500); 
}



