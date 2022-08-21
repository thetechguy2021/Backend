from flask import Flask_request
from flask_restful import Resource, Api
import pickle
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
#
CORS (app)
#create an API object
api = Api(app)

#prediction api call
class prediction(Resource):
    def get(self, city):

    #city = request.args.get('budget')
    print(city)

 #Loading package
 df = pd.DataFrame(city, columns =['CityOfRide', 'Distance', 'NumOfPassengers', 'PaymentType'])
 model = pickle.load(open('taxifare_prediction_model.pkl', 'rb'))
prediction = model.predict(df)
return str(prediction)

#Data API
class getData(Resource):
    def get(self):
        df = pd.read_excel('data.csv')
        df = _df.rename({'CityOfRide':'City', 'Distance':'Distance in KM', 'NumOfPassengers':'No. of Passengers', 'PaymentType': 'Type of Payment'}) #Rename the columns
       #print(df.head())
    #out = {'key':str}
    res = df.to.json(orient = 'records')

    #print (res)
    return res

api.add_resource(getData, '/api')
api.add_resource(prediction, '/prediction/<int:taxifare>')

if __name__ = 'main':
    app.run(debug=True)