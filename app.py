import streamlit as st
from predict import show_predictions_page
from find import show_find_page
from about import show_about_page

bg_img = """
<style>
[data-testid="stAppViewContainer"]
{
background-image:url("https://w0.peakpx.com/wallpaper/204/817/HD-wallpaper-clear-water-summer-beach-exotic-fruit-ocean-seaside-summertime-sun-tropical-vacation.jpg");
background-size: cover;
background-attachment: local;
}

[data-testid="stHeader"]
{
background-color: rgba(0,0,0,0)
}

[data-testid="stSidebar"]
{
background-image:url("https://img.freepik.com/premium-photo/miniature-toy-airplane-beige-background-summer-holiday-air-travel-by-plane-concept_661495-33414.jpg?w=360");
background-size: cover;
}
</style>
"""

st.markdown(bg_img,unsafe_allow_html=True)
st.title("SOJOURN")
# page = st.sidebar.selectbox("Find, Explore, About",("Find","Explore","About"))
page = st.sidebar.selectbox("Find, Explore",("Find","Explore"))
if page=="Explore":
   show_predictions_page()
else:
   show_find_page()