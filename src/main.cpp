#include <Arduino.h>

const int ledPinGreen = 23;
const int ledPinRed = 22;
void setup() {
  Serial.begin(115200);
  pinMode(ledPinGreen, OUTPUT);
  pinMode(ledPinRed, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    Serial.println(command);
    if (command == '0') {       
      digitalWrite(ledPinGreen, HIGH);
      digitalWrite(ledPinRed, LOW);
    } 
    else if (command == '1') { 
      digitalWrite(ledPinGreen, LOW);
      digitalWrite(ledPinRed, HIGH);
    }
  }
}
