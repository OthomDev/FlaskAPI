from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import error 

app = Flask(__name__)
api = Api(app)

class Add(Resource):
    def post(self):

        PostedData = request.get_json()
        if error.Error(PostedData) != 200:
            retJson={
                "Status Code": 301,
                "Error": "Missing Data(needs two values for add)"
            }
            return jsonify(retJson)

        x = PostedData["x"]
        y = PostedData["y"]
        z = x + y

        resJSON = {
            "Status Code" : 200,
            "z" : z 
        }
        return jsonify(resJSON)
    
class Sub(Resource):
    def post(self):
        PostedData = request.get_json()
        if error.Error(PostedData) != 200:
            retJson={
                "Status Code": 301,
                "Error": "Missing Data (needs two values for sub)"
            }
            return jsonify(retJson)
        x = PostedData['x']
        y = PostedData['y']
        z = x - y

        resJSON = {
            "Status Code": 200,
            "z": z
        }
        return jsonify(resJSON)
    
class Multiply(Resource):
    def post(self):
        PostedData = request.get_json()
        if error.Error(PostedData) != 200:
            retJson = {
                "Status Code": 301,
                "Error": "Missing value(needs two values to do multiplication)"
            }
            return jsonify(retJson)
        x = PostedData['x']
        y = PostedData['y']
        z = x*y

        resJson = {
            "Status Code": 200,
            "z" : z
        }
        return jsonify(resJson)

class Division(Resource):
    def post(Self):
        postedData = request.get_json()
        if error.Error(postedData) != 200:
            retJson = {
                "Status Code": 301,
                "Error": "There is a missing value (to do the division you need two value)"
            }
            return jsonify(retJson)
        elif postedData['y'] == 0:
            retJson = {
                "Status Code": 302,
                "Error": "Division on 0 is a math error" 
            }
        else:
            x = postedData["x"]
            y = postedData["y"]
            z = x/y
            resJson = {
                "Status Code": 200,
                "z": z
            }
            return jsonify(resJson)

api.add_resource(Add, "/add")
api.add_resource(Sub, '/sub')
api.add_resource(Multiply, '/mul')
api.add_resource(Division, '/div')



if __name__=="__main__":
    app.run(host='0.0.0.0')
