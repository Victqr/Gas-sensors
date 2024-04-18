
---

# Gas-sensors: MQ131 en MG811

## Inleiding
Welkom! Ik ben Victor. Voor mijn GIP-project heb ik een code geschreven voor twee gas sensoren: de MQ811 en de MG131. Omdat er maar weinig informatie beschikbaar is over deze sensoren, deel ik hier meer gegevens over hun werking.

## Sensoren en Modules
De sensoren zijn gebaseerd op een FC22-module, die alleen een analoge pin heeft, zonder digitale pin. Hierbij vind je ook een foto van het schema zoals de datasheets en mijn leerkracht aanraden.

## Aansluiting
- **Voeding**: De 5V-voeding kan worden aangesloten op een batterij of via een boostbuck-converter. Sluit de boostbuck aan op de 5V-batterij en vervolgens sluit je de + van de boostbuck aan op de VBUS of VSYS van de Raspberry Pi. De - van de boostbuck wordt aangesloten op een GND-pin. 
- **FC22 Module**: Sluit de 5V van de module aan op de VSYS of VBUS van de Raspberry Pi (afhankelijk van welke voeding je gebruikt). Sluit de GND van de module aan op een GND-pin van de Pi. Sluit de 3.3V-pin van de FC22-module aan op de 3V3(OUT) pin van de Pi. De analoge pin van de module wordt verbonden met een ADC-pin van de Pi.
- **Boostbuck**: De boostbuck voorziet niet alleen de FC22-module van stroom, maar ook de Raspberry Pi Pico, waardoor deze wordt gevoed vanaf dezelfde batterij.

## Codes
De codes zijn ontworpen om de analoge data van de sensoren te lezen en om te zetten naar PPM-waardes van ozon (O3) of CO2.

---

## ENGLISH

---

# Gas Sensors: MQ131 and MG811

## Introduction
Hello! I'm Victor. For my GIP project, I had to write code for two gas sensors: the MQ811 and the MG131. Since there is very little information available about these sensors, I'm sharing more data about their operation here.

## Sensors and Modules
The sensors are based on an FC22 module, which only has an analog pin, without a digital pin. I'm also including a photo of the schematic as recommended by the datasheets and my teacher.

## Connection
- **Power Supply**: The 5V power supply can be connected to a battery or via a boostbuck converter. Connect the boostbuck to the 5V battery, and then connect the + of the boostbuck to the VBUS or VSYS of the Raspberry Pi. The - of the boostbuck is connected to a GND pin.
- **FC22 Module**: Connect the 5V of the module to the VSYS or VBUS of the Raspberry Pi (depending on which power supply you're using). Connect the GND of the module to a GND pin of the Pi. Connect the 3.3V pin of the FC22 module to the 3V3(OUT) pin of the Pi. The analog pin of the module is connected to an ADC pin of the Pi.
- **Boostbuck**: The boostbuck not only provides power to the FC22 module but also to the Raspberry Pi Pico, powering it from the same battery.

## Codes
The codes are designed to read the analog data from the sensors and convert it into PPM values of ozone (O3) or CO2.

---
