# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 18:17:24 2023

@author: jeyasri
"""

import numpy as np
import pickle
import streamlit as st

# Loading the trained model
loaded_model = pickle.load(open('stress_trained.sav','rb'))

def stresslevel_prediction(input_data):
    
    #changing the input data into numpy array
    id_np_array = np.asarray(input_data)
    id_reshaped = id_np_array.reshape(1,-1)

    prediction = loaded_model.predict(id_reshaped)
    print(prediction)

    if(prediction[0]==0):
        return "Stress Level: LOW"
    elif(prediction[0]==1):
        return "Stress Level: MEDIUM"
    else:
        return "Stress Level: HIGH"
    
def main():
    
    st.title('STRESS LEVEL PREDICTION WEB APP')
    
    Humidity = st.text_input('Humidity Value')
    Temperature = st.text_input('Body Temperature')
    Step_count = st.text_input('Number of Steps')
    
    # Prediction code
    diagnosis = ''
    
    if st.button('PREDICT'):
        diagnosis = stresslevel_prediction([Humidity, Temperature, Step_count])
        
    st.success(diagnosis)
    
if __name__=='__main__':
    main()
