import json
import time

import requests
import simplejson

sp_api_key = 'ApiKey 8fbd38a9-7713-41a3-b5fc-9dd57cd64c1d'
nafath_url = 'https://www.iam.gov.sa/nafath/'
headers = {
    'Content-Type': 'application/json',
    'Authorization': sp_api_key
}
national_id = '2406685814'
payload = json.dumps({
    "Action": "SpRequest",
    "Parameters": {
        "service": "AdvancedLogin",
        "id": national_id
    }
})

print("Header", headers)
print("data", payload)
print()

random = ''
transId = ''
try:
    print("Sending POST Request")
    response = requests.request("POST", nafath_url, headers=headers, data=payload)
    print('response', response)
    content = response.json()
    print('content : ', content)
    transId = content.get('transId', False)
    random = content.get('random', False)
except Exception as e:
    print('Error during the request.', e)
    pass

print('transId : ', transId)
print('random : ', random)
print(content)

if transId and random:
    payload_check = json.dumps({
        "Action": "CheckSpRequest",
        "Parameters": {
            "transId": transId,
            "id": national_id,
            "random": random
        }
    })
    print('payload_check', payload_check)
    status = ''
    count = 1
    arFullName = ''
    while count < 60:
        print('count', count)

        try:
            response2 = requests.request("POST", nafath_url, headers=headers, data=payload_check)
            print('response2', response2)
            print('response2 content:', response2.text)

            if response2.status_code == 200:
                try:
                    content2 = response2.json()
                    print('content2', content2)
                    status = content2.get('status', False)
                    print('status', status)

                    if status == 'COMPLETED':
                        person = content2.get('person', {})
                        arFullName = person.get('arFullName', 'N/A')
                        print('person', person)
                        print('full name', arFullName)

                except simplejson.errors.JSONDecodeError as decode_error:
                    print('JSON Decode Error:', decode_error)
                    print('Response2 Content:', response2.text)


            else:
                # Print error response details
                error_response = {
                    'Code': content2.get('Code', 'N/A'),
                    'RequestedURL': content2.get('RequestedURL', 'N/A'),
                    'Message': content2.get('Message', 'N/A'),
                    'Trace': content2.get('Trace', 'N/A')
                }
                print('Error Response2:', error_response)

        except requests.exceptions.RequestException as e:
            print('2nd Step ..')
            print('Exception', e)
            pass

        time.sleep(1)
        count += 1
