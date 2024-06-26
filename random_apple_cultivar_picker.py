import pandas as pd
import streamlit as st
import random


# PANDAS
# Load the data
df = pd.read_csv("seznam_odrud.csv", encoding='utf-8')

# Make a list of cultivars, strip off junk chars
cultivars = df['Název odrůdy'].to_list()


# STREAMLIT
# Set page configs
st.set_page_config(
    page_title="Jablko pro tebe",
    page_icon="🍎",
    layout="centered"
)

# CSS markdown for centering
st.markdown(
    """
    <style>
    .centered {
        justify-content: center;
        align-items: center;
    }
    .centered h1 {
        text-align: center;
    }
    .centered div {
        text-align: center;
    }
    .stButton button {
        display: block;
        margin: 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Center apple img
st.image('img/streamlit_apple_900_02.png')

# Center the header
header = 'Jablko pro tebe'
st.markdown(f'<div class="centered"><h1>{"&nbsp;" * 5}{header}</h1></div>', unsafe_allow_html=True)

# Center the button
st.markdown('<div class="centered">', unsafe_allow_html=True)
button = st.button('Vylosuj si odrůdu')
st.markdown('</div>', unsafe_allow_html=True)

# Button behavior and output
if button:
    your_apple = random.choice(cultivars)
    if len(your_apple) > 22:
        if your_apple == 'James Grieve Super Compact':
            st.markdown(f'<div class="centered"><h3>{"&nbsp;" * 2}{your_apple}</h3></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="centered"><h3>{"&nbsp;" * 5}{your_apple}</h3></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="centered"><h2>{"&nbsp;" * 5}{your_apple}</h2></div>', unsafe_allow_html=True)

