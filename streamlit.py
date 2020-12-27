import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

DATA_URL = ("/home/gourav/Desktop/streamlit/data.csv")


st.title("Collision")
st.markdown("###### my first streamlit project")
# here hash is used to adjust the fontsize

# st.cache is used to prevent from load on every refresh
@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL , nrows = nrows , parse_dates = [['CRASH_DATE','CRASH_TIME']] )
    data.dropna( subset=['LATITUDE','LONGITUDE'] , inplace=True )
    lowercase = lambda x:str(x).lower()
    data.rename(lowercase , axis='columns' , inplace=True )
    data.rename( columns={'crash_data_crash_time':'date/time'},inplace=True )
    return data


data = load_data(100000)


st.header("what are the most injured people in new york")
injured_people  = st.slider("no of injured people at given spot" , 0 , 19 )
st.map(data.query("injured_persons >= @injured_people")[["latitude","longitude"]].dropna(how="any"))


st.header("what is the hour of accident")
hour = st.selectbox("hours to look at" , range(0 , 24) , 1 )
#data = data[data['crash_data_crash_time'].dt.hour == hour]


#st.markdown("Vehicle collision between %i:00 and %i:00" %(hour , hour+1) %24)

midpoint = [np.average(data["latitude"]) , np.average(data["longitude"])]

st.write(pdf.Deck(
 map_style="mapbox://styles/mapbox/light-v9",
 initial_view_state={
  "latitude":midpoint[0],
  "longitude":midpoint[1],
  "zoom":11,
  "pitch":50,
 },
))

if st.checkbox("Show Raw Data", False):
    st.subheader('Raw Data')
    st.write(data)
