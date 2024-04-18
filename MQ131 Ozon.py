from machine import ADC, Pin
import time

pin_sensor = 26  # Pas dit aan naar de juiste pin voor de sensor
value_rl = 1000  # Pas dit aan naar de weerstandswaarde van de belastingsweerstand

class MQ131Class:
    def __init__(self, pin_sensor, value_rl):
        self.pin_sensor = pin_sensor
        self.value_rl = value_rl
        self.adc = ADC(Pin(pin_sensor))

    def read_rs(self):
        # Lees de waarde
        value_sensor = self.adc.read_u16()

        # Bereken de spanning over de belastingsweerstand (voor 3.3V Raspberry Pico)
        v_rl = (value_sensor / 65535) * 3.3

        # Bereken de weerstand van de sensor (voor 3.3V Raspberry Pico)
        if v_rl == 0.0:
            return 0.0  # Voorkom deling door nul
        r_s = (3.3 / v_rl - 1.0)
        return r_s

mq131 = MQ131Class(pin_sensor, value_rl)

while True:
    O3_ppm = mq131.read_rs()  # Verander read_rs() naar mq131.read_rs()
    print("O3 Concentratie:", O3_ppm)
    time.sleep(1)  # Wacht voor de volgende meting



