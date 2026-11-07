#include <Servo.h>
//servo stuff
Servo NoEa;
Servo SoEa;
Servo SoWe;
Servo NoWe;
int pos = 0;
const int angleBase = 90;
const int OffM = 60;
//stick (pots in testing) stuff
const int Yaxis = A0;
const int Xaxis = A1;

void setup()
{
  NoEa.attach(3);
  SoEa.attach(5);
  SoWe.attach(6);
  NoWe.attach(9);
}

void loop()
{
  //update read vals
  int YVal = analogRead(Yaxis);
  int XVal = analogRead(Xaxis);
  //set map
  long XX = map(XVal, 0, 1023, -100, 100);
  long YY = map(YVal, 0, 1023, -100, 100);
  
  long offNoWe = -YY + XX;
  long offNoEa = -YY - XX;
  long offSoEa =  YY - XX;
  long offSoWe =  YY + XX;
  
  int angleNoWe = angleBase + map(offNoWe, -200, 200, -OffM, OffM);
  int angleNoEa = angleBase + map(offNoEa, -200, 200, -OffM, OffM);
  int angleSoEa = angleBase + map(offSoEa, -200, 200, -OffM, OffM);
  int angleSoWe = angleBase + map(offSoWe, -200, 200, -OffM, OffM);
  
  NoEa.write(angleNoEa);
  SoEa.write(angleSoEa);
  SoWe.write(angleSoWe);
  NoWe.write(angleNoWe);
  
  delay(50);
}
