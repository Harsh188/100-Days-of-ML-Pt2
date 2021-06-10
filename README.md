# 100-Days-of-ML-Pt2

Daily log to track my progress on the 100 days of ML code challenge.

## Description ##

100 Day ML Challenge to learn and develop machine learning products. Since this is my second time performing this challenge, this time around I will be focusing more on the production enviroment rather than the concepts and theory behind ML/DL models. I will be placing heavy emphasis on the ML pipeline and the process of taking an ML model and applying into a real-world application.

## Challenge Goals ##

- [x] Learn how to deploy ML models into production.
- [x] Learn about scripting for MLOps
- [x] Learn about the ML Pipeline
- [ ] Learn more about privacy & protection for ML applications
- [x] Learn the CI/CD for ML
- [ ] Learn about CUDA and get hands on experience
- [ ] Learn more about deep reinforcement learning
	- [x] Markov Chains
	- [ ] Markov Decision Processes
- [ ] Learn more about generative learning
- [ ] Learn about AWS microservices

[Additional]
- Milti-modal Systems
- Apache Flume
- [x] Apache Beam
- MySQL/Apache Spark
- PostgreSQL
- Optimizing/architecting software/hardware solutions for ML

## Resources ##

### Books ###

Deploy Machine
Learning Models
to Production
With Flask, Streamlit, Docker, and
Kubernetes on Google Cloud Platform

Building Machine
Learning Powered
Applications
Going from Idea to Products

Building
Machine Learning
Pipelines
Automating Model Life Cycles
with TensorFlow

Hands-On GPU Programming with Python and CUDA: Explore High-performance Parallel Computing with CUDA

### Web Resources ###

- [Made with ML](https://madewithml.com/courses/mlops/)

@article{madewithml,
    title  = "MLOps - Made With ML",
    author = "Goku Mohandas",
    url    = "https://madewithml.com/courses/mlops/organization/"
    year   = "2021",
}

## Youtube Log ##

This whole challenge will be documented on youtube during live streams. The link to the playlist: [100 Days of ML](https://www.youtube.com/playlist?list=PLJC9FdR4qnfiTDFDHAiDsxJwvttoFqGS8)

## Daily Goals ##

<h3>Day 1: Deploy a Linear Regression model using FLASK</h3>
<ul>
	<li>Develop a web application using FLASK</li>
	<li>Code a linear regression model</li>
	<li>Deploy the trained model as a REST service</li>
</ul>
<h3>Day 2: Deploy a Linear Regression model using Streamlit</h3>
<ul>
	<li>Read the section about streamlit</li>
	<li>Create UI using streamlit</li>
	<li>Deploy the trained model as a REST service</li>
	<li>code LSTM model</li>
</ul>
<h3>Day 3: Deploy a Deep Learning model using Streamlit</h3>
<ul>
	<li>Train the LSTM model</li>
	<li>Create UI using streamlit</li>
</ul>
<h3>Day 4: Deploy a Deep Learning model using Streamlit</h3>
<ul>
	<li>Deploy the trained model as a REST service</li>
	<li>Read Chapter 4: ML Deployment using Docker</li>
</ul>
<h3>Day 5: Deploy ML model using Docker</h3>
<ul>
	<li>Create a dockerfile for Flask App</li>
	<li>Create Docker image</li>
	<li>Push our Docker image to DockerHub</li>
</ul>
<h3>Day 6: ML Deployment using Kubernetes</h3>
<ul>
	<li>Read chapter 5: ML Deployment using Kubernetes</li>
	<li>Create GCP Project</li>
	<li>Enable and utilize the Kubernetes Engine API on GCP</li>
</ul>
<h3>Day 7: Scripting</h3>
<ul>
	<li>Read topics under scripting from MadeWithML</li>
	<li>Apply learning by adding it to current projects</li>
</ul>
<h3>Day 8: Reading Building ML Pipelines</h3>
<ul>
	<li>Read Ch1: Introduction</li>
	<li>Read Ch2: Introduction to TensorFlow Extended</li>
</ul>
<h3>Day 9: Reading Building ML Pipelines</h3>
<ul>
	<li>Read Ch2: Introduction to TensorFlow Extended</li>
	<li>Read Ch3: Data Ingestion</li>
</ul>
<h3>Day 10: TFX Setup</h3>
<ul>
	<li>Download and setup TFX</li>
	<li>Execute TFX Data Ingestion examples</li>
</ul>
<h3>Day 11: TFX Data Ingestion</h3>
<ul>
	<li>Follow [TFX tutorial](https://www.tensorflow.org/tfx/tutorials/tfx/penguin_simple#install_tfx)</li>
</ul>
<h3>Day 12: TFX Data Ingestion</h3>
<ul>
	<li>Try using Colab</li>
	<li>Check online resources and try to debugg [TFX tutorial](https://www.tensorflow.org/tfx/tutorials/tfx/penguin_simple#install_tfx)</li>
</ul>
<h3>Day 13: Reading Building ML Pipelines</h3>
<ul>
	<li>Read Ch4: Data Validation</li>
	<li>Read online resources on TFX Data Validation</li>
</ul>
<h3>Day 14: Data Validation</h3>
<ul>
	<li>Read online resources on TFX Data Validation</li>
	<li>Execute example code for TFVD</li>
</ul>
<h3>Day 15: Reading Building ML Pipelines</h3>
<ul>
	<li>Read Ch5: Data Preprocessing</li>
	<li>Read online resources on TFX Data Preprocessing</li>
</ul>
<h3>Day 16: Data Preprocessing</h3>
<ul>
	<li>Read more about feature engineering</li>
	<li>Feature engineering vs ML engineering</li>
	<li>Execute example code for TF Transform</li>
</ul>
<h3>Day 17: MLOps Production</h3>
<ul>
	<li>Read about production from [Made with ML](https://madewithml.com/courses/mlops/)</li>
	<li>Watch youtube videos on CI/CD workflows</li>
	<li>Learn more about Github Actions </li>
</ul>
<h3>Day 18: Reading Building ML Pipelines</h3>
<ul>
	<li>Read Ch 6: Model Training</li>
	<li>Read online resources on TFX Trainer Component</li>
</ul>
<h3>Day 19: Reading Building ML Pipelines</h3>
<ul>
	<li>Read Ch 7: Model Analysis and Validation</li>
	<li>Read online resources on TF Model Analysis</li>
</ul>
<h3>Day 20: Reading Building ML Pipelines</h3>
<ul>
	<li>Read Ch 8: Model Deployment with TensorFlow Serving</li>
</ul>
<h3>Day 21: Reading Building ML Pipelines</h3>
<ul>
	<li>Continue reading Ch8: Model Deployment with TensorFlow Serving</li>
	<li>Read online resources on TF Serving</li>
</ul>
<h3>Day 22: Plan out an ML Product to Build</h3>
<ul>
	<li>Look into simple ML models to deploy</li>
	<li>Create the architecture for the pipeline</li>
	<li>Setup/Decide on github project organization</li>
	<li>Choose how to build front-end</li>
	<li>What orchestration tool to use?</li>
</ul>
<h3>Day 23: Plan out an ML Product to Build</h3>
<ul>
	<li>How to integrate CI/CD into project</li>
	<li>FLASK Web deployment vs Model Server</li>
	<li>Create order of events</li>
	<li>Look into setting up GitHub Project</li>
</ul>
<h3>Day 24: Build Dockerfile for ML Project</h3>
<ul>
	<li>List out dependencies</li>
	<li>Create Dockerfile</li>
	<li>Build Docker Image</li>
	<li>Run Docker container</li>
	<li>Check if GPU is being used</li>
</ul>
<h3>Day 25: Build Dockerfile for ML Project</h3>
<ul>
	<li>Troubleshoot Dockerfile</li>
	<li>Build Docker Image</li>
	<li>Update README.md</li>
</ul>
<h3>Day 26: Setup TFX Pipeline Architecture</h3>
<ul>
	<li>Setup TFX pipeline</li>
	<li>Design TFX architecture</li>
</ul>
<h3>Day 27: TFX Pipeline</h3>
<ul>
	<li>Understand the template code</li>
	<li>Clear out the template files and rewrite the pipeline</li>
</ul>
<h3>Day 28: Import Data</h3>
<ul>
	<li>Change permissions for files in /ml</li>
	<li>Add the IMDB datset into /data</li>
	<li>Convert dataset to desired format</li>
</ul>
<h3>Day 29: Add Formating/Styling</h3>
<ul>
	<li>Setup formating/styling</li>
	<li>Black & flake8</li>
	<li>Setup github actions</li>
</ul>
<h3>Day 30: Data Validation</h3>
<ul>
	<li>Fix features.py</li>
	<li>Generate statistics</li>
	<li>Visualize statistics</li>
	<li>Infer schema</li>
</ul>
<h3>Day 31: Troubleshooting Data Ingestion/Validation</h3>
<ul>
	<li>Figure out why example gen is not loading</li>
</ul>
<h3>Day 32: Data Preprocessing</h3>
<ul>

</ul>