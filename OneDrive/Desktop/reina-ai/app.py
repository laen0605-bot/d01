from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    user_message = data["userRequest"]["utterance"]

    print(user_message)

    return jsonify({
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "......레이나가 바라본다."
                    }
                }
            ]
        }
    })

app.run(host="0.0.0.0", port=3000)