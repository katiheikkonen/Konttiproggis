from flask import Flask, jsonify
import scan_table

app = Flask(__name__)

@app.route('/')

def get_items():
    return jsonify(scan_table.get_items())

if __name__ == '__main__':
    app.run()