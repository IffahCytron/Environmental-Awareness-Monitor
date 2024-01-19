import time
import board
import digitalio
import adafruit_ssd1306
import adafruit_dht
from adafruit_circuitplayground import cp

# Initialize OLED display
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Initialize environmental sensor (DHT22) - Optional
dht_sensor = adafruit_dht.DHT22(board.GP15)

# Main loop
while True:
    # Clear the OLED display
    oled.fill(0)

    # Read temperature and humidity from the sensor (if connected) - Optional
    try:
        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity
    except (ValueError, RuntimeError):
        temperature = None
        humidity = None

    # Display environmental data on OLED
    oled.text("Room Conditions", 0, 0)
    oled.text("----------------", 0, 10)
    
    if temperature is not None:
        oled.text("Temp: {:.1f} C".format(temperature), 0, 20)
    
    if humidity is not None:
        oled.text("Humidity: {:.1f}%".format(humidity), 0, 30)
    
    # Display Climate Action (SDG 13) icon if the environmental conditions are critical
    if temperature is not None and humidity is not None:
        if temperature > 30 and humidity > 70:
            oled.text("SDG 13: 🔥🌧", 0, 40)  # High temp and humidity
        elif temperature < 0:
            oled.text("SDG 13: ❄️", 0, 40)  # Low temperature
        elif humidity < 30:
            oled.text("SDG 13: 🌵", 0, 40)  # Low humidity
    
    # Refresh the display
    oled.show()
    
    # Check for user interaction (e.g., button press)
    if cp.button_a:
        # Implement actions or messages related to SDGs here
        oled.fill(0)
        oled.text("Take action for", 0, 0)
        oled.text("SDG 13: Climate", 0, 10)
        oled.text("Action!", 0, 20)
        oled.show()
        time.sleep(5)  # Display message for 5 seconds
