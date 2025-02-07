import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open('rf_res_model.pkl', 'rb'))

# Title of the app
st.title('Titanic Survival Prediction')

# Input fields for user data
age = st.number_input('Age', min_value=0, max_value=100, value=30)
sex = st.selectbox('Sex', ['Male', 'Female'])
if sex == 'Male':
    sex_encoded = 1
else:
    sex_encoded = 0

sibsp = st.number_input('Number of Siblings/Spouses Aboard', min_value=0, value=0)
parch = st.number_input('Number of Parents/Children Aboard', min_value=0, value=0)
fare = st.number_input('Fare', min_value=0.0, value=0.0)

# Calculate family size
family_size = sibsp + parch + 1

# Button to make prediction
if st.button('Predict'):
    # Prepare the input data for prediction
    input_data = pd.DataFrame({
        'Age': [age],
        'Sex': [sex_encoded],
        'Fare': [fare],
        'Family Size': [family_size]
    })
    
    # Ensure the order of columns matches the model's training
    input_data = input_data[['Sex', 'Age', 'Fare', 'Family Size']]

    # Make prediction
    prediction = model.predict(input_data)
    
    # Display the result
    if prediction[0] == 1:
        st.success('The passenger is likely to survive.')
    else:
        st.error('The passenger is likely to not survive.')
