from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


@app.route('/api/question', methods=['POST'])
def get_answer():
    question = request.json['question']
    answer = "default lorem ipsum"
    return jsonify({'answer': answer})

@app.route('/api/question')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
