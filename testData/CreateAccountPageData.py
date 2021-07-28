import requests


class CreateAccountData():

    headers = {
        'User-Agent': 'Chrome/92.0.4515.107 '}
    response = requests.get("https://www.dummy.restapiexample.com/api/v1/employees", headers=headers)
    while response.status_code != 200:
        response = requests.get("https://www.dummy.restapiexample.com/api/v1/employees", headers=headers)
    json_response = response.json()
    data = json_response.get("data")

    expected_data = [{
        "pre_search": "Echo",
        "desired": "Echo Support",
        "Expected_Links":
            ['Getting Started',
             'Wi-Fi and Bluetooth',
             'Device Software and Hardware',
             'Troubleshooting']
        }
    ]



