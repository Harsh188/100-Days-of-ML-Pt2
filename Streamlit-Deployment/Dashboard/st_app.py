import streamlit as st

# Title
st.title("MLOps Production Dashboard")
st.info("🔍 Explore the different pages below.")

# Pages
pages = ["Data", "Performance", "Inference", "Inspection"]
st.header("Pages")
selected_page = st.radio("Select a page:", pages, index=2)

if selected_page == 'Data':
	st.header("Data")

	

