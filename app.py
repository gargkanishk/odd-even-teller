import streamlit as st
import pandas as pd

st.write("""
# Let the user know if the number is even or odd
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    number_input = st.number_input("number_input",step=1)
    data = {'number_input': number_input,

            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())

#Preprocessing
st.subheader('Result')
if df['number_input'][0] %2 == 0:
    st.write('Even')
else:
    st.write('Odd')
#st.write(prediction)

