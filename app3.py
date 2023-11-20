import streamlit as st
import pandas as pd

# 판다스의 데이터프레임을, 웹 화면으로 보여주는 방법

def main():
    st.title('아이리스 꽃 데이터')

    df = pd.read_csv('./data/iris.csv')

    st.dataframe(df)


if __name__ == '__main__' :
    main()