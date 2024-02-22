# Smart Power Quality Monitoring System

## Introduction

The Smart Power Quality Monitoring System is a Raspberry Pi-based project designed for real-time monitoring of live current and voltage. Utilizing dedicated sensors, the system converts current and voltage readings into Analog-to-Digital (ADC) values, which are then logged to a Firebase real-time database. This project is ideal for tracking power quality metrics, historical analysis, and providing alerts for abnormal power conditions.

## Features

- _Real-time Monitoring_ : Continuously monitors live current and voltage data.
- _Data Logging_ : Logs current and voltage information to a Firebase real-time database, facilitating historical analysis.
- _Alert System_ : Issues alerts for abnormal power conditions, ensuring timely response to potential issues.

## Hardware Requirements

- Raspberry Pi (any model with GPIO pins)
- Current sensor (ACS-712)
- Voltage sensor (ZMPT101B)

## Software Requirements

- Python 3.x

## Installation

1. Clone this repository to your Raspberry Pi.

   ```bash
   git clone https://github.com/jaywyawhare/Smart-Power-Quality-Monitoring-System.git
   ```

2. Install the required libraries.

   ```bash
   chmod +x setup.sh
   bash setup.sh
   ```

3. Set up a Firebase real-time database and obtain the credentials along with ADAFRUIT_IO_USERNAME and ADAFRUIT_IO_KEY.

4. Create a `.env` file in the root directory of the project and add the following environment variables:

   ```bash
   apiKey = <FIREBASE_API_KEY>
   authDomain = <FIREBASE_AUTH_DOMAIN>
   databaseURL = <FIREBASE_DATABASE_URL>
   storageBucket = <FIREBASE_STORAGE_BUCKET>
   messageSenderId = <FIREBASE_MESSAGE_SENDER_ID>
   appId = <FIREBASE_APP_ID>
   measurementId = <FIREBASE_MEASUREMENT_ID>
   ADAFRUIT_IO_USERNAME = <ADAFRUIT_IO_USERNAME>
   ADAFRUIT_IO_KEY = <ADAFRUIT_IO_KEY>
   ```

## Usage

Run the main script with `python main.py`.

## Ownership

- If you use this tool/library, you are obligated to sponsor the [creator](https://github.com/jaywyawhare) in a way that makes you not a mega jerk. Remember, mega jerks are never cool.

- Using the word <b>'Smart Power Quality Monitoring System'</b> in your project implies that the Smart Power Quality Monitoring System does not own your project. However, if you don't use the word <b>'Smart Power Quality Monitoring System'</b> in your project implies that the Smart Power Quality Monitoring System owns your project. If you like to keep ownership of your project, use the word <b>'Smart Power Quality Monitoring System'</b> in your project.

  Here are some examples of how to use the word <b>'Smart Power Quality Monitoring System'</b> in your project:

  - ✅ "Project Smart Power Quality Monitoring System" (Does not owned by Smart Power Quality Monitoring System)

  - ❌ "Linux" (Owned by Smart Power Quality Monitoring System, please consider using the word <b>'Smart Power Quality Monitoring System'</b> in your project)

  - ❌ "Windows" (Owned by Smart Power Quality Monitoring System, please consider using the word <b>'Smart Power Quality Monitoring System'</b> in your project)

## License

This project is licensed under the MIT License - see the [LICENCE](./LICENCE.md) file for details.
