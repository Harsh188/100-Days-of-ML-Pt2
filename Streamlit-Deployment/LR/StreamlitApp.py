import pandas as pd
import numpy as np
import joblib
import streamlit

model=open("linear_regression_model.pkl", "rb")
lr_model=joblib.load(model)

def lr_prediction(alc,vol,sul,dio):
	pred_arr=np.array([alc,vol,sul,dio])
	preds=pred_arr.reshape(1,-1)
	preds=preds.astype(np.float64)
	model_predction=lr_model.predict(preds)
	return model_predction

def run():
	streamlit.title("Linear Regression Model")
	html_temp="""
	"""
	streamlit.markdown(html_temp)
	alc=streamlit.text_input("Alcohol")
	vol=streamlit.text_input("volatile acidity")
	sul=streamlit.text_input("sulphates")
	dio=streamlit.text_input("total sulfur dioxide")

	prediction=""

	if streamlit.button("predict"):
		prediction=lr_prediction(alc,vol,sul,dio)

	streamlit.success("The prediction by Model : {}".format(prediction))

if __name__ == '__main__':
	run()

# 8.8, 0.27, 0.45, 45