# Stroke_Prediction
[![Follow @StrokePred on Twitter](https://img.shields.io/twitter/follow/strokepred?style=social)](https://twitter.com/StrokePred)

<img src="https://topnews.in/healthcare/sites/default/files/styles/large/public/Stroke7.jpg?itok=xInaWFYK" width="200" height="200">

# Stroke Prediction
Jefn Alshammari & Abdulaziz Almass
## Abstract
This project aimed to predict stroke for people by analyzing a dataset found in [Kaggle](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset) using different machine learning models(MLs) to help the medical staff to recognize those people with stroke. The used dataset was trained and get 96% accuracy as the highest value of the different used models.  

<!-- The data has been explored, cleaned and One-Hot-Encoding for some of the features such as "gender" ...etc.  -->

## Design

This project is one of the T5 Data Science BootCamp requirements. Data provided by Kaggle has been used in this project. The attribute "Stroke" is the label or target to be predicted in this project. This target is binary having either 1 or 0 as a value. The value of "1" means predicted with stroke and "0" means predicted without a stroke. This classifcation prediction is deployed using various machine learning models and a comparison of these models is done to measure of performance for each model to find the one that fits with the selected dataset. All of the following models have been used and tested: Logistic Regression, K-Nearest Neighbors (KNN), Decision Tree,  Support-Vector Machines (SVM),Random Forest and XGBoost.  

## Data 

The dataset is available in ```.csv``` format. It consists of 5110 observations/data points with 12 attributes or features. From exploratory data analysis, the age feature has an important role in stroke prediction which most models deployed confirmed afterwards. Other features were not definately if they are important due to the imbalanced dataset that has been treated with Synthetic Minority Oversampling Technique (SMOTE). Another important feature of this project is the label of the stroke whether the person is predicted with a stroke or not.


***Models***

Logistic Regression, K-Nearest Neighbors (KNN), Decision Tree, Support-Vector Machines (SVM),Random Forest and XGBoost are trained to predict stroke. The Random Forest has the highiest accuracy.

***Models Evaluation and Selection***

The following metrics summarize the results of all ML models used in this project : 


|                     |                | Macro Avg | Accuracy | Precision |   Recall  |  F1 Score | Stroke |
|---------------------|----------------|:---------:|:--------:|:---------:|:---------:|:---------:|:------:|
| Logistic Regression |   Imbalanced   |    0.50   |   0.92   | 0.93<br> 0.00 | 1.00<br> 0.00 | 0.96<br> 0.00 |   0<br> 1  |
| Logistic Regression |   Not Scaled   |    0.91   |   0.90   | 0.89<br> 0.92 | 0.93<br> 0.89 | 0.91<br> 0.90 |   0<br> 1  |
| Logistic Regression |     Scaled     |    0.92   |   0.91   | 0.88<br> 0.97 | 0.97<br> 0.87 | 0.92<br> 0.92 |   0<br> 1  |
| Logistic Regression | Tuned & Scaled |    0.92   |   0.91   | 0.89<br> 0.94 | 0.94<br> 0.89 | 0.92<br> 0.91 |   0<br> 1  |
|         KNN         |     Scaled     |    0.94   |   0.94   | 0.96<br> 0.93 | 0.93<br> 0.96 | 0.94<br> 0.94 |   0<br> 1  |
|    Decision Tree    |     Scaled     |    0.92   |   0.92   | 0.94<br> 0.91 | 0.90<br> 0.95 | 0.92<br> 0.93 |   0<br> 1  |
|         SVM         |   Not Scaled   |    0.92   |   0.92   | 0.89<br> 0.96 | 0.97<br> 0.88 | 0.92<br> 0.92 |   0<br> 1  |
|         SVM         |     Scaled     |    0.92   |   0.92   | 0.88<br> 0.97 | 0.97<br> 0.87 | 0.92<br> 0.92 |   0<br> 1  |
|    Random Forest    |     Scaled     |    0.97   |   0.96   | 0.96<br> 0.97 | 0.97<br> 0.96 | 0.97<br> 0.97 |   0<br> 1  |
|       XGBoost       |     Scaled     |    0.93   |   0.93   | 0.91<br> 0.95 | 0.95<br> 0.91 | 0.93<br> 0.93 |   0<br> 1  |


## Tools

- Pandas library for data frames
- Numpy for mathematical operations
- Matplotlib and Seaborn for plots
- SKlearn for modeling
- One-Hot-Encoding for categorical labeling
- Imblearn
- Plotly
- Seaborn
- XGBoost

## Communication

The presentation show is provided [here](https://github.com/jefnkhalaf/Stroke-Prediction/edit/main/Final_Phase/Presentation.pdf), besides details are provided at the [readme](https://github.com/jefnkhalaf/Stroke-Prediction/blob/main/README.md) of the project.
for any enquiries, you can contact us via [Email]( mailto:jefnkhalaf@gmail.com) or Twitter via [![Follow @StrokePred on Twitter](https://img.shields.io/twitter/follow/strokepred?style=social)](https://twitter.com/StrokePred)
