import streamlit as st

st.set_page_config(page_title="My Styled App", layout="wide")

page_bg = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://plus.unsplash.com/premium_photo-1669748157617-a3a83cc8ea23?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjV8fGJlYWNofGVufDB8fDB8fHww");
background-size: cover;
background-position: center;
background-attachment: fixed;
opacity: 0.9;
}

.box{
background: rgba(0,1,1,0.6);
padding: 40px;
border-radius: 12px;
color: white;
width: 50%;
margin-top: 50px;
font-size: 20px;
}

.box2{
background: rgba(1,0,0,0.6);
padding: 40px;
border-radius: 12px;
color: yellow;
width: 50%;
margin-top: 30px;
font-size: 18px;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

st.title("🚀 Welcome to My Streamlit App")

st.markdown("""
<div class="box">
    <h1>What is Streamlit?</h1>
    <p>Streamlit is an open-source Python framework used to build and deploy web apps for Machine Learning and Data Science projects quickly and easily.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="box2">
    <h1>Why use Streamlit?</h1>
    <p>It requires no frontend knowledge. Just write Python and your app is ready to deploy!</p>
</div>
""", unsafe_allow_html=True)
