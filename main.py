import logging
from urllib.parse import urlencode
from datetime import datetime

import requests

logging.basicConfig(level=logging.INFO)


def main():
    endpoint = "https://api.sunrise-sunset.org/json"
    params = \
        {
            "lat": 40.7579787,
            "lng": -73.9877366,
            "formatted": 0
        }

    # convert the 'English' string to HTML
    url_params = urlencode(params)

    url = f"{endpoint}?{url_params}"

    logging.info(url)

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    now = datetime.now().hour
    sunrise, sunset = get_hour('sunrise', data), get_hour('sunset', data)
    dark = is_dark(now, sunrise, sunset)

    print(
        f"    now: {now}\nsunrise: {sunrise}\n sunset: {sunset}\n   dark: {dark}")


def get_hour(key, data):
    # extracts the hour form the datetime received and adds 2 to adjust the timezone
    return int(data['results'][key].split('T')[1].split(':')[0]) + 2


def is_dark(hour, sunrise, sunset):
    if hour < sunrise or hour > sunset:
        return True
    else:
        return False


if __name__ == '__main__':
    main()

# logging.debug(stuff)
