import pandas as pd
import numpy as np
import streamlit as st
from pandas import DataFrame

# displaying tittle
st.title("Hello Streamlit App")

## display a simple text
st.write("Hello this Streamlit app is build by Sushant")

df = pd.DataFrame({
    "firstColumn":[1,3,5,7,9],
    "secondColumn":[2,4,6,8,0],
})

##display a dataFrame
st.write(df)

## creat a line chart
chart_data = DataFrame(
    np.random.rand(20,3),columns=["a","b","c"]
)
st.line_chart(chart_data)