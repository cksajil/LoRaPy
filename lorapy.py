from SX127x.LoRa import *
from LoRaPy.lorasender import LoRaSender


class LoRaPy(object):
    def __init__(self, dev_addr=[], nw_key=[], app_key=[], verbose=False, callback=lambda *_, **__: None):
        self.lora_sender = LoRaSender(dev_addr, nw_key, app_key, verbose, callback)
        self.setup_lora()

        if verbose:
            print(self.lora_sender)

        assert (self.lora_sender.get_agc_auto_on() == 1)

    def setup_lora(self):
        self.lora_sender.set_mode(MODE.SLEEP)
        self.lora_sender.set_dio_mapping([1, 0, 0, 0, 0, 0])
        self.lora_sender.set_freq(868.1)
        self.lora_sender.set_pa_config(pa_select=1)
        self.lora_sender.set_spreading_factor(7)
        self.lora_sender.set_pa_config(max_power=0x0F, output_power=0x0E)
        self.lora_sender.set_sync_word(0x34)
        self.lora_sender.set_rx_crc(True)

    def send(self, string, spreading_factor=7):
        self.lora_sender.set_dio_mapping([1, 0, 0, 0, 0, 0])
        self.lora_sender.set_spreading_factor(spreading_factor)
        self.lora_sender.send_tx(string)
