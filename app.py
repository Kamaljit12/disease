import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


## load the model

## scale model
with open("scaler.pkl", 'rb') as file:
    scaler = pickle.load(file)

## random forest algorithms
with open("RandomForest.pkl", 'rb') as file:
    randoFroest = pickle.load(file)

## adaboost alogtithms

with open("Adaboost.pkl", 'rb') as file:
    adaboost = pickle.load(file)


## header title
st.image("thyroid.png", width=150)
st.title("Thyroid disease Prediction")

## ============================== side bar ======================================

st.sidebar.title("Menu")
st.sidebar.image('thyroid.png',width=100)
option = st.sidebar.selectbox("Select an option",
                              ('Thyroid Prediction', 'Dataset', 'Code'))


### input data



## thyroid prediction with random forest
if option == 'Thyroid Prediction':

    # age = st.number_input("Enter Age")
    # sex = st.number_input("Enter Sex")
    # on_thyorxine = st.number_input("On Thyroxine")
    # tsh = st.number_input("TSH")
    # t3_measured = st.number_input("T3 Measured")
    # t3 = st.number_input("T3")
    # tt4 = st.number_input("TT4")


    
    age = st.select_slider("select Age", ragne(1, 100))
    sex = st.select_slider("select Sex", range(0, 1))
    on_thyorxine = st.select_slider("On Thyroxine", 0, 1)
    tsh = st.select_slider("TSH", range(0, 530))
    t3_measured = st.select_slider("T3 Measured", range(0, 1))
    t3 = st.select_slider("T3", range(0, 11))
    tt4 = st.select_slider("TT4", range(2, 430))
    

    input_ls = [age, sex, on_thyorxine, tsh, t3_measured, t3, tt4]
    df = pd.DataFrame([input_ls], )
    df.columns = ['Age', 'Sex', "On Thyorxine", "TSH", "T3 Measured", "T3", "TT4"]
    df

    
    scaled_data =scaler.transform([input_ls])
    prediction = randoFroest.predict(scaled_data)

    result = ''
    if st.button("Predict"):
        if prediction == 0:
            result = 'The Person is Healthy'
        else:
            result = "The person is having Thyroid"

    st.success(result)

elif option == 'Dataset':
    df = pd.read_csv('prepocessed_hypothyroid.csv')
    ## get sample data

    def sample_data(df, n=5):
        sample_data = df.head(n)
        return sample_data


    obj = sample_data(df)
    if __name__=="__main__":
        obj

    try:
        data_size = st.number_input("Enter the Sample Size", placeholder='like...numbers')
        if st.button("Click For New"):
            sample_data = df.sample(int(data_size))
            sample_data
    except Exception as err:
        st.warning("Please Enter any real Number!")
        data_size
        sample_data = df.sample(int(data_size))
        sample_data

else:
    st.warning("This is empty !")

 


