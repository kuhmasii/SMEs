from sklearn import preprocessing
import plotly.express as px
from sklearn import metrics
from pathlib import Path
import pandas as pd
import numpy as np
import joblib

import warnings
warnings.filterwarnings('ignore')

def clean_data(test_data):
	
	# changing all categorical data to binary.
	test_data["Gender"] = [1 if x == "Male" else 0 for x in test_data["Gender"]]
	test_data["Education"] = [1 if x == "Graduate" else 0 for x in test_data["Education"]]
	test_data["Self_Employed"] = [1 if x == "Yes" else 0 for x in test_data["Self_Employed"]]
	test_data["Married"] = [1 if x == "Yes" else 0 for x in test_data["Married"]]
	test_data["Property_Area"] = [1 if x == "Urban" else 0 for x in test_data["Property_Area"]]
	test_data['Credit_History'] = [1 if x == 1. else 0 for x in test_data['Credit_History']]  
	return test_data


def check_loan_status(x_test):
	
	try:
		# 'Y' == 1 means Loan status approved
		# 'N' == 0 means Loan status rejected
		# using random forest classifier model
		rfc = joblib.load(Path("main") / "ML_models/rfc.pkl")
		# using logistic regression model
		lc = joblib.load(Path("main") / "ML_models/lc.pkl")
		random_forest_prediction = rfc.predict(x_test)
		logistic_prediction = lc.predict(x_test)
		print(random_forest_prediction, logistic_prediction)
		if random_forest_prediction == [1]:
			return {"status":"Approved"}
		return {"status":"Failed"}
	except:
		return None

def clean_file(file, labels_, data_, indicate_=None):

	try:
		# cleaning data
		data = pd.read_csv(f'{file.file.path}')
		data.replace(0, np.nan, inplace=True)
		data.replace(' ', np.nan, inplace=True)
		data.dropna(inplace=True)

		col = labels_.split(",")
		if len(col) > 1:
			labels_ = col 

		if isinstance(labels_, str) and not labels_ in data.columns.values:
			return None
		
		if not data_ in data.columns.values:
			return None

		if indicate_ and indicate_ not in data.columns.values:
			return None 

		if isinstance(labels_, list):
			for l in labels_:
				if l not in data.columns.values:
					return None

		if indicate_:
			fig = px.histogram(data,  x=data_, y=labels_, title=f"Graph of {data_} against {labels_}",
					labels={'x':data_, 'y':labels_}, height=1000, color=indicate_)
		else:
			fig = px.histogram(data,  x=data_, y=labels_, title=f"Graph of {data_} against {labels_}", 
				labels={'x':data_, 'y':labels_}, height=1000)
		

		return fig.to_html(full_html=True, include_plotlyjs=False)
	except:
		return None

