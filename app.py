from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    message = os.environ.get('APP_MESSAGE', 'Hello from Flask App!')
    return f'<h1>{message}</h1><p>This is version 1.0 of our awesome app.</p>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)