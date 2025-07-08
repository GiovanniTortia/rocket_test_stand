
LED_FORM = '<form action="/led" method="post"><button type="submit" name="led_btn" value="1">led</button></form>'
TARE_FORM = '<form action="/tare" method="post"><button type="submit" name="tare_btn" value="1">tare</button></form>'
CF_FORM = '<form action="/setCF", method="post"><input type="text" id="weight" name="weight"><label for="weight">weight:</label><button type="submit" name="weight_btn" value="1">set CF</button></form>'
START = '<form action="/start", method="post"><button type="submit" name="start_btn" value="1">record</button></form>'


INDEX = '<!DOCTYPE html><html>' + LED_FORM + TARE_FORM + CF_FORM + START +'</html>'