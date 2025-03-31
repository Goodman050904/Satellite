import machine
import utime
import uos


from Satlib.mq2 import MQ2
from Satlib.gyro import MPU6050
from Satlib.pressure import*
from Satlib.assistant import*

#i2c configuration
i2c= machine.I2C(0,scl=machine.Pin(1),sda=machine.Pin(0))
devices=i2c.scan()
if devices:
    print (devices)
    
#mq2
sensor =MQ2(pinData = 26)
sensor.calibrate()

#gyro
mpu6050 = MPU6050(i2c)

#pressure
bmp280 = BMP280(i2c)
calibrate.pressure(bmp280)


    
while True:
        t=time.ticks_ms()/1000
        pressure = bmp280.pressure
        temperature=bmp280.temperature
        
        GAS = sensor.readLPG()
        Smoke = sensor.readSmoke()
        Methane = sensor.readMethane()
        Hydrogen = sensor.readHydrogen()
        
        gx=round(mpu6050.gyro.x,2)
        gy=round(mpu6050.gyro.y,2)
        gz=round(mpu6050.gyro.z,2)
        ax=round(mpu6050.accel.x,2)
        ay=round(mpu6050.accel.y,2)
        az=round(mpu6050.accel.z,2)
        
        dashboard.sendAll(pressure, temperature, Smoke, GAS, Methane, Hydrogen, ax, ay, az, gx, gy, gz)
       
