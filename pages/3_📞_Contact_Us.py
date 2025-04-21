
import streamlit as st

st.set_page_config(page_title="Contact Us")
st.title("Contact Us")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    submit = st.form_submit_button("Send")

    if submit:
        st.success("Thank you! Your message has been received.")

st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2025 Sten Design. All rights reserved.</p>", unsafe_allow_html=True)
