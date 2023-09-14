from flask import current_app as app
from flask import request
from flask_restful import Resource, Api
from flask import jsonify
import random
api = Api(app)


    

class Predictions(Resource):
    def post(self):
        
        img = request.files["image"]
        # res = model.predict(Image.open(img))

        return jsonify({
            "prediction": random.randint(1, 10),
            "message": "success"
        })


api.add_resource(Predictions, "/getPredictions")