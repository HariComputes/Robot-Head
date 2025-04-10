Details and images to be added soon
![Robot Head Final Product](https://github.com/HariComputes/Robot-Head/blob/main/Images/IMG-20230408-WA0000.jpg?raw=true "Robot Head")

Uses a raspberry pi 4. has 2 power supplies. USB-C and IEC C13/14. As well as a battery backup using a 12v 12ah lead acid battery.

Types of technologies used:
Software PWM
1-Wire
Serial communication


Pi pins/usage below:

GPIO 2 (I2C1 SDA)		Switch LED 1 - 5th button. Blue
GPIO 3 (I2C1 SCL)		Switch LED 2 - 4th button. White
GPIO 4 (GPCLK0)			Thermometer
Ground
GPIO 17					Motion Sensor
GPIO 27					Light Sensor
GPIO 22					Button 1
3v3 Power
GPIO 10 (SPI0 MOSI)		RGBW Strip - Green
GPIO 9 (SPI0 MISO)		RGBW Strip - Blue
GPIO 11 (SPI0 SCLK)		RGBW Strip - Red
Ground
GPIO 0 (EEPROM SDA)
GPIO 5					Switch 1
GPIO 6					Relay 2 - Mains
GPIO 13 (PWM1)			Button 2 - 2nd button. White
GPIO 19 (PCM FS)		Switch LED 3 - 2nd Button. White
GPIO 26					Button 3
Ground
5v Power
5v Power
Ground
GPIO 14 (UART TX)
GPIO 15 (UART RX)
GPIO 18 (PCM CLK)		EyeLEDs 1 - Right Eye
Ground
GPIO 23					Display Clock
GPIO 24					Display Data-In
Ground					
GPIO 25					Button 4
GPIO 8 (SPI0 CE0)		RGBW Strip - White
GPIO 7 (SPI0 CE1)		Switch LED 4 - 3rd Button. Red
GPIO 1 (EEPROM SCL)
Ground
GPIO 12 (PWM0)			Button 1 - 1st button. Blue
Ground
GPIO 16					Relay 1 - USB C
GPIO 20 (PCM DIN)		Switch LED 5 - 1st button. Blue
GPIO 21 (PCM DOUT)		EyeLEDs 2 - Left Eye
