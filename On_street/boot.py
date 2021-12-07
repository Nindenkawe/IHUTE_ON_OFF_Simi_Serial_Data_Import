import ubinascii
import machine
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'Wutang-Wan'
password = '..,123456'
mqtt_server = '10.0.2.15'
user = 'nindenka'
password = 'Robinson'
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'notification'
topic_pub = b'hello'

last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())