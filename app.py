from flask import Flask
from waitress import serve

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the Flask application with Waitress
if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
