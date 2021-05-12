from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import sklearn
import joblib

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('home.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
	if request.method=='POST':
		print(request.form.get('alcohol'))
		print(request.form.get('volatile acidity'))
		print(request.form.get('sulphates'))
		print(request.form.get('total sulfur dioxide'))
		try:
			alc = float(request.form.get('alcohol'))
			vol = float(request.form.get('volatile acidity'))
			sul = float(request.form.get('sulphates'))
			dio = float(request.form.get('total sulfur dioxide'))

			pred_arg=[alc,vol,sul,dio]
			pred_arg=np.array(pred_arg)
			pred_arg=pred_arg.reshape(1,-1)

			model=open("linear_regression_model.pkl", 'rb')
			lr_model = joblib.load(model)

			try:
				model_pred = lr_model.predict(pred_arg)
				model_pred = round(float(model_pred), 2)

			except Exception as e:
				return str(e) 

		except ValueError:
				return "Please Enter valid values"

	return render_template('predict.html', prediction=model_pred)


if __name__ == '__main__':
	app.run(debug=True)