from machine import Pin
from ssd1306 import SSD1306_I2C
from wio_link import PORT_MAPPING, DEFAULT_PORTS, GroveDevice, i2c

class Display(GroveDevice):

    def __init__(self, type, port):
        GroveDevice.__init__(self, type, port)

    def write_message(self, line):
        pass

class OledScreen(Display, SSD1306_I2C):
    
    def __init__(self, port=DEFAULT_PORTS["OledScreen"], width=128, height=64, address=0x3c):
        if address not in i2c.scan():
            raise OSError("Please check if the OLED Screen is connected to Port 6 or an I2C hub")
        Display.__init__(self, "OledScreen", port)
        SSD1306_I2C.__init__(self, width, height, i2c, addr=address)
        self.max_line = int(self.height/8)

    def clear(self):
        self.fill(0)

    def _check_max_line(self, line):
        if line > self.max_line:
            raise ValueError("The {0}x{1} display can only support {2} lines of texts".format(self.width, self.height, max_line))

    def clear_line(self, line):
        self._check_max_line(line)
        for y in range(8*(line-1), 8*line):
            for x in range(self.width):
                self.pixel(x, y, 0)

    def write_line(self, line, message):
        if not isinstance(message, str):
            raise TypeError("The message to be shown can only be strings")
        self._check_max_line(line)
        self.text(message, 0, 8*(line-1))

    def show_line(self, line, message):
        self.clear_line(line)
        self.write_line(line, message)
        self.show()

    def show_sensor_data(self, sensor, line):
        sensor.show_data(self, line)