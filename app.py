from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_ip_info', methods=['POST'])
def fetch_ip_info():
    ip_address = request.form['ip_address']

    if not ip_address:
        return jsonify({"error": "Please enter an IP address."})

    try:
        url = f'https://ipinfo.io/{ip_address}/json'
        headers = {
            'Authorization': 'Bearer 2fa007984e53b5'
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({"error": f"Failed to retrieve IP details. Status code: {response.status_code}"})

    except Exception as e:
        return jsonify({"error": "An error occurred while fetching IP details."})

if __name__ == '__main__':
    app.run(debug=True)
