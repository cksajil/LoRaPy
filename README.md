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

## Preparation

1. Rename `keys_example.py` to `keys.py` and enter your device information from the [TTN Console](https://console.thethingsnetwork.org/applications).
1. Setup your Raspberry Pi
1. Connect the Adafruit Lora Bonnet
1. Add an antenna to the Lora Bonnet [p.e. "simple" Wire Antenna](https://learn.adafruit.com/adafruit-feather-m0-radio-with-lora-radio-module/antenna-options)
1. Check your [environment](https://www.thethingsnetwork.org/map) and look for a public Lora Gateway

---

## Usage

### Sending

    $ python3 tx_ttn.py

Sends an uplink to your TTN-Application.

### Receiving

    $ python3 rx_ttn.py

Receives a downlink from your TTN-Application. Attention: LoRaWAN does not send downlinks fulltime.

### Send & Receive

    $ python3 txrx_ttn.py

Sends an uplink and receives directly after a downlink.

## TODO

- [ ] Add a constant uplink-sender
- [ ] Add a constant uplink-sender with short downlink-check.
- [ ] Check OTAA for TTN
- [ ] Remove Helium
- [ ] TTN v3
- [ ] move `./LoRaWAN` & `./SX127x` to git submodule (if possible...)
