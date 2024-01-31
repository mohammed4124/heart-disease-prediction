import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
############# data
st.title('Heart disease prediction ')
df = pd.read_csv('https://github.com/mohammed4124/heart-disease-prediction/blob/master/heart_1.csv',nrows =50)

st.markdown('We create a system that allows us to predict cardiac patients from a database of diagnosed patients.'
 'This was achieved by using machine learning techniques and applying the PCA method'
 ' for data processing and preparing the collected data for classification by the KNN algorithm,'
 ' which allowed us to achieve an accuracy of 97.83%.'
 'my linkedin profile is [here](https://www.linkedin.com/in/mohammed-amin-boutarfa-71a12a199/)')
if st.checkbox('Show first 100 raw data'):
    st.subheader('Raw data')
    st.write(df)
components.html("""
    <!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>Contact us Form</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css">
<link rel="stylesheet" href="d:/pfe_2022/heart_disease_prediction/style.css">

</head>
<body>
        <style>
        @import url('https://fonts.googleapis.com/css?family=Poppins:400,500,600,700&display=swap');
*{
  margin: 0;
  padding: 0;
  outline: none;
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}
body{
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 10px;
  font-family: 'Poppins', sans-serif;
  background-color: #5acbe4;
}
.container{
  max-width: 800px;
  background: #fff;
  width: 800px;
  padding: 25px 40px 10px 40px;
  box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
}
.container .text{
  text-align: center;
  font-size: 41px;
  font-weight: 600;
  font-family: 'Poppins', sans-serif;
  background: -webkit-linear-gradient(right, #56d8e4, #9f01ea, #56d8e4, #9f01ea);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.container form{
  padding: 30px 0 0 0;
}
.container form .form-row{
  display: flex;
  margin: 32px 0;
}
form .form-row .input-data{
  width: 100%;
  height: 40px;
  margin: 0 20px;
  position: relative;
}
form .form-row .textarea{
  height: 70px;
}
.input-data input,
.textarea textarea{
  display: block;
  width: 100%;
  height: 100%;
  border: none;
  font-size: 17px;
  border-bottom: 2px solid rgba(0,0,0, 0.12);
}
.input-data input:focus ~ label, .textarea textarea:focus ~ label,
.input-data input:valid ~ label, .textarea textarea:valid ~ label{
  transform: translateY(-20px);
  font-size: 14px;
  color: #3498db;
}
.textarea textarea{
  resize: none;
  padding-top: 10px;
}
.input-data label{
  position: absolute;
  pointer-events: none;
  bottom: 10px;
  font-size: 16px;
  transition: all 0.3s ease;
}
.textarea label{
  width: 100%;
  bottom: 40px;
  background: #fff;
}
.input-data .underline{
  position: absolute;
  bottom: 0;
  height: 2px;
  width: 100%;
}
.input-data .underline:before{
  position: absolute;
  content: "";
  height: 2px;
  width: 100%;
  background: #3498db;
  transform: scaleX(0);
  transform-origin: center;
  transition: transform 0.3s ease;
}
.input-data input:focus ~ .underline:before,
.input-data input:valid ~ .underline:before,
.textarea textarea:focus ~ .underline:before,
.textarea textarea:valid ~ .underline:before{
  transform: scale(1);
}
.submit-btn .input-data{
  overflow: hidden;
  height: 45px!important;
  width: 25%!important;
}
.submit-btn .input-data .inner{
  height: 100%;
  width: 300%;
  position: absolute;
  left: -100%;
  background: -webkit-linear-gradient(right, #56d8e4, #9f01ea, #56d8e4, #9f01ea);
  transition: all 0.4s;
}
.submit-btn .input-data:hover .inner{
  left: 0;
}
.submit-btn .input-data input{
  background: none;
  border: none;
  color: #fff;
  font-size: 17px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 1px;
  cursor: pointer;
  position: relative;
  z-index: 2;
}
@media (max-width: 700px) {
  .container .text{
    font-size: 30px;
  }
  .container form{
    padding: 10px 0 0 0;
  }
  .container form .form-row{
    display: block;
  }
  form .form-row .input-data{
    margin: 35px 0!important;
  }
  .submit-btn .input-data{
    width: 40%!important;
  }
}

        </style>
<!-- partial:index.partial.html -->
<div class="container">
      <div class="text">
         Enter the patient data to be examined
      </div>
      <form action="">
         <div class="form-row">
            <div class="input-data">
               <input type="number" required placeholder ="Age">
               <div class="underline"></div>
            </div>
            <div class="input-data">
               <input list="Sex" required placeholder = "Sex">
               <datalist id="Sex">
                <option value="Men">
                <option value="Women">
              </datalist>          
            </div>
         </div>
         <div class="form-row">
            <div class="input-data">
               <input list="Chest_pain" required placeholder = "Chest pain type">
               <datalist id="Chest_pain">
                <option value="Typical angina">
                <option value="Atypical angina">
                <option value="Non-anginal pain">
                <option value="Asymptomatic">
              </datalist>
            </div>
            <div class="input-data">
               <input type="number" required placeholder ="Blood pressure">
               <div class="underline"></div>
            </div>
         </div>
                  <div class="form-row">
            <div class="input-data">
               <input type="number" required placeholder = "Cholesterol">
               <div class="underline"></div>
            </div>
            <div class="input-data">
               <input list="Fasting_blood_sugar" required placeholder = "Fasting blood sugar">
               <datalist id="Fasting_blood_sugar">
                <option value="Yes">
                <option value="No">
              </datalist>
            </div>
         </div>
         <div class="form-row">
            <div class="input-data">
               <input list="ECG" required placeholder = "ECG">
               <datalist id="ECG">
                <option value="Normal">
                <option value="ST-T abnormality">
                <option value="Left ventricular hypertrophy">
              </datalist>
            </div>
            <div class="input-data">
               <input type="number" required placeholder ="Max heart rate">
               <div class="underline"></div>
            </div>
         </div>
         <div class="form-row">
            <div class="input-data">
               <input list="Angina_from_exertion" required placeholder = "Angina from exertion">
               <datalist id="Angina_from_exertion">
                <option value="Yes">
                <option value="No">
              </datalist>
            </div>
            <div class="input-data">
               <input type="number" required placeholder = "Oldpeak">
               <div class="underline"></div>
               
            </div>
         </div>
         <div class="form-row">
            <div class="input-data">
               <input list="ST_slope" required placeholder = "ST segment slope">
               <datalist id="ST_slope">
                <option value="Up">
                <option value="Flat">
                <option value="Down">
              </datalist>
            </div>
            <div class="input-data">
            </div>
         </div>
         <div class="form-row"> 
        </div>
            <div class="form-row submit-btn">
               <div class="input-data">
                  <div class="inner"></div>
                  <input type="submit" value="submit">
               </div>
            
      </form>
      </div>
<!-- partial -->
  
</body>
</html>
""",height=900,scrolling=True)
st.subheader('About creator')
components.iframe("https://www.datascienceportfol.io/mohammed_amin",height=500,width=700,scrolling=True)
