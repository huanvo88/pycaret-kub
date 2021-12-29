## A Simple MLOps Project: Build and Deploy a Customer Churn Model

This is a simple MLOps project that aims to build and deploy a simple machine learning model, namely a customer churn model. I combine several popular open-sourced data science packages: [pycaret](https://pycaret.org/), [pandas-profiling](https://github.com/pandas-profiling/pandas-profiling), [MLflow](https://mlflow.org/), [Streamlit](https://streamlit.io/), and finally deploy on [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine)

Most of the codes are taken from this repo [pycaret-streamlit-google](https://github.com/pycaret/pycaret-streamlit-google), written by [Moez Ali](https://ca.linkedin.com/in/profile-moez), the creator of pycaret. One can clone this repository and follow the instructions in the article 
[Deploy Machine Learning App on GKE](https://towardsdatascience.com/deploy-machine-learning-app-built-using-streamlit-and-pycaret-on-google-kubernetes-engine-fd7e393d99cb) in order to deploy the model on GKE. In order to avoid unneccessary errors, the project name on GKE should be the same as the name of your repo, and remember to enable the relevant Google APIs. 

One can take a look at the finished app here http://34.94.20.18/ (hosted on Google Cloud Platform). Please be reasonable and do not overload the server. This is meant as a learning project, not a production environment. 

The main jupyter notebook is [main_notebook.ipynb](main_notebook.ipynb)

One can take a look at the pandas-profiling report of the data here [data_profiling.html](data_profiling.html)

In order to launch the MLflow UI locally, follow the steps: 

* clone the project
* create the python env based on the requirements.txt file (for pycaret, use the [full] option)
* activate the environment
* cd to the cloned project folder
* run the command: **mlflow ui --backend-store-uri sqlite:///mlruns.db**
* go to **http://localhost:5000** to view the results

In order to launch the deployment ui locally, after doing the first four steps as above, instead running the command

* run the command: **streamlit run app.py**
* go to **http://localhost:8501** to view the results

