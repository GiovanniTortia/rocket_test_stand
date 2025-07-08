from microdot import Microdot, Response
import network
import time
import sdcard
import machine
import uos
from hx711 import HX711
import pages
import _thread


cs = machine.Pin(13, machine.Pin.OUT)

spi = machine.SPI(1,
                  baudrate = 1000000,
                  polarity=0,
                  phase=0,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(10),
                  mosi=machine.Pin(11),
                  miso=machine.Pin(12))

sd = sdcard.SDCard(spi, cs)
vfs = uos.VfsFat(sd)
uos.mount(vfs, '/sd')

sensor = HX711(d_out=19, pd_sck=18)

def connect(ssid, pw):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, pw)
    while wlan.isconnected() == False:
        print("trying to connect")
        time.sleep(1)
    print(wlan.ifconfig())


app = Microdot()
Response.default_content_type = 'text/html'

led=machine.Pin("LED", machine.Pin.OUT)

@app.route('/')
def home(request):
    return pages.INDEX

@app.route('/led', methods=['POST'])
def led_toggle(request):
    led.toggle()
    
@app.route('/tare', methods=['POST'])
def tare_sensor(request):
    led.toggle()
    print(sensor.tare())
    led.toggle()

@app.route('/setCF', methods=['POST'])
def setCF(req):
    led.toggle()
    weight = float(req.form.get('weight'))
    print('weight: ')
    print(weight)
    CF = sensor.getCF(weight)
    print(CF)
    led.toggle()
    
@app.route('/read', methods=['GET'])
def read(req):
    w = sensor.read()
    return {'weight':w}

@app.route('/start', methods=['POST'])
def thr_start(req):
    led.toggle()
    file = open("/sd/recording.txt", "w")
    start = time.time_ns()
    et =  0
    while(et/1000000000 < 30):
        w = sensor.read()
        et = time.time_ns()-start
        file.write(str(et/1000)+": "+str(w)+"\n")
    led.toggle()
    file.close()
    

if __name__ == '__main__':
    ssid = 'Giova'
    pw = 'horten229'
    connect(ssid, pw)
    app.run(debug=True)
    


