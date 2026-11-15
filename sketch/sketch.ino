#include <Arduino_RouterBridge.h>
#include <Arduino_Modulino.h>

ModulinoThermo thermo;

float temp = 0;  // temp in Celsius
float humidity = 0;

void setup() {  // runs once
  Bridge.begin();
  Modulino.begin(); // connects to the modulino
  thermo.begin();
  Serial.begin(9600);
}

void loop() { // runs continously
  temp = thermo.getTemperature(); // reads temperature in celsius
  humidity = thermo.getHumidity();
  
  
  Serial.print("Temperature (C):\t");
  Serial.println(temp);
  Serial.print("Humidity (%)\t"); //  Relative Humidity in percent units
  Serial.println(humidity);
  
  Bridge.notify("update_scensors", temp, humidity);

  
  delay(1000);
}