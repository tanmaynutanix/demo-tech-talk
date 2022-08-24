from flask import Flask
from flask import request,jsonify,make_response
 
app = Flask(__name__)
 
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
      jsonify({"data":"Well, Hello there from server 1!"}),200
      )
    response1.headers["Content-Type"] = "application/json"
    return response1

@app.route('/allowed_endpoint')
def allowed_endpoint():
    
    response2 = make_response(
      jsonify({"data":"You have access to server 1 allowed endpoint!"}),200
      )
    response2.headers["Content-Type"] = "application/json"
    return response2

@app.route('/disallowed_endpoint')
def disallowed_endpoint():
    
    response3 = make_response(
      jsonify({"data":"You have access to server 1 disallowed endpoint!"}),200
      )
    response3.headers["Content-Type"] = "application/json"
    return response3

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port = 5001)