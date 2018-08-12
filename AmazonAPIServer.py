from flask import Flask, jsonify, request
import random

app = Flask(__name__)
idJson = {"Id":0}
soldJson = {"sold": False}

@app.route("/amazonAPI/register-request", methods=['POST'])
def register_request():
	new_id = random.randint(1, 1000000)
	idJson["Id"] = new_id
	return jsonify(idJson)
 
@app.route("/amazonAPI/request-data/<req_id>", methods=['GET'])
def get_request(req_id):
	if int(req_id)%2 == 0:
	    new_sold  = True
	else:
	    new_sold = False
	soldJson["sold"] = new_sold
	return jsonify(soldJson)

if __name__ == '__main__':
    app.run()

