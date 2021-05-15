import os
import numpy as np 
import pandas as pd 
import pickle
import tensorflow as tf 
import tensorflow.keras.models
from tensorflow.keras.models import model_from_json
import streamlit
import re
from tensorflow import keras

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

VOCAB_SIZE = 1000

# Loading in model
# json_file = open('model.json', 'r')
# loaded_model_json = json_file.read()
# json_file.close()
# lstm_model = model_from_json(loaded_model_json)

# lstm_model.load_weights("model.h5")
lstm_model = keras.models.load_model('model/')


# Prediction function
def sentiment_prediction(review):
	sentiment=[]
	input_review= review
	# input_review = [x.lower() for x in input_review]
	# input_review = [re.sub('[^a-zA-z0-9\s]','',x) for x in input_review]
	sentiment = lstm_model.Predict(np.array([input_review]))

	if(sentiment>0.0):
		pred="Positive"
	else:
		pred="Negative"
	return pred

# UI
def run():
	streamlit.title("Sentiment Analysis - LSTM Model")
	html_temp="""
	"""
	streamlit.markdown(html_temp)
	review=streamlit.text_input("Enter the Review ")
	prediciton=""
	if (streamlit.button("Predict Senitment")):
		pass
	streamlit.success("The sentiment predicted by the Model : {}".
		format(prediciton))

if __name__ == '__main__':
	run()
