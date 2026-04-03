from flask import Flask, request, jsonify
import random
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
def generate_otp(length=5):
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])

@app.route('/generate-otp', methods=['POST'])
def send_otp():
    phone = request.json.get('phone')
    otp = generate_otp()
    print(f"Sending OTP {otp} to {phone}")  # Replace with SMS logic
    return jsonify({"otp": otp})

if __name__ == '__main__':
    app.run(debug=True)

