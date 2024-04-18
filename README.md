
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
