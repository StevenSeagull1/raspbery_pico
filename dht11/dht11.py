import time
import board
import adafruit_dht

# Definieer de pinnen waarop de DHT11 is aangesloten
DHT_PIN = board.GP0

# Maak een DHT-object aan
dht = adafruit_dht.DHT11(DHT_PIN)

while True:
    try:
        # Lees de temperatuur en vochtigheid uit
        temperature_c = dht.temperature
        humidity = dht.humidity

        # Print de waarden naar de console
        print("Temperature: {:.1f}°C".format(temperature_c))
        print("Humidity: {}%".format(humidity))

    except RuntimeError as e:
        # Als er een fout optreedt, laat het zien en ga door
        print("Fout bij het lezen van de sensor: ", e)

    time.sleep(2)  # Wacht 2 seconden voordat de volgende meting wordt uitgevoerd
