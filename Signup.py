import streamlit as st
import pymongo
import hashlib

# Connect to the Mongo database
client = pymongo.MongoClient("mongodb+srv://employee:20200@atlascluster.v4i2hkf.mongodb.net/test")
db = client["ocr"]
collection = db["users"]

# Define a function to hash a password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Create a simple signup form
st.title('Signup')
name = st.text_input('Name')
email = st.text_input('Email')
password = st.text_input('Password', type='password')
confirm_password = st.text_input('Confirm Password', type='password')
if st.button('Signup'):
    # Check that passwords match
    if password != confirm_password:
        st.error('Passwords do not match')
    else:
        # Hash the password and insert the new user into the database
        hashed_password = hash_password(password)
        user = {'name': name, 'email': email, 'password': hashed_password}
        collection.insert_one(user)
        st.success('Signup successful!')

