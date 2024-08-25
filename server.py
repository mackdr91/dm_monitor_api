from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

computer_info_data = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/computer_info', methods=['POST'])
def computer_info():
    computer_info_data = request.get_json()
    print(f'Received data: {computer_info_data=}')
    return jsonify({

        "status": 200,
        "success": True,
        "data": computer_info_data,
        "message": "Data received successfully"

        })

@app.route('/computer_info', methods=['GET'])
def get_computer_info():
    return jsonify(computer_info_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)