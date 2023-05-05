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

# Create a simple login form
st.title('Login')
email = st.text_input('Email')
password = st.text_input('Password', type='password')
if st.button('Login'):
    # Hash the entered password to check against the stored password in the database
    hashed_password = hash_password(password)
    user = collection.find_one({'email': email, 'password': hashed_password})
    if user is not None:
        st.success('Login successful!')
    else:
        st.error('Invalid email or password')
