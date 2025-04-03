import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Delivery Agent Hiring", page_icon="🚚")

st.title("🚚 Delivery Agent Hiring Portal")
st.subheader("Where Talent Meets the Road")

st.markdown("Welcome to our staffing portal. We connect skilled delivery agents with companies that need fast and reliable service.")

st.header("📋 Apply as a Delivery Agent")

# Form Inputs
name = st.text_input("Full Name")
phone = st.text_input("Phone Number")
area = st.text_input("Preferred Delivery Area")
experience = st.selectbox("Do you have previous delivery experience?", ["Yes", "No"])

csv_file = "applications.csv"

if st.button("Submit"):
    if name and phone and area:
        new_entry = pd.DataFrame({
            "Name": [name],
            "Phone": [phone],
            "Area": [area],
            "Experience": [experience]
        })

        if os.path.exists(csv_file):
            existing_data = pd.read_csv(csv_file)
            updated_data = pd.concat([existing_data, new_entry], ignore_index=True)
        else:
            updated_data = new_entry

        updated_data.to_csv(csv_file, index=False)
        st.success(f"Thank you, {name}! Your application has been submitted.")
    else:
        st.warning("Please fill in all required fields.")
