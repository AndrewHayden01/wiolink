sudo rm -rf micropython
git submodule update --init
cd micropython
git submodule update --init
cd ..
cp -r umqtt micropython/ports/esp8266/modules
cp {wio_link,ssd1306,tsl2561,sensors,actuators,displays,urequests}.py micropython/ports/esp8266/modules
mkdir micropython/ports/esp8266/scripts
cp boot.py micropython/ports/esp8266/scripts
rm micropython/ports/esp8266/scripts/main.py
cd micropython/ports/esp8266
make axtls
make
sudo rm /vagrant/firmware/micropython-1.9.3-wiolink-clean.bin
cp build/firmware-combined.bin /vagrant/firmware/micropython-1.9.3-wiolink-clean.bin