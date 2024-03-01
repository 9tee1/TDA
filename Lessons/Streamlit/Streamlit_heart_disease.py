##import libraries
import streamlit as st
import keras
import pickle
import numpy as np
from keras.models import load_model
from PIL import Image

##load the saved model
model=load_model('heart_disease.h5')

##load the pickle file
#with open('hrt_model.pkl', 'rb') as file:
    #model_lr =pickle.load(file)


##create a function for prediction
def heart_prediction(input):
    input_array = np.asarray(input)
    input_reshape = input_array.reshape(1,-1)
    prediction = model.predict(input_reshape)
    print(prediction)

    if (prediction[0]==0):
        return 'you are not likely to die from heart failure given your conditions.'
    else:
        return 'you are likely to die from heart failure given your conditions.'

##setup streamlit page
    
def main():
    st.set_page_config(page_title='Heart failure Predictor', layout='wide')
    ## add image
    image = Image.open('heart.png')
    st.image(image,use_column_width=False)

    #add title to application
    st.title('Heart failure predictor using artificial neural network')
    st.write('Enter your personal data to get heart failure risk evaluation')

    ##take input from users
    ## variable inputs
    age = st.number_input('Age of the patient:',min_value=0, step=1)
    anaemia = st.number_input('Anaemia | yes or no | yes = 1 and no = 0:',min_value=0, step=1)
    creatinine_phosphokinase = st.number_input('Level of the CPK enzyme in the blood (mcg/L):',min_value=0, step=1)
    diabetes = st.number_input('Diabetes | yes or no | yes = 1 and no = 0:',min_value=0, step=1)
    ejection_fraction = st.number_input('Percentage of blood leaving the heart at each contraction:',min_value=0, step=1)
    high_blood_pressure = st.number_input('Hypertension | yes or no | yes = 1 and no = 0:',min_value=0, step=1)
    platelets = st.number_input('Platelet count of blood (kiloplatelets/mL):',min_value=0, step=1)
    serum_creatinine = st.number_input('Level of serum creatinine in the blood (mg/dL):',min_value=0.00, step=0.01)
    serum_sodium = st.number_input('Level of serum sodium in the blood (mEq/L):',min_value=0, step=1)
    sex = st.number_input('Sex | male or female | male = 1 and female = 0:',min_value=0, step=1)
    smoking = st.number_input('Habit of smoking | yes or no | yes = 1 and no = 0:',min_value=0, step=1)
    time = st.number_input('Follow-up period (days):',min_value=0, step=1)


    ##code for predict
    predict = ''

    ## button for prediction
    if st.button('Predict'):
        predict=heart_prediction([age,anaemia,creatinine_phosphokinase,diabetes,ejection_fraction,high_blood_pressure,platelets,serum_creatinine,serum_sodium,sex,smoking,time])
    st.success(predict)


    ##run script
main()
