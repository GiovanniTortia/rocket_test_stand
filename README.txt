Program to set up a raspberry pi pico as a server, accessed from a web app, to control a rocket thrust test stand, using an hx711 ADC to read the output of a load cell and store it in an sd card. 

Once powered the raspberry pi periodically tries to connect to the specified wifi network, to access the web interface go to the pico's ip address on port 5000.
Must specify your network's SSID and password in function __main__ in main.py

To calibrate the sensor, first tare the sensor with no weights on it ("tare" button), once done (look at the led), place a known weight over the load cell, enter its weight in grams in the form and press "set CF" button
Once calibrated, press the "record" button to start recording the thrust in the sd card, the recording lasts 30 seconds
The onboard led toggles when processing something, toggling again once finished.

Microdot library by Miguel Grinberg: https://github.com/miguelgrinberg/microdot
HX711 library by Sergey Piskunov: https://github.com/SergeyPiskunov/micropython-hx711
