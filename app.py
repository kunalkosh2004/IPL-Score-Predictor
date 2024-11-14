import streamlit as st
import pandas as pd
import pickle

df = pickle.load(open('final_model.pkl','rb'))

st.title('IPL Score Predictor')

teams=['Mumbai Indians',
 'Sunrisers Hyderabad',
 'Kings XI Punjab',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Chennai Super Kings',
 'Delhi Capitals',
 'Rajasthan Royals',
 'Pune Warriors',
 'Gujarat Lions']

city=['Mumbai',
 'Kolkata',
 'Delhi',
 'Hyderabad',
 'Bangalore',
 'Chennai',
 'Chandigarh',
 'Jaipur',
 'Pune',
 'Dubai',
 'Abu Dhabi',
 'Sharjah',
 'Durban',
 'Bengaluru',
 'Visakhapatnam',
 'Centurion',
 'Ahmedabad',
 'Rajkot',
 'Dharamsala',
 'Johannesburg',
 'Indore',
 'Port Elizabeth',
 'Cuttack',
 'Ranchi',
 'Cape Town']

col1,col2 = st.columns(2)

with col1:
    batting_team = st.selectbox(
    "Select Batting Team",
    sorted(teams)
)
    
with col2:
    bowling_team = st.selectbox(
    "Select Bowling Team",
    sorted(teams)
)
    
venue = st.selectbox(
    "Select City",
    sorted(city)
)

col1,col2 = st.columns(2)

with col1:
    curr_score = st.number_input("Enter Cureent Score")

with col2:
    overs = st.number_input("How Many Overs Done?")
    

col1,col2 = st.columns(2)

with col1:
    wickets = st.number_input("How Many Wickets Gone")

with col2:
    last_five = st.number_input("Enter last five over runs")
    

if st.button("Predict Score"):
    balls_left = 120-(overs*6)
    wickets_left = 10-wickets
    crr = curr_score/overs
    input_df = pd.DataFrame({
        "batting_team":[batting_team],
        "bowling_team":[bowling_team],
        "city":[venue],
        "curr_score":[curr_score],
        "balls_left":[balls_left],
        "wickets_left":[wickets_left],
        "crr":[crr],
        "last_five_runs":[last_five]
    })
    res = df.predict(input_df)
    st.header("Predicted Score:- "+str(int(res[0])))