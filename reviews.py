import streamlit as st
import numpy as np
import pandas as pd
from streamlit_star_rating import st_star_rating

original=pd.read_csv("reviews_db.csv", encoding='latin-1')

def show_reviews(place):
    st.write("")
    count=0
    for index, row in original.iterrows():
           
           if(row['Place']==place):
             with st.container():
                col1, col2 = st.columns(2,gap="large")
                with col1:
                    st.write(row["Raw_Review"])
                with col2:
                    st_star_rating(label = "", maxValue = 5, defaultValue = row["Rating"], key = index, read_only = True )
                st.divider()
             count=count+1
             if(count>20):
              break
            