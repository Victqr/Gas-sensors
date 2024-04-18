from machine import ADC, Pin
import time

co2_sensor_pin = machine.ADC(27)

def read_co2_level():
    sensor_value = co2_sensor_pin.read_u16()
    co2_ppm = sensor_value / 65535 * 3300
    CO2waarde = int(350 + (sensor_value - 0) * (10000 - 350) / (65535 - 0))
    return CO2waarde


while True:
    CO2waarde = read_co2_level()
    print("O3 Concentratie:", CO2waarde)
    time.sleep(1)

