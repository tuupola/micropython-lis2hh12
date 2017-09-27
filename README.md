# MicroPython LIS2HH12 I2C driver

MicroPython library for accessing the [STMicroelectronics LIS2HH12](http://www.st.com/en/mems-and-sensors/lis2hh12.html) 3-axis accelerometer over
I2C. The LIS2HH12 is an ultra-low-power high-performance three-axis linear accelerometer belonging to the “pico” family. It has full scales of ±2g/±4g/±8g and is capable of measuring accelerations with output data rates from 10 Hz to 800 Hz.

## Usage

Using default I2C pins for ESP32.

```python
import utime
from lis2hh12 import LIS2HH12

sensor = LIS2HH12()

while True:
    print(sensor.whoami())
    print(sensor.read())
    utime.sleep_ms(1000)
```

Custom I2C pins when using non ESP32 board.

```python
import utime
from machine import I2C, Pin
from lis2hh12 import LIS2HH12

i2c = I2C(scl=Pin(26), sda=Pin(25))
sensor = LIS2HH12(i2c)

while True:
    print(sensor.whoami())
    print(sensor.read())
    utime.sleep_ms(1000)
```

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.