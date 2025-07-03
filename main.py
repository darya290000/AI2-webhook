from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("✅ Webhook کد دریافت شد:")
    print(data)
    return jsonify({"status": "✅ success"}), 200

@app.route('/')
def home():
    return "🚀 Webhook آماده است"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
