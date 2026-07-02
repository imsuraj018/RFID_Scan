# Required Arduino Libraries

Install the following libraries from the Arduino IDE Library Manager.

---

## 1. MFRC522

Author:
Miguel Balboa

Purpose:
Used for communication with the RC522 RFID Reader.

---

## 2. ESP8266WiFi

Included with ESP8266 Board Package.

Purpose:
Connects NodeMCU to WiFi.

---

## 3. ESP8266HTTPClient

Included with ESP8266 Board Package.

Purpose:
Used for sending HTTP requests to the FastAPI server.

---

## 4. SPI

Included with Arduino.

Purpose:
Communication protocol for RC522.

---

## Board Package

Install:

ESP8266 by ESP8266 Community

Version:
Latest Stable

---

## Board Selection

Board:
NodeMCU 1.0 (ESP-12E Module)

Flash Size:
4MB (FS:2MB OTA:~1019KB)

CPU Frequency:
80 MHz

Upload Speed:
115200

Port:
Select your COM Port

---

## Wiring

| RC522 | NodeMCU |
|--------|----------|
| SDA | D8 |
| SCK | D5 |
| MOSI | D7 |
| MISO | D6 |
| RST | D3 |
| GND | GND |
| 3.3V | 3.3V |

---

## Tested Hardware

- NodeMCU ESP8266
- RC522 RFID Reader
- MIFARE Classic 1K Cards

---

## Project Version

School RFID Tracking System

Version 1.0