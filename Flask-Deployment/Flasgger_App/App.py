from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle
import joblib
from flasgger import Swagger


app = Flask(__name__)
Swagger(app)

model=open("linear_regression_model.pkl", 'rb')
lr_model = joblib.load(model)

@app.route('/predict', methods=['GET','POST'])
def predict():
	"""Returns the predicted value from the ML model
	---
	parameters:
		- name: alcohol
		  in: query
		  type: number
		  required: true
		- name: volatile acidity
		  in: query
		  type: number
		  required: true
		- name: sulphates
		  in: query
		  type: number
		  required: true
		- name: total sulfur dioxide
		  in: query
		  type: number
		  required: true

	responses:
		500:
			description: Prediction
	"""
	if request.method=='POST':
		print(request.args.get('alcohol'))
		print(request.args.get('volatile acidity'))
		print(request.args.get('sulphates'))
		print(request.args.get('total sulfur dioxide'))
		try:
			alc = float(request.args.get('alcohol'))
			vol = float(request.args.get('volatile acidity'))
			sul = float(request.args.get('sulphates'))
			dio = float(request.args.get('total sulfur dioxide'))

			pred_arg=[alc,vol,sul,dio]
			pred_arg=np.array(pred_arg)
			pred_arg=pred_arg.reshape(1,-1)
			try:
				model_pred = lr_model.predict(pred_arg)
				model_pred = round(float(model_pred), 2)

			except Exception as e:
				return str(e) 

		except ValueError:
				return "Please Enter valid values"

	return str("The predicted value is: "+ str(model_pred))

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')