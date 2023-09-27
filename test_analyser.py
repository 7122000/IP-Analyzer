ip_address = '103.181.91.131'  
import requests
url = f'https://ipinfo.io/{ip_address}/json'

headers = {
    'Authorization': f'Bearer {"2fa007984e53b5"}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    ip_info = response.json()
    parts = ip_info["org"].split()
    ISP = " ".join(parts[1:])
    ASN = ip_info["org"].split()[0]
    print(f"IP Address: {ip_info['ip']}")
    print(f"ISP: {ISP}")
    print(f"ASN: {ASN}")
    print(f"City: {ip_info['city']}")
    print(f"Region: {ip_info['region']}")
    print(f"Country: {ip_info['country']}")
    print(f"Location: {ip_info['loc']}")
else:
    print(f"Failed to retrieve IP details. Status code: {response.status_code}")

