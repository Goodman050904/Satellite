import machine
import uos
from Satlib.sdcard import SDCard

# Initialize SPI
spi = machine.SPI(1, sck=machine.Pin(14), mosi=machine.Pin(15), miso=machine.Pin(12))

# Initialize SD card
sd = SDCard(spi)

# Mount SD card
uos.mount(sd, '/sd')
print("SD card connected")

# List files in the root directory of the SD card
print(uos.listdir('/sd'))

class Copy:
    def __init__(self, from_loc='demo0.csv', to_loc='demo_data.csv'):
        self.source_file = '/sd/' + str(from_loc)
        self.destination_file = '/' + str(to_loc)
        
        try:
            with open(self.source_file, 'rb') as source:
                with open(self.destination_file, 'wb') as destination:
                    destination.write(source.read())
            print("File copied successfully.")
        except OSError as e:
            print("Error:", e)

# Usage
if __name__ == "__main__":
    file_copy = Copy(from_loc='demo0.csv', to_loc='demo_data.csv')
