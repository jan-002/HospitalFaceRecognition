import streamlit as st
from multiapp import MultiApp
from apps import home, register, hospital, insurance

# with open('styles.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

app = MultiApp()


app.add_app("Home",home.app)
app.add_app("Register Patient",register.app)
app.add_app("View Patient Details",hospital.app)
app.add_app("Online Billing",insurance.app)

app.run()