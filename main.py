import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode, GridUpdateMode
import nfl_data_py as nfl
import numpy as np
import requests
from PredictionsPage import DisplayPredictions
from AnalysisPage import DisplayAnalysisPage
from HomePage import DisplayHomePage



def main():
    page = "Home"
    with st.sidebar:
        page = st.radio("Select Page", ["Home", "Predictions", "Analysis"])
    df = pd.read_parquet('prodPredictionData.parquet')
    if page == "Home":
        DisplayHomePage().run()

    elif page == "Predictions":
        DisplayPredictions(df).run()
    else:
        DisplayAnalysisPage(df).run()

if __name__ == '__main__':
    st.set_page_config(layout="wide")
    main()