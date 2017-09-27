"""
MicroPython I2C driver for LIS2HH12 3-axis accelerometer
"""

import utime
import ustruct
from machine import I2C, Pin

_TEMP_L = const(0x0b)
_TEMP_H = const(0x0c)
_WHO_AM_I = const(0x0f)
_CTRL1 = const(0x20)
_CTRL2 = const(0x21)
_CTRL3 = const(0x22)
_CTRL4 = const(0x23)
_CTRL5 = const(0x24)
_CTRL6 = const(0x25)
_CTRL7 = const(0x26)
_OUT_X_L = const(0x28)
_OUT_X_H = const(0x29)
_OUT_Y_L = const(0x2a)
_OUT_Y_H = const(0x2b)
_OUT_Z_L = const(0x2c)
_OUT_Z_H = const(0x2d)

# CTRL1
_ODR_MASK = const(0b01110000)
_ODR_OFF = const(0b00000000)
_ODR_50HZ = const(0b00100000)
_ODR_100HZ = const(0b01100000)
_ODR_200HZ = const(0b01000000)

class LIS2HH12:
    def __init__(self, i2c=None, address=0x1e):
        if i2c is None:
            self.i2c = I2C(scl=Pin(26), sda=Pin(25))
        else:
            self.i2c = i2c

        self.address = address

        uchar = self._register_uchar(_CTRL1)
        uchar &= ~_ODR_MASK # clear ODR bits
        uchar |= _ODR_100HZ # set 100Hz
        self._register_uchar(_CTRL1, uchar)

    def _register_uword(self, register, value=None):
        if value is None:
            data = self.i2c.readfrom_mem(self.address, register, 2)
            return ustruct.unpack("<H", data)[0]
        data = ustruct.pack("<H", value)
        self.i2c.writeto_mem(self.address, register, data)

    def _register_uchar(self, register, value=None):
        if value is None:
            return self.i2c.readfrom_mem(self.address, register, 1)[0]
        data = ustruct.pack("<B", value)
        self.i2c.writeto_mem(self.address, register, data)

    def read(self):
        x = self._register_uword(_OUT_X_L)
        y = self._register_uword(_OUT_Y_L)
        z = self._register_uword(_OUT_Z_L)
        return (x, y, z)

    def whoami(self):
        return self._register_uchar(_WHO_AM_I)
