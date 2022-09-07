import streamlit as st
import pandas as pd
import nfl_data_py as nfl
import plotly.express as px

class DisplayAnalysisPage:
    def __init__(self, predictions):
        self.predictions = predictions
        self.data = pd.read_parquet('prodSeasonalData.parquet')
        self.position = []
        self.players = {}
        self.playerNames = []
        self.column = ''
        return

    def __sidebar(self):
        positionOptions = ['QB', 'RB', 'WR', 'TE']
        self.position = st.sidebar.multiselect(label='Select Position', 
                                               options=positionOptions,
                                               default=positionOptions)
        self.players = self.predictions[self.predictions.position.isin(self.position)][['name', 'id']].set_index('name').to_dict('index')
        self.playerNames = st.sidebar.multiselect(label='Select Player(s):', options=self.players.keys())
        self.column = st.sidebar.selectbox(label='Select Column', options=self.data.columns, index=2)

     

    def __displayDataFrames(self):
        selectedIds = [self.players[player]['id'] for player in self.playerNames]
        selectedData = self.data.loc[selectedIds]
        selectedData.sort_values(by='season', inplace=True)
        plot = px.scatter(selectedData, 
                          x="season", 
                          y=self.column, 
                          color="name",
                          size='games', 
                          hover_data=[self.column])
        st.plotly_chart(plot)
        st.dataframe(selectedData.set_index("name"))

            

        
    def run(self):
        if len(self.playerNames) < 5:
            self.__sidebar()
            self.__displayDataFrames()
        return