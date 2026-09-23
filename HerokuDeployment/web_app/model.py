import streamlit as st
from pickle import load
import pandas as pd
from sklearn.svm import SVC
from sklearn import metrics

def prediction(val1,val2):
    val1=float(val1)
    val2=float(val2)
    dict={1:val1,2:val2}
    col1=pd.Series(dict[1])
    col2=pd.Series(dict[2])
    test=pd.DataFrame({"col1":col1,"col2":col2})
    classifier=load(open('pickle/svm_model.pkl','rb'))
    pred=classifier.predict(test)
    return pred[0]

def main():
    value1= st. number_input("Enter value 1: ")
    value2= st. number_input("Enter value 2: ")

    output=prediction(value1,value2)

    if value1 and value2:
        st.subheader("Output Prediction")
        if(output== 0):
            st.write("Negative class :triumph:")
        else:
            st.write("Positive class :grin:")


if(__name__=='__main__'):
    main()
