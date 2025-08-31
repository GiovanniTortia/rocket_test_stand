Program to set up a raspberry pi pico as a server, accessed from a web app, to control a rocket thrust test stand, using an hx711 ADC to read the output of a load cell and store it in an sd card. 
Once powered the raspberry pi periodically tries to connect to the specified wifi network, to access the web interface go to the pico's ip address on port 5000.
The onboard led toggles when processing something, toggling again once finished.

Microdot library by Miguel Grinberg: https://github.com/miguelgrinberg/microdot
HX711 library by Sergey Piskunov: https://github.com/SergeyPiskunov/micropython-hx711
