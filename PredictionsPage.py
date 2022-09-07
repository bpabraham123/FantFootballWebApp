import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode, GridUpdateMode
import nfl_data_py as nfl
import numpy as np
import requests


class DisplayPredictions:
    def __init__(self, df):
        self.dataframe = df
        
        return

    def run(self):
        self.__sidebar()
        self.__displayDataFrame()
        return

    def __sidebar(self):
        positions = st.sidebar.multiselect(label='Select Position(s):', 
                                           options=['QB', 'RB', 'WR', 'TE'], 
                                           default=['QB', 'RB', 'WR', 'TE'])
        self.dataframe = self.dataframe[self.dataframe['position'].isin(positions)]

        

    def __displayDataFrame(self):
        self.dataframe = self.dataframe.sort_values(by=['key'], ascending=False)
        grid_options = {'columnDefs':   [ {'field': 'name', 
                                           'headerName': 'Player'
                                          },
                                          {'field': 'position', 
                                           'headerName': 'Position'},
                                          {'field': 'predicted_range', 
                                           'headerName': 'Expected Range', 
                                           'sortable': True
                                        },
                                          {'field': 'team', 
                                           'headerName': 'Team'},
                                          {'field': 'age', 
                                           'headerName': 'Age'},
                                          {'field': 'last_season_points_per_game', 
                                           'headerName': 'Previous Season Points Per Game',
                                           'sortable': True} 
                                        ],
                        "rowSelection": "single",
                        'rowDragManaged': True,
                        'enableRangeSelection': True,
                        'allowContextMenuWithControlKey': True,
                        'getContextMenuItems': 'getContextMenuItems',
                        'allowDragFromColumnsToolPanel': True,
                        'defaultColDef': {'flex': 1}
                    }
        # Theme options: "streamlit", "light", "dark", "blue", "fresh", "material"
        AgGrid(self.dataframe, 
               grid_options, 
               theme="streamlit", 
               height=500,
               allow_unsafe_jscode=True,
               enable_enterprise_modules=True,
               update_mode=GridUpdateMode.SELECTION_CHANGED)