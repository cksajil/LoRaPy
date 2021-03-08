# LoRaWAN

![Language: Python](https://img.shields.io/badge/language-Python3-blue)
![TTN: v2](https://img.shields.io/badge/TTN-v2-success)
![Adafruit: 4074](https://img.shields.io/badge/Adafruit-4074-success)
![Lora: 868MHz](https://img.shields.io/badge/Lora-868MHz-success)

![TTN: v3](https://img.shields.io/badge/TTN-v3%20in%20progress-yellow)

This is an improved LoRaWAN v1.0 implementation in python.

It works with a Raspberry Pi 4 and the [Adafruit LoRa Radio Bonnet with OLED](https://www.adafruit.com/product/4074) - RFM95W @ 868MHz.

Based on the work of ❤️
- [mayeranalytics/pySX127x](https://github.com/mayeranalytics/pySX127x)
- [ryanzav/LoRaWAN](https://github.com/ryanzav/LoRaWAN)
- [jeroennijhof/LoRaWAN](https://github.com/jeroennijhof/LoRaWAN)

For reference on LoRa see: [lora-alliance: specification](https://www.lora-alliance.org/portals/0/specs/LoRaWAN%20Specification%201R0.pdf)

This fork improves the support for the [Adafruit LoRA Radio Bonnet with OLED](https://www.adafruit.com/product/4074) - RFM95W @ 868MHz.

You can find the access to the [Helium Network](https://helium.com) in the repository of [ryanzav](https://github.com/ryanzav/LoRaWAN).

---

## First Steps

1. Rename `keys_example.py` to `keys.py` and enter your device information from the [TTN Console](https://console.thethingsnetwork.org/applications).
1. Setup your Raspberry Pi
1. Connect the Adafruit Lora Bonnet
1. Add an antenna to the Lora Bonnet [p.e. "simple" Wire Antenna](https://learn.adafruit.com/adafruit-feather-m0-radio-with-lora-radio-module/antenna-options)
1. Check your [environment](https://www.thethingsnetwork.org/map) and look for a public Lora Gateway

---

## Testing

### Sending

    $ python3 tx_ttn.py

Sends an uplink to your TTN-Application.

### Receiving

    $ python3 rx_ttn.py

Receives a downlink from your TTN-Application. Attention: LoRaWAN does not send downlinks fulltime.

### Send & Receive

    $ python3 txrx_ttn.py

Sends an uplink and receives directly after a downlink.

---

## Usage (TTN v2 and TTS v3)

Now we use this library as a python package.
Move the folder to your project: `$ mv ~/LoRaPy ~/your-project/LoRaPy`.
Copy the `keys_example.py` to your project: `$ cp ~/LoRaPy ~/your-project/keys.py`
and set the correct keys from your TTN-Console. 

### Example
```python
from LoRaPy.lorapy import LoRaPy
import keys
import time


def receive_callback(payload):
    print(payload)


lora = LoRaPy(keys.devaddr, keys.nwskey, keys.appskey, True, receive_callback)

while True:
    lora.send('this is your payload-string', 7)
    time.sleep(900)
```

### Downlink check for The Thing Stack (v3)
```python
from LoRaPy.lorapy import LoRaPy
import keys
import time
last_send = 0


def receive_callback(payload):
    global last_send
    print(payload)
    # reset time 
    last_send = time.time()

    
def try_to_send(message):
    # wait at least 900s before sending next message.
    if last_send + 900 > time.time():
        return
    
    # more than 900s since the last sending.
    lora.send(message, 7)


lora = LoRaPy(keys.devaddr, keys.nwskey, keys.appskey, True, receive_callback)

while True:
    time.sleep(30)
    try_to_send('this is your payload-string')
```

## TODO

- [x] Add a constant uplink-sender
- [x] Add a constant uplink-sender with short downlink-check.
- [x] Remove Helium
- [x] TTN v3
- [ ] Check OTAA for TTN
- [ ] Prepare as python-library (p.e. PIP)
- [ ] move `./LoRaWAN` & `./SX127x` to git submodule (if possible...)
