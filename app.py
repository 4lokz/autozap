from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(data)  # Aqui você pode processar os dados recebidos
    return 'Webhook received!', 200

if __name__ == '__main__':
    app.run(debug=True)
