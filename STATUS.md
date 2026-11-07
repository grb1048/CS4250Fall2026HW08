Current status:
Created a 3d model of a the maze stage to house the maze, frame and servos.
Created a wiring diagram of the servos connected to an Arduino UNO.
Updated wiring diagram to include a mock thumbstick and added +6v supply.
+6v is for the servos and preventing overdraw from the board.
Created initial code for the Arduino UNO with support for servos and input.
Included wiring schematic.
Decided to scrap the thumbstick because this dev board sucks and doesn't have a digital to analog signal converter.
Got an MPU5060 working in a python script to show when tilted but can't get an led to light for some reason.
No matter what I do, it's either I use I2C for the MPU5060 or the LED. It refuses to do both. I've fought for weeks on this and there is no progress.
Included 2test.py for the MPU5060 testing.