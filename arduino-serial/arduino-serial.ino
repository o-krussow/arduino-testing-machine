#include <ezButton.h>
#include <SPI.h>
#include <Adafruit_MAX31855.h>

/***************************************************
  This is an example for the Adafruit Thermocouple Sensor w/MAX31855K

  Designed specifically to work with the Adafruit Thermocouple Sensor
  ----> https://www.adafruit.com/products/269

  These displays use SPI to communicate, 3 pins are required to
  interface
  Adafruit invests time and resources providing this open source code,
  please support Adafruit and open-source hardware by purchasing
  products from Adafruit!

  Written by Limor Fried/Ladyada for Adafruit Industries.
  BSD license, all text above must be included in any redistribution
 ****************************************************/



// Default connection is using software SPI, but comment and uncomment one of
// the two examples below to switch between software SPI and hardware SPI:

// Example creating a thermocouple instance with software SPI on any three
// digital IO pins.
#define MAXDO   3
#define MAXCS   4
#define MAXCLK  5

// initialize the Thermocouple
Adafruit_MAX31855 thermocouple(MAXCLK, MAXCS, MAXDO);

ezButton button(8);



void setup() {
  
  button.setDebounceTime(50); // set debounce time to 50 milliseconds
  button.setCountMode(COUNT_FALLING);
  
  Serial.begin(115200);
  
  while (!Serial) delay(1); 
  
  Serial.println("MAX31855 test");
  // wait for MAX chip to stabilize
  delay(500);
  Serial.print("Initializing sensor...");
  if (!thermocouple.begin()) {
    Serial.println("ERROR.");
    while (1) delay(10);
  }
  Serial.println("DONE.");
}

void button_pressed() {
  float sample_delay = 100;
  int count = 0;
  int run_time = 30; //Enter run time in seconds
  int current_sensor_value = 0;
  float current_sensor_voltage = 0;
  
  float loop_run_time = (1000/sample_delay)*run_time;
  
  while (count < loop_run_time) {
      current_sensor_value = analogRead(A0);
      current_sensor_voltage = current_sensor_value * (5.0 / 1023.0);
      
      double c = thermocouple.readCelsius();
      if (isnan(c)) {
       Serial.println("Something wrong with thermocouple!");
      } else {
       Serial.println(c);
       Serial.println(current_sensor_voltage);
      }

      
      delay(sample_delay);

      count++;
  }
}

void loop() {
  button.loop();
  
  if (button.isPressed()) {
    button_pressed();
      
    
  }
}
