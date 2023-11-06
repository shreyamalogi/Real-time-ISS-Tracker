
# Real Time ISS Tracker 🛰️🌐

Welcome to the beginner-friendly project - " Real Time ISS Tracker project! "

Crafted and taught by **Shreya Malogi!** 🌐

[![GitHub stars](https://img.shields.io/github/stars/shreyamalogi/Real-Time-ISS-Tracker.svg?style=social)](https://github.com/shreyamalogi/Real-Time-ISS-Tracker/stargazers)

### Project Details: 💻🌐📅✍️

- **Functionality:** Tracks the International Space Station's (ISS) current location using the Open Notify API.
- **Tech Stack:** `Python`, `Requests`, ` Open Notify API`
- **Author:** [@shreyamalogi](https://github.com/shreyamalogi/)
- **Year of Project:** 2021
  
---

# Table of Contents

- [Introduction](#introduction)
- [How It Works](#how-it-works)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Running the Script](#running-the-script)
- [Example Output](#example-output)
- [Contribution](#contribution)
- [License](#license)

# Introduction 

 🚀 This Python script utilizes the Open Notify API to effortlessly retrieve and display the current location of the International Space Station (ISS). Whether you're an astronomy enthusiast or simply curious, join us in exploring the wonders of space and contribute to this spellbinding journey! ⭐


## How It Works 

1. The script makes an API request to [Open Notify](http://api.open-notify.org/iss-now.json).
2. It uses the `requests` library to handle the HTTP request.
3. The `raise_for_status()` method checks for any errors in the API response.
4. The JSON response is then parsed to extract the ISS's current latitude and longitude.
5. The latitude and longitude are stored in a tuple named `iss_position`.
6. Finally, the script prints the ISS's current position.

## Dependencies 

- [Requests](https://docs.python-requests.org/en/latest/): Used for making HTTP requests to the Open Notify API.


## Installation 

Clone the repository to your local machine:

```bash
git clone https://github.com/shreyamalogi/Real-Time-ISS-Tracker.git
```

Ensure you have the necessary dependencies installed by running:

```bash
pip install requests
```

## Running the Script 

Navigate to the project directory:

```bash
cd Real-Time-ISS-Tracker
```

Execute the following command:

```bash
python main.py
```

The script will fetch and display the ISS's current location. Enjoy tracking! 🌍🛰️

## Example Output 

```python
('33.3136', '-9.0541')
```



## Contribution 

Feel the magic within you? Contribute to this enchanting spellbook and make it even more magical. Don't forget to star the project! ⭐🌟

## License 

This ISS Tracker script is licensed under the MIT License.

MIT License

Copyright (c) 2021 Shreya Malogi

Happy tracking! 🛰️🌐

