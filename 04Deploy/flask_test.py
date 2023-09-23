# Only for testing the flask package

from flask import Flask

app = Flask('test')


#Registers the /ping route, and assigns it to the ping function
@app.route('/ping', methods = ['GET'])
def ping():
    return "ping"

if __name__ == '__main__':
    
    #To test it, open the browser and type 'localhost:9696/ping'   
    app.run(debug=True, host='0.0.0.0', port=9696)