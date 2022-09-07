import streamlit as st 
import pandas as pd

class DisplayHomePage:
    def __init__(self):
        return
    
    def run(self):
        st.title("Fantasy Football Analysis Tool")
        st.caption("Built by Ben Abraham")

        with st.expander("User Guide"):
            st.write("Predictions Section:")
            st.caption("This section contains the output from a machine learning model \
                        I built with xgBoost. The user may filter by position on the left sidebar. \
                        Each player's predicted points per game \
                        for the upcoming season is shown in the expected range column.\
                        Additional useful information for each player is displayed such \
                        as age and position.")
            st.write("Analysis Section:")
            st.caption("This seciton allows the user to compare up to five players at once. \
                        The user may select to select specific statistics for each player and \
                        create plots over time, or simply view a dataframe.")
            st.write("Other Information:")
            st.caption("I built this tool during the summer of 2022, and I sourced my data using the \
                        python library, 'nfl-data-py'. I plan to continually update the site and improve \
                        my model over time. Next summer, I may like to implement the site in a more scaleable \
                        framework compared to streamlit. I am open to any feedback, to get in contact \
                        please visit my personal website: bpabraham123.github.io")
        return