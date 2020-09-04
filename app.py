from flask import Flask, jsonify
import student_controller

app = Flask(__name__)

@app.route('/')

def get_items():
    return jsonify(student_controller.get_items())

if __name__ == '__main__':
    app.run()