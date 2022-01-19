import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

#style of background
st.markdown(
	"""
	<style>
	.main{
	background-color:F5F5F5;
	}
	</style>
	""",
	unsafe_allow_html=True
)


#caching to boost dataset work
@st.cache
def get_data(filename):
	df = pd.read_csv(filename)

	return df

with header:
	st.title('Welcome to Storke Prediction Project')
	st.text('This project aimed to predict stroke for people by analyzing a dataset found\nin Kaggle using different machine learning models(MLs) to help the medical staff to\nrecognize those people with stroke. The used dataset was trained and get 96%\naccuracy as the highest value of the different used models.')


with dataset:
	st.header('Stroke Prediction Dataset')
	st.text('The dataset is available in .csv format. It consists of 5110 observations/data\npoints with 12 attributes or features. From exploratory data analysis, the age\nfeature has an important role in stroke prediction which most models deployed\nconfirmed afterwards. Other features were not definately if\nthey are important due to the imbalanced dataset that has been treated\nwith Synthetic Minority Oversampling Technique (SMOTE).\nAnother important feature of this project is the label of the stroke whether\nthe person is predicted with a stroke or not.')
	st.subheader('imbalanced dataset')
	df = get_data('data/healthcare-dataset-stroke-data.csv')
	imb_stroke_vis = pd.DataFrame(df['stroke'].value_counts()).head(30)
	st.bar_chart(imb_stroke_vis)
	#st.write(df.head(5))	
	imb_stroke_vis

	st.subheader('Oversampled (SMOTE) balanced dataset')
	df2 = pd.read_csv('data/Stroke_Dataset_with_Smote.csv')
	b_stroke_vis = pd.DataFrame(df2['stroke'].value_counts()).head(30)
	st.bar_chart(b_stroke_vis)
	#st.write(df2.head(5))	
	b_stroke_vis

with features:
	st.header('The created features')

	st.markdown(' * ** age:** it was considered as an important feature due to its trending')
	st.markdown(' * ** avg_glucose_level:**  is getting higher from 150 onwards')
	st.markdown(' * ** gender:**  it was noticed that women gets more stroke than men')


with model_training:
	st.header('Time to train the model')
	st.text('here you get to choose the hyperparameters of \nthe model and see how the perfomance changes')

	sel_col, disp_col = st.columns(2)

	max_depth = sel_col.slider('what should be the max_depth of the model?', min_value=10, max_value=100, value=20, step=10)

	n_estimators = sel_col.selectbox('how many trees should there be?', options=[100,200,300,'No limit'], index = 0) # default value is 0


	sel_col.text('Here is a list of features in dataset:')
	sel_col.write(df.columns)
	input_features = sel_col.text_input('which feature should be used as the input feature?','stroke')
    
    
	#if n_estimators == 'No limit':
	#	rfc = RandomForestClassifier(max_depth=max_depth)
	#else:
	#	rfc = RandomForestClassifier(max_depth=max_depth, n_estimators=n_estimators)

	# random forest classifer
	rfc = RandomForestClassifier(max_depth=max_depth, n_estimators=n_estimators)

	X = df[[input_features]]
	y = df[['stroke']]

	rfc.fit(X, y)
	prediction = rfc.predict(y)

	disp_col.subheader('Mean absolute error of the model is:')
	disp_col.write(mean_absolute_error(y,prediction))

	disp_col.subheader('Mean squared error of the model is:')
	disp_col.write(mean_squared_error(y,prediction))

	disp_col.subheader('R squared of the model is:')
	disp_col.write(r2_score(y,prediction))

