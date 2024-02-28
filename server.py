import sys
from gunicorn.app.wsgiapp import run
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send_data', methods=['POST'])
def send_data():
    data = request.get_json()
    print("Received data from Minecraft mod:", data)
    # Process the data as needed
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    sys.argv = "gunicorn --bind 0.0.0.0:5151 app:app".split()
    sys.exit(run())
