from flask import Flask, request

app = Flask(__name__)

all_pseudos = []
all_messages = []

@app.route('/motd', methods=['GET'])
def motd():
    return "Hello", 200, {'Content-Type': 'text/plain; charset=utf-8'}

@app.route('/nick', methods=['POST'])
def nick():
    if not request.is_json:
        return "Non JSON request", 400

    try:
        data = request.get_json(silent=True)
        pseudo = data.get("pseudo")
        all_pseudos.append(pseudo)
    except Exception:
        # TO DO : add a more specific exception
        return "Invalid data", 400

@app.route('/nick', methods=['POST', 'GET'])
def msg():
    if request.method == 'GET':
        return f"{all_messages}", 200, {'Content-Type': 'text/plain; charset=utf-8'}

    if request.method == 'POST':
        if not request.is_json:
            return "Requête invalide : contenu non-JSON", 400

        try:
            data = request.get_json(silent=True)
            author = data.get("from")
            message = data.get("message")
            all_pseudos.append((author, message))
        except Exception:
            # TO DO : add a more specific exception
            return "Invalid data", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
