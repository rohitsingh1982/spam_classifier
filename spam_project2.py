import streamlit as st
import joblib
import pandas as pd


model=joblib.load("spam_clf.pkl")
st.set_page_config(layout="wide")

st.sidebar.image("flag.jpg")
st.sidebar.title("ℹ️ About Us")
st.sidebar.text("sdsgashjsgdhasgdg")
st.sidebar.title("📞 Contact us")
st.sidebar.text("9999999999")

st.markdown(
    """
    <style>
    .banner {
        background: linear-gradient(90deg, #6366f1, #22c55e);
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        color: white;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 30px;
    }
    </style>

    <div class="banner">
        🚫 Spam Classifier Project
    </div>
    """,
    unsafe_allow_html=True
)


col1,col2=st.columns([1.5,2],gap="large")
with col1:

    st.markdown(
    """
    <style>
    .card-header {
        background-color: Yellow;
        padding: 16px;
        border-radius: 10px;
        font-size: 25px;
        font-weight: 700;
        color: #22c55e;
        margin: 25px 0;
    }
    </style>

    <div class="card-header">
        🔍 Single Msg Prediction
    </div>
    """,
    unsafe_allow_html=True
)
    text=st.text_input("Enter MSG")
    if st.button("predict"):
        result=model.predict([text])
        if result=="spam":
            st.error("spam->Irrelevent ❌")
        else:
            st.success("ham->Relevent ✅")


with col2:
    st.markdown(
    """
    <style>
    .card-header {
        background-color: Yellow;
        padding: 16px;
        border-radius: 10px;
        font-size: 25px;
        font-weight: 700;
        color: #22c55e;
        margin: 25px 0;
    }
    </style>

    <div class="card-header">
        🔍 Bulk Msg Prediction
    </div>
    """,
    unsafe_allow_html=True
)
    file=st.file_uploader("select file countaing bulk msgs",type=['txt','csv'])

    if file!=None:
        df=pd.read_csv(file,header=None,names=["Msg"])
        place=st.empty()
        place.dataframe(df)  
        if st.button("Predict",key="b2"):
            df['result']=model.predict(df.Msg)
            place.dataframe(df) 


