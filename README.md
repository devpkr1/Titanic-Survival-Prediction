# Titanic Survival Prediction

This project involves analyzing the famous Titanic dataset to predict passenger survival using various machine learning models. The goal was to achieve the highest prediction accuracy possible.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Feature Engineering](#feature-engineering)
- [Model Building](#model-building)
- [Model Evaluation](#model-evaluation)
- [Kaggle Submission](#kaggle-submission)
- [Conclusion](#conclusion)
- [How to Run the Project](#how-to-run-the-project)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## Project Overview
The Titanic Survival Analysis project aimed to predict whether a passenger survived the disaster using features such as age, gender, ticket class, and other attributes. The analysis includes EDA, feature engineering, model building, and evaluation.

## Dataset
The Titanic dataset used for this project contains the following key features:
- **PassengerId:** Unique identifier for each passenger
- **Pclass:** Ticket class (1st, 2nd, or 3rd)
- **Sex:** Gender of the passenger
- **Age:** Age of the passenger
- **SibSp:** Number of siblings/spouses aboard
- **Parch:** Number of parents/children aboard
- **Ticket:** Ticket number
- **Fare:** Passenger fare
- **Cabin:** Cabin number (if available)
- **Embarked:** Port of embarkation (C, Q, S)

The test set lacks the `Survived` column, requiring the model to predict survival outcomes.

## Exploratory Data Analysis (EDA)
Key insights gained from EDA:
- Majority of passengers in higher classes had a higher survival rate.
- Women had a significantly higher survival rate compared to men.
- Passengers with lower ticket fares had lower survival rates.

## Feature Engineering
The following transformations and feature engineering techniques were applied:
- Handling missing values in columns like `Age`, `Cabin`, and `Embarked`.
- Creating new features based on ticket class and family size.
- Encoding categorical variables.
- Normalizing numerical features to improve model performance.

## Model Building
Various machine learning models were tested, including:
- Logistic Regression
- Random Forest
- XGBoost
- CatBoost
- MLP Classifier

Hyperparameter tuning was performed to optimize model performance. The Random Forest Classifier (after resampling) provided the most accurate and balanced predictions.


Hyperparameter tuning was performed to optimize model performance.

## Model Evaluation
The best-performing model achieved an accuracy score of **0.77** on Kaggle. The Random Forest Classifier (Resampled) was finalized as the best model based on evaluation metrics.
### Evaluation Metrics
- **Metrics Table for comparison (`Accuracy`, `Precision` and `Recall`)**

   ![metrics table](metrics-table.png)

- **Confusion Matrix**

   ![confusion matrices](confusion-matrices.png)

- **ROC-AUC Curve for best performing model**

   ![roc-auc-curve](roc-auc-curve.png)

## Kaggle Submission
A final submission was made to Kaggle, achieving a prediction score of **0.77**.

## Conclusion
- Effective feature engineering and hyperparameter tuning significantly contributed to the model's performance.
- The test set's prediction accuracy of 0.77 demonstrates a strong predictive model.
- Further improvements could involve advanced ensemble methods.

## How to Run the Project
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd Titanic_Survival_Analysis
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Jupyter Notebook:
   ```bash
   jupyter notebook Titanic_Survival_Analysis.ipynb
   ```
## Live App
**App Link:-** [Click Here](https://pkr1234-titanic-survival-prediction.hf.space)

## Acknowledgments
- [Kaggle](https://www.kaggle.com/) for providing the Titanic dataset.
- Data Science Community for continuous learning and support.

## License
- This project is licensed under the MIT License. See the LICENSE file for more information.
