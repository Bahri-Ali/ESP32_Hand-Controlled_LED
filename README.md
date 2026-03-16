# ESP32 Hand-Controlled LED

This project allows you to control an LED connected to an ESP32 using hand gestures detected by a camera and Mediapipe.

![Project Screenshot](fc2c7f5e-9e79-4a32-b8ca-e35dc50c9b33.png)

## Features

- **Hand gesture detection** using Python and Mediapipe.
- **Real-time LED control** via serial communication with ESP32.
- **Open/Close hand** controls turning the LED ON/OFF.
- Compatible with PlatformIO for ESP32.

## Hardware

- ESP32 development board
- LED with resistor
- USB cable for programming and power

## Software

- Python 3.x
- OpenCV
- Mediapipe
- PySerial
- PlatformIO (for ESP32 programming)

## Setup

### 1. ESP32 Code
Upload `main.cpp` to your ESP32 using PlatformIO:

```cpp
#include <Arduino.h>

const int ledPin = 23;

void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == '1') digitalWrite(ledPin, HIGH);
    else if (command == '0') digitalWrite(ledPin, LOW);
  }
}
