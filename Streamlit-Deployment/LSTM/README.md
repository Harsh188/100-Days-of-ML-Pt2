# Streamlit App

## Description ##

Using streamlit I was able to host my deep learning LSTM Model on a local machine.

To run the application I used a docker container.

docker run --gpus all -it --rm -p 8501 -v $PWD:/tmp huggingface/transformers-tensorflow-gpu

export LC_ALL=C.UTF-8
export LANG=C.UTF-8
