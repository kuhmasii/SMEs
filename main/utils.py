# from keras import backend as K
# import joblib
# import numpy as np
import plotly.express as px
import pandas as pd
import numpy as np
# from pathlib import Path


# def ohevalue(df):
# 	ohe_col=joblib.load(Path("main") / "model/model1.pkl")
# 	cat_columns=['Gender','Married','Education','Self_Employed','Property_Area']
# 	df_processed = pd.get_dummies(df, columns=cat_columns)
# 	newdict={}
# 	for i in ohe_col:
# 		if i in df_processed.columns:
# 			newdict[i]=df_processed[i].values
# 		else:
# 			newdict[i]=0
# 	newdf=pd.DataFrame(newdict)
# 	return newdf

# def approvereject(unit):
# 	try:
# 		mdl=joblib.load(Path("main") / "model/loan_model.pkl")
# 		scaler=joblib.load(Path("main") / "model/ML_Model.pkl")
# 		X=scaler.transform(unit)
# 		y_pred=mdl.predict(X)
# 		y_pred=(y_pred>0.58)
		
# 		newdf=pd.DataFrame(y_pred, columns=['Status'])
# 		newdf=newdf.replace({True:'Approved', False:'Rejected'})
# 		K.clear_session()
# 		return (newdf.values[0][0],X[0])
# 	except ValueError as e:
# 		return (e.args[0])

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

