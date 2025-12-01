import streamlit as st
st.set_page_config(page_title='AI Projects Demo', layout='wide')
st.title('AI Projects — Demos')

app = st.sidebar.selectbox('Choose demo', ['Traffic', 'Pest', 'Bike'])

if app == 'Traffic':
    st.header('Adaptive Traffic — Demo')
    st.write('Run the traffic demo on Streamlit or connect to backend.')
    st.code('python -m uvicorn 1-Adaptive-Traffic-Signal-Control/backend/api/main:app --reload --port 8000')
elif app == 'Pest':
    st.header('Pest Forecaster — Demo')
    st.write('Upload a drone image to the pest forecast backend endpoint.')
else:
    st.header('Bike Maintenance — Demo')
    st.write('Show predictions or plan routes.')
