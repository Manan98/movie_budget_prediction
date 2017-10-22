from flask.ext.cors import CORS
from flask import Flask
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
#import httplib, urllib
#params = urllib.urlencode({'action': 'getbacon', 'account': '1234'})
#headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
# conn = httplib.HTTPSConnection("server.com:8443")
# conn.request("POST", "/kitchen/query", params, headers)
# response = conn.getresponse()
#print response.status, response.reason
#200 OK
#>>> data = response.read()
#>>> conn.close()
@app.route('/get_data', methods=['POST'])
def get_data():
    dat = request.get_json()
    
    return "hello world!"



if __name__=="__main__":
    app.run("0.0.0.0", port=5010)
