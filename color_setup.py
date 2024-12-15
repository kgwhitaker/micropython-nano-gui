# ili9486_pico.py Customise for your hardware config and rename

# Released under the MIT License (MIT). See LICENSE.

# ILI9486 on Pi Pico
# See DRIVERS.md for wiring details.

# from machine import Pin, SPI
# import gc

# from drivers.ili94xx.ili9486 import ILI9486 as SSD

# pdc = Pin(8, Pin.OUT, value=0)
# prst = Pin(9, Pin.OUT, value=1)
# pcs = Pin(10, Pin.OUT, value=1)
# spi = SPI(0, sck=Pin(6), mosi=Pin(7), miso=Pin(4), baudrate=30_000_000)
# gc.collect()  # Precaution before instantiating framebuf
# ssd = SSD(spi, pcs, pdc, prst)

import machine
import gc
from drivers.epaper.pico_epaper_42_v2 import EPD as SSD  # V2 driver

gc.collect()  # Precaution before instantiating framebuf.
ssd = SSD()  # Create a display instance based on a Pico in socket.