# Environmental-Awareness-Monitor
 This project uses a Raspberry Pi Pico to monitor room conditions, displaying temperature, humidity, and promoting SDG 13 (Climate Action) awareness through a simple OLED display interface. Stay informed and take action for a sustainable environment!


Project Description:
The Environmental Awareness Monitor is a Raspberry Pi Pico-based project designed to promote awareness of environmental conditions and Sustainable Development Goal 13 (Climate Action). It monitors room temperature and humidity, displaying real-time data on an OLED display. Additionally, it alerts users to critical conditions by displaying climate-related icons. Users can also trigger information related to SDG 13 by pressing a button.

How It Works:

Hardware Setup:

Connect an OLED display to your Raspberry Pi Pico.
Optionally, connect a DHT22 temperature and humidity sensor to gather environmental data.
Running the Program:

Save the environment_monitor.py code to your Raspberry Pi Pico.
Connect your Pico to your computer via USB.
Displaying Environmental Data:

The program continuously reads and displays temperature and humidity data on the OLED display, providing real-time information about the room's conditions.
SDG 13 Awareness:

The program displays an SDG 13 (Climate Action) icon on the OLED display when certain environmental conditions are met. For example, it will display different icons for high temperature and humidity or low temperature or humidity, promoting awareness of climate-related issues.
User Interaction:

The project allows user interaction by pressing Button A on the Raspberry Pi Pico.
When Button A is pressed, the OLED display will show messages or actions related to SDG 13, encouraging users to take climate action.
Example SDG 13 Messages:

"Take action for SDG 13: Climate Action!"
"Reduce energy consumption to combat climate change."
Customization:

You can customize the SDG 13 messages and conditions for displaying climate icons to suit your specific needs and climate awareness goals.
Dependencies:

This project requires the Adafruit CircuitPython library for the OLED display and, optionally, the Adafruit CircuitPython DHT library for the DHT22 sensor.
