import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import datetime
from streamlit_gsheets import GSheetsConnection
# data preparation

url = "https://docs.google.com/spreadsheets/d/1ZV2oZt-KXeWsAftMvrttQPfIiLy-o3oV0axLTCTDCaQ/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)
form_attributs = []
form_attributs_bool = True
form_variables = []
reformulated_attributes =[]

df = conn.read(spreadsheet=url)
df = pd.DataFrame(df)
today = datetime.date.today()
st.title('Heart disease prediction ')
#df = pd.read_csv('D:\pfe_2022\heart_disease_prediction\heart_1.csv', nrows=50)
#df = st.dataframe(data)


st.markdown('  >This system allows us to predict cardiac patients from a [database](https://docs.google.com/spreadsheets/d/1ZV2oZt-KXeWsAftMvrttQPfIiLy-o3oV0axLTCTDCaQ/edit?usp=sharing) of diagnosed patients.'
 'This was achieved by using machine learning techniques and applying the **PCA** method'
 ' for data processing and preparing the collected data for classification by the **KNN** algorithm,'
 ' which allowed us to achieve an accuracy of 97.83%.'
 'the project repository [here](https://github.com/mohammed4124/heart-disease-prediction/tree/master)'
 ' --this information is updated in '+today.strftime('%d/%m/%y')+'--')

if st.checkbox('Show first 100 raw data'):
    st.subheader('Raw data')
    st.write(df)
def reformulate_attributes(arg):
    switcher = {
        "No": 0,
        "Yes": 1,
        "Male": 1,
        "Female": 0,
        "Normal": 0,
        "ST-T abnormality": 1,
        "Left ventricular hypertrophy": 2,
        "Typical angina": 0,
        "Atypical angina": 1,
        "Non-anginal pain": 2,
        "Asymptomatic": 2,
    }
    return switcher.get(arg, arg)
#form______________________________

with st.form("my_form"):
    Age = st.number_input("Age",min_value=1, value=None, placeholder="Age")
    form_attributs.append(Age)
    form_variables.append('Age')

    Sex = st.selectbox('Sex', ('Male', 'Female'))
    form_attributs.append(Sex)
    form_variables.append('Sex')


    Chest_pain_type = st.selectbox('Chest pain type', ('Typical angina', 'Atypical angina', 'Non-anginal pain', 'Asymptomatic'))
    form_attributs.append(Chest_pain_type)
    form_variables.append('Chest pain type')

    Blood_pressure = st.number_input("Blood pressure", min_value=0, value=None, placeholder="Blood pressure")
    form_attributs.append(Blood_pressure)
    form_variables.append('Blood Pressure')

    Cholesterol = st.number_input("Cholesterol", min_value=0, value=None, placeholder="Cholesterol")
    form_attributs.append(Cholesterol)
    form_variables.append('Cholesterol')

    Fasting_blood_sugar = st.selectbox('Fasting blood sugar', ('No', 'Yes'))
    form_attributs.append(Fasting_blood_sugar)
    form_variables.append('Fasting blood sugar')

    ECG = st.selectbox('ECG', ('Normal', 'ST-T abnormality', 'Left ventricular hypertrophy'))
    form_attributs.append(ECG)
    form_variables.append('ECG')

    Max_heart_rate = st.number_input("Max heart rate", min_value=0, value=None, placeholder="Max heart rate")
    form_attributs.append(Max_heart_rate)
    form_variables.append('Max heart rate')

    Angina_from_exertion = st.selectbox('Angina from exertion', ('No', 'Yes'))
    form_attributs.append(Angina_from_exertion)
    form_variables.append('Angina from exertion')
    Oldpeak = st.number_input("Old peak", min_value=-2.6, value=None, placeholder="Oldpeak")
    form_attributs.append(Oldpeak)
    form_variables.append('Old peak')


    ST_segment_slope = st.selectbox('ST segment slope', ('Up', 'Flat', 'Down'))
    form_attributs.append(ST_segment_slope)
    form_variables.append('ST segment slope')

   # Every form must have a submit button
    submitted = st.form_submit_button("Predict")

if submitted:
    for item in form_attributs:
        if item is None:
            st.warning("You forgot the " + form_variables[form_attributs.index(item)]+".")
            form_attributs_bool = False
            break
    if form_attributs_bool:
        for item in form_attributs:
            reformulated_attributes.append(reformulate_attributes(item))

    if form_attributs_bool and len(form_attributs) == len(reformulated_attributes):
        components.html("""
        <style>
        .text{
          text-align: center;
          font-size: 41px;
          font-weight: 600;
          font-family: 'Poppins', sans-serif;
          background: -webkit-linear-gradient(right, #56d8e4, #9f01ea, #56d8e4, #9f01ea);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
          
        }
        
        </style>    
            <div class="text">
                 The patient : <br> HAS NOT A HEART DISEASE
            </div>
        """)
    elif form_attributs_bool:
        components.html("""
        <style>
        .text{
          text-align: center;
          font-size: 41px;
          font-weight: 600;
          font-family: 'Poppins', sans-serif;
          background: -webkit-linear-gradient(right, #56d8e4, #9f01ea, #56d8e4, #9f01ea);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
          
        }
        
        </style>    
            <div class="text">
                 The patient : <br> HAS A HEART DISEASE
            </div>
        """)


st.markdown("**Note:** ")
st.markdown(">***The application is under maintenance, so the result will always be negative***")
st.markdown(">***It will be fixed as soon as possible. Thank you***")
st.subheader('Developer profile:')
components.iframe("https://www.datascienceportfol.io/mohammed_amin",height=500,width=700,scrolling=True)
