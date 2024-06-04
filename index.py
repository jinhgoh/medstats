import streamlit as st
import pandas as pd
from scipy.stats import chi2_contingency

# Title of the application
st.title("카이제곱분포 분석기 for Dr.Cho, DVM, Ph.D.")

# Upload Excel file
uploaded_file = st.file_uploader("엑셀파일업로드", type=["xlsx"])

if uploaded_file:
    # Read the Excel file
    df = pd.read_excel(uploaded_file)
    
    # Show the dataframe
    st.write("입력된 데이터:", df)
    
    # Select dependent and independent variables
    dependent_var = st.selectbox("변수1을 선택하세요", df.columns)
    independent_var = st.selectbox("변수2를 선택하세요", df.columns)
    
    if st.button("Run Chi-square Analysis"):
        # Create a contingency table
        contingency_table = pd.crosstab(df[dependent_var], df[independent_var])
        #st.write(contingency_table)
        # Perform Chi-square test
        chi2, p, dof, expected = chi2_contingency(contingency_table, correction=False)
        
        # Display the results
        st.write("Chi-square test results:")
        st.write(f"Chi-square statistic: {chi2}")
        st.write(f"P-value: {p}")
        st.write(f"Degrees of freedom: {dof}")
        st.write("Expected frequencies:")
        st.write(expected)
        st.write("언제나 선생님의 행복을 바라며 기도합니다. 말뿐만 아니라 저도 노력하겠습니다. 힘내세요!!")

