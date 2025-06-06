import streamlit as st
import pandas as pd

# import pandas as pd

df = pd.DataFrame(
    {
        "first column": [0, 1, 2, 3, 4],
        "second column": [0, 10, 20, 30, 40],
    }
)
#df

st.write("Below is a DataFrame:", df, "Above is a dataframe.")
st.write(1234)

