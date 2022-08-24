from flask import Flask
from flask import request,jsonify,make_response
import requests
 
app = Flask(__name__)

URL1 = "http://0.0.0.0/server1/allowed_endpoint" 
URL2 = "http://0.0.0.0/server1/disallowed_endpoint"

@app.before_request
def log_request_info():
    app.logger.debug('Request: %s', request.get_json())
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())

@app.after_request
def after(response):
    app.logger.debug('Response: %s', response.get_json())
    app.logger.debug('Status Code: %s', response.status)
    app.logger.debug('Headers: %s', response.headers)
    app.logger.debug('Body: %s', response.get_data())
    return response

@app.route('/')
def hello_world():
    
    response1 = make_response(
        jsonify({"data":"Well, Hello there from server 2!"}),200
        )
    response1.headers["Content-Type"] = "application/json"
    return response1

@app.route('/allowed_endpoint')
def allowed_endpoint():
    r2 = requests.get(url = URL1)
    data2 = r2.json()
    return data2

@app.route('/disallowed_endpoint')
def disallowed_endpoint():
    r2 = requests.get(url = URL2)
    data2 = r2.json()
    return data2
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0' , port = 5002)