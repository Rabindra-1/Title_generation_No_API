from flask import Flask, request, jsonify
from generator import generate_blog
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def api_generate():
    topic = request.json['topic'] # type: ignore
    blog = generate_blog(topic)
    return jsonify({'blog': blog})

if __name__ == '__main__':
    app.run(debug=True)