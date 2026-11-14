#include <Arduino_Modulino.h>
ModulinoThermo thermo;

float tempC = 0;  // temp in Celsius
float tempF = 0;  // temp in Fahrenheit
float humidity = 0;

void setup() {  // runs once
  Modulino.begin(); // connects to the modulino
  thermo.begin();
  Serial.begin(9600);
}

void loop() { // runs continously
  tempC = thermo.getTemperature(); // reads temperature in celsius
  tempF = (9*tempC/5) + 32;
  humidity = thermo.getHumidity();
  
  
  Serial.print("Temperature (C):\t");
  Serial.println(tempC);
  Serial.print("Temperature (F):\t");
  Serial.println(tempF);
  Serial.print("Humidity (%)\t"); //  Relative Humidity in percent units
  Serial.println(humidity);
  
  delay(1000);
}