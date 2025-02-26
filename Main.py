import streamlit as st

# Set page title
st.set_page_config(page_title="October Technological University", page_icon="🎓", layout="wide")

# Title in the center with a large font size
st.markdown(
    "<h1 style='text-align: center; font-size: 50px;'>October Technological University APP</h1>", 
    unsafe_allow_html=True
)

# Create layout with two large buttons in the center
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("🎓 Predicting Specialization ", use_container_width=True):
        st.switch_page("pages\PredictSpecialty.py")  # Redirects to the Classification Page

with col2:
    if st.button("📄 Predicting Grades App", use_container_width=True):
        st.switch_page("pages\PredictDegree.py")  # Redirects to the Second Page
