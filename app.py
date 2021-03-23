from flask import Flask,request,jsonify,request
from flask_restful import Api,Resource,reqparse

from transformers import pipeline



app=Flask(__name__)
api=Api(app)


@app.route('/api/',methods=['POST'])
def post():
   data=reqparse.RequestParser()
   data.add_argument('text')
   args=data.parse_args()
   translator = pipeline("translation_en_to_fr")
   data=translator(args['text'],max_length=40)
   return {'out':data[0]['translation_text']}



if __name__=='__main__':
   app.run(debug=True,host='0.0.0.0')


