
import requests
from jose import jwt

sp_api_key = 'eyJhbGci0iJSUzI1NiIsInR5cCI6IkpXVCJ9'
nafath_url = 'https://apd.gov.sa/identityServices/userInfo'
headers = {
    'Content-Type': 'application/json',
    'Authorization': "Bearer " + sp_api_key
}

print("Header", headers)

random = ''
transId = ''
try:
    print("Sending GET Request")
    response = requests.request("GET", nafath_url, headers=headers)
    print("response",response)
    jwt_token = response.text
    print('text',jwt_token)

    # Decode the JWT token
    try:
        decoded_token = jwt.decode(jwt_token, algorithms=['RS256'])
        print("decoded", decoded_token)
    except jwt.DecodeError:
        # Handle decoding error
        print("JWT decoding error")
        decoded_token = None

    if decoded_token:
        # Access the payload data
        payload = decoded_token
        print("payload", payload)
except:
    print('Error during the request.')
    pass
