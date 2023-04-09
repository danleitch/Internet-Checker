# Internet-Checker

This Python script checks internet connectivity by pinging Google's DNS server and controls an LED based on the result. If the ping is unsuccessful, the script turns on the LED, and if the ping is successful, the script turns off the LED. The script runs on a while true loop and rests for 30 seconds between each check.


## Getting Started
To use this script, you'll need:

A Raspberry Pi or other Linux-based computer with Python 3 installed
A compatible LED connected to your Raspberry Pi's GPIO pins (see these instructions for details)


## Installation
To install this script:

1. Clone the repository to your Raspberry Pi using the following command:
``` git clone https://github.com/danleitch/Internet-Checker.git ```

2. Navigate to the repository directory using the following command:
``` cd internet-checker ```

3. Make the script file executable using the following command:
``` chmod +x internet_checker.py ```

## Usage
To run the script, navigate to the repository directory and use the following command:
```python3 ./internet_checker.py ```

The script will run in the foreground and continuously check internet connectivity while controlling the LED based on the result. Press Ctrl+C to stop the script.

## Customization
You can customize the script as needed by modifying the following variables at the top of the script:

ip: the IP address to ping (default is Google's DNS server)
on_cmd: the command to turn the LED on (default is echo 1 | sudo tee /sys/class/leds/PWR/brightness)
off_cmd: the command to turn the LED off (default is echo 0 | sudo tee /sys/class/leds/PWR/brightness)
You can also modify the while loop to change the interval between checks (default is 30 seconds):

```
while True:
    # Your code here

    # Wait for 60 seconds before checking again
    time.sleep(60)
```
