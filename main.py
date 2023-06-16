"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import requests

def get_quote():
    url = 'https://api.kanye.rest/' # Kanye Rest API url
    response = requests.get(url)

    # If the request is successful, the status code will be 200
    if response.status_code == 200:
        return response.json()['quote'] # Returns data from API
    else:
        return None

def print_quotes(num_quotes):
    for i in range(num_quotes):
        quote = get_quote()
        if quote is not None:
            st.write(quote)
        else:
            st.write("Failed to fetch quote")
    

st.title("Kanye's words of Divine Wisdom")
st.image('https://media2.giphy.com/media/f5Rl5kM3cmAMVYQg9z/giphy.gif', caption='KANYE', use_column_width=True)


num_quotes = st.slider('Number of quotes', min_value=1, max_value=10)

if st.button('Try generating these again!'):
    print_quotes(num_quotes)
else:
    print_quotes(num_quotes)