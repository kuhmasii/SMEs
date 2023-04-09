# from keras import backend as K
# import joblib
# import numpy as np
# import pandas as pd
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