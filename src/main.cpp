#include <Arduino.h>

const int ledPin = 23;

void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    Serial.println(command);
    if (command == '1') {       
      digitalWrite(ledPin, HIGH);
    } 
    else if (command == '0') { 
      digitalWrite(ledPin, LOW);
    }
  }
}
