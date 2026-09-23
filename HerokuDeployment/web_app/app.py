import streamlit as st

import model as m

def load_sidebar():
    st.sidebar.subheader("Logistic vs SVM ")
    st.sidebar.success("Deployment Challenge")
    st.sidebar.info("The purpose of Challenge is to get familiar with deployment of machine learning models using streamlit and heroku")


def main():
    st.title("Deployment Challenge :trophy:")
    st.image("img\download.jpeg",use_column_width='auto')
    load_sidebar()

    st.subheader("Predictions using SVM with rbf kernel")

    m.main()

if __name__ == '__main__':
    main()
