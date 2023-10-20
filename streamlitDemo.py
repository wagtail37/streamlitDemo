import streamlit as st
import pandas as pd
import numpy as np

text = st.text_input(label='Message', value='二酸化炭素センサwebアプリデモ')


st.sidebar.header('サイドバー')
st.sidebar.write(text)



def main():
    df2 = pd.DataFrame(
        np.random.rand(20, 3),
        columns=['a', 'b', 'c']
    )

    st.line_chart(df2)
    st.area_chart(df2)
    st.bar_chart(df2)


if __name__ == '__main__':
    main()

#streamlit run streamlitDemo.py
