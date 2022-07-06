# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 10:25:05 2022

@author: Openlab
"""

import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

import datetime as dt
from datetime import datetime, timedelta, date, time

from cachetools import cached, TTLCache
from PIL import Image

st.set_page_config(layout="wide")
image = Image.open(r'C:\Users\Openlab\Pictures\ME.png')

st.image(image, width=300)
st.title("Welcome to Huawei ME Openlab Data Center Monitoring") 
st.sidebar.header("Please Filter Date and Time Here")

## Adding the caching
cache = TTLCache(maxsize=100, ttl=86400)

@cached(cache)
@st.cache(ttl=60*6000,max_entries=200,suppress_st_warning=True, allow_output_mutation=True)
def source_loading():
    UPS_001_40Mod_ACEnergy_df = pd.read_excel(r'F:\Shared\Ashner\DataCenter_PowerMonitoring\Datacenter_Power_Test\MEOL_DataCenter_PowerMonitoring_2022.xlsx', sheet_name='40Modular_UPS-001_ACEnergy')
    ## Filter only the important Columns
    UPS_001_40Mod_ACEnergy_df_date = UPS_001_40Mod_ACEnergy_df.iloc[::,2:4]
    UPS_001_40Mod_ACEnergy_df = UPS_001_40Mod_ACEnergy_df.iloc[::,19:34]
    ## Concatinate the date and time to the important columns and delete the unused dataframe
    UPS_001_40Mod_ACEnergy_df = pd.concat([UPS_001_40Mod_ACEnergy_df_date, UPS_001_40Mod_ACEnergy_df], axis=1)
    del(UPS_001_40Mod_ACEnergy_df_date)
    
    UPS_001_40Modul_ITB1_EnergyInfo_df = pd.read_excel(r'F:\Shared\Ashner\DataCenter_PowerMonitoring\Datacenter_Power_Test\MEOL_DataCenter_PowerMonitoring_2022.xlsx', sheet_name='40Modul_UPS-001_ITB1_EnergyInfo')
    ## Filter only the important Columns
    UPS_001_40Modul_ITB1_EnergyInfo_df_date = UPS_001_40Modul_ITB1_EnergyInfo_df.iloc[::,2:4]
    UPS_001_40Modul_ITB1_EnergyInfo_df = UPS_001_40Modul_ITB1_EnergyInfo_df.iloc[::,28:52]
    ## Concatinate the date and time to the important columns and delete the unused dataframe
    UPS_001_40Modul_ITB1_EnergyInfo_df = pd.concat([UPS_001_40Modul_ITB1_EnergyInfo_df_date, UPS_001_40Modul_ITB1_EnergyInfo_df], axis=1)
    del(UPS_001_40Modul_ITB1_EnergyInfo_df_date)
    
    UPS_001_40Modul_ITB2_EnergyInfo_df = pd.read_excel(r'F:\Shared\Ashner\DataCenter_PowerMonitoring\Datacenter_Power_Test\MEOL_DataCenter_PowerMonitoring_2022.xlsx', sheet_name='40Modul_UPS-001_ITB2_EnergyInfo')
    ## Filter only the important Columns
    UPS_001_40Modul_ITB2_EnergyInfo_df_date = UPS_001_40Modul_ITB2_EnergyInfo_df.iloc[::,2:4]
    UPS_001_40Modul_ITB2_EnergyInfo_df = UPS_001_40Modul_ITB2_EnergyInfo_df.iloc[::,15:26]
    ## Concatinate the date and time to the important columns and delete the unused dataframe
    UPS_001_40Modul_ITB2_EnergyInfo_df = pd.concat([UPS_001_40Modul_ITB2_EnergyInfo_df_date, UPS_001_40Modul_ITB2_EnergyInfo_df], axis=1)
    del(UPS_001_40Modul_ITB2_EnergyInfo_df_date)
    
    UPS_02_40Modul_ITB1_EnergyInfo_df = pd.read_excel(r'F:\Shared\Ashner\DataCenter_PowerMonitoring\Datacenter_Power_Test\MEOL_DataCenter_PowerMonitoring_2022.xlsx', sheet_name='40Modul_UPS-02_ITB1_EnergyInfo')
    ## Filter only the important Columns
    UPS_02_40Modul_ITB1_EnergyInfo_df_date = UPS_02_40Modul_ITB1_EnergyInfo_df.iloc[::,2:4]
    UPS_02_40Modul_ITB1_EnergyInfo_df = UPS_02_40Modul_ITB1_EnergyInfo_df.iloc[::,28:52]
    ## Concatinate the date and time to the important columns and delete the unused dataframe
    UPS_02_40Modul_ITB1_EnergyInfo_df = pd.concat([UPS_02_40Modul_ITB1_EnergyInfo_df_date, UPS_02_40Modul_ITB1_EnergyInfo_df], axis=1)
    del(UPS_02_40Modul_ITB1_EnergyInfo_df_date)
    
    UPS_02_40Modul_ITB2_EnergyInfo_df = pd.read_excel(r'F:\Shared\Ashner\DataCenter_PowerMonitoring\Datacenter_Power_Test\MEOL_DataCenter_PowerMonitoring_2022.xlsx', sheet_name='40Modul_UPS-02_ITB2_EnergyInfo')
    ## Filter only the important Columns
    UPS_02_40Modul_ITB2_EnergyInfo_df_date = UPS_02_40Modul_ITB2_EnergyInfo_df.iloc[::,2:4]
    UPS_02_40Modul_ITB2_EnergyInfo_df = UPS_02_40Modul_ITB2_EnergyInfo_df.iloc[::,15:26]
    ## Concatinate the date and time to the important columns and delete the unused dataframe
    UPS_02_40Modul_ITB2_EnergyInfo_df = pd.concat([UPS_02_40Modul_ITB2_EnergyInfo_df_date, UPS_02_40Modul_ITB2_EnergyInfo_df], axis=1)
    del(UPS_02_40Modul_ITB2_EnergyInfo_df_date)

    UPS_18Modular_UPS_ACEnergy_df = pd.read_excel(r'F:\Shared\Ashner\DataCenter_PowerMonitoring\Datacenter_Power_Test\MEOL_DataCenter_PowerMonitoring_2022.xlsx', sheet_name='18Modular_UPS_ACEnergy')
    ## Filter only the important Columns
    UPS_18Modular_UPS_ACEnergy_df_date = UPS_18Modular_UPS_ACEnergy_df.iloc[::,2:4]
    UPS_18Modular_UPS_ACEnergy_df = UPS_18Modular_UPS_ACEnergy_df.iloc[::,10:16]    
    ## Concatinate the date and time to the important columns and delete the unused dataframe
    UPS_18Modular_UPS_ACEnergy_df = pd.concat([UPS_18Modular_UPS_ACEnergy_df_date, UPS_18Modular_UPS_ACEnergy_df], axis=1)
    del(UPS_18Modular_UPS_ACEnergy_df_date)
    
    UPS_18Modul_ITB1_EnergyInfo_df = pd.read_excel(r'F:\Shared\Ashner\DataCenter_PowerMonitoring\Datacenter_Power_Test\MEOL_DataCenter_PowerMonitoring_2022.xlsx', sheet_name='18Modul_UPS_ITB1_EnergyInfo')
    ## Filter only the important Columns
    UPS_18Modul_ITB1_EnergyInfo_df_date = UPS_18Modul_ITB1_EnergyInfo_df.iloc[::,2:4]
    UPS_18Modul_ITB1_EnergyInfo_df = UPS_18Modul_ITB1_EnergyInfo_df.iloc[::,25:46]
    ## Concatinate the date and time to the important columns and delete the unused dataframe
    UPS_18Modul_ITB1_EnergyInfo_df = pd.concat([UPS_18Modul_ITB1_EnergyInfo_df_date, UPS_18Modul_ITB1_EnergyInfo_df], axis=1)
    del(UPS_18Modul_ITB1_EnergyInfo_df_date)
    
    UPS_18Modul_ITB2_EnergyInfo_df = pd.read_excel(r'F:\Shared\Ashner\DataCenter_PowerMonitoring\Datacenter_Power_Test\MEOL_DataCenter_PowerMonitoring_2022.xlsx', sheet_name='18Modul_UPS_ITB2_EnergyInfo')
    ## Filter only the important Columns
    UPS_18Modul_ITB2_EnergyInfo_df_date = UPS_18Modul_ITB2_EnergyInfo_df.iloc[::,2:4]
    UPS_18Modul_ITB2_EnergyInfo_df = UPS_18Modul_ITB2_EnergyInfo_df.iloc[::,25:46]
    ## Concatinate the date and time to the important columns and delete the unused dataframe
    UPS_18Modul_ITB2_EnergyInfo_df = pd.concat([UPS_18Modul_ITB2_EnergyInfo_df_date, UPS_18Modul_ITB2_EnergyInfo_df], axis=1)
    del(UPS_18Modul_ITB2_EnergyInfo_df_date)

    return UPS_001_40Mod_ACEnergy_df, UPS_001_40Modul_ITB1_EnergyInfo_df, UPS_001_40Modul_ITB2_EnergyInfo_df, UPS_02_40Modul_ITB1_EnergyInfo_df, UPS_02_40Modul_ITB2_EnergyInfo_df, \
        UPS_18Modular_UPS_ACEnergy_df, UPS_18Modul_ITB1_EnergyInfo_df, UPS_18Modul_ITB2_EnergyInfo_df

def date_time():
    global start_date_option, end_date_option, start_time_option, end_time_option
    now = datetime.now() + timedelta(days=-1)
    start_date_option = st.sidebar.date_input("Start of Dates", datetime(datetime.now().year, datetime.now().month, 1))
    end_date_option = st.sidebar.date_input("End of Dates", now) 
    
    start_date_option = start_date_option.strftime("%Y-%m-%d")
    end_date_option = end_date_option.strftime("%Y-%m-%d") 
    
    
    start_time_option = st.sidebar.time_input('Set Start Time', time(00, 00))
    end_time_option = st.sidebar.time_input('Set End Time', time(23, 00))
    
    start_time_option = start_time_option.strftime("%H:%M:%S")
    end_time_option = end_time_option.strftime("%H:%M:%S") 
    
    return start_date_option, end_date_option, start_time_option, end_time_option

def old_date_time():
    global old_start_date_option, old_end_date_option, old_start_time_option, old_end_time_option
    
    old_start_date_option = datetime(datetime.now().year, datetime.now().month-1, 1)
    old_end_date_option = datetime(datetime.now().year, datetime.now().month-1, 31)
    
    old_start_date_option = old_start_date_option.strftime("%Y-%m-%d")
    old_end_date_option = old_end_date_option.strftime("%Y-%m-%d") 
    
    old_start_time_option = time(00, 00)
    old_end_time_option = time(23, 00)
    
    old_start_time_option = old_start_time_option.strftime("%H:%M:%S")
    old_end_time_option = old_end_time_option.strftime("%H:%M:%S")        
    return old_start_date_option, old_end_date_option, old_start_time_option, old_end_time_option


def UPS_001_40Mod_ACEnergy_Energy():
    
    ## This is to just take the 1st five 
    UPS_001_40Mod_ACEnergy_head = source_loading()[0]
    
    ## Make a period and covert it to index
    UPS_001_40Mod_ACEnergy_head['Date'] = pd.to_datetime(UPS_001_40Mod_ACEnergy_head['Date']).dt.date
    
    
    ## Remove the Date Outliers Section
    UPS_001_40Mod_ACEnergy_head = UPS_001_40Mod_ACEnergy_head[UPS_001_40Mod_ACEnergy_head['Date'] !=  pd.to_datetime('2021-07-16')]
    UPS_001_40Mod_ACEnergy_head = UPS_001_40Mod_ACEnergy_head[UPS_001_40Mod_ACEnergy_head['Date'] !=  pd.to_datetime('2022-01-01')]
    UPS_001_40Mod_ACEnergy_head = UPS_001_40Mod_ACEnergy_head[UPS_001_40Mod_ACEnergy_head['Date'] !=  pd.to_datetime('2022-04-22')]
    UPS_001_40Mod_ACEnergy_head = UPS_001_40Mod_ACEnergy_head[UPS_001_40Mod_ACEnergy_head['Date'] !=  pd.to_datetime('2022-05-08')]
    ## Remove the Date Outliers Section
    
    UPS_001_40Mod_ACEnergy_head["period"] = UPS_001_40Mod_ACEnergy_head["Date"].astype(str) +" "+ UPS_001_40Mod_ACEnergy_head["Time"].astype(str)
    UPS_001_40Mod_ACEnergy_head["period"] = pd.to_datetime(UPS_001_40Mod_ACEnergy_head['period'])
    UPS_001_40Mod_ACEnergy_head = UPS_001_40Mod_ACEnergy_head.set_index('period')
    
    ## Make Year, Month and All Filter
    UPS_001_40Mod_ACEnergy_head['Date'] = pd.to_datetime(UPS_001_40Mod_ACEnergy_head['Date'])
    UPS_001_40Mod_ACEnergy_head['Month'] = UPS_001_40Mod_ACEnergy_head['Date'].dt.strftime('%B')
    UPS_001_40Mod_ACEnergy_head['Year'] = UPS_001_40Mod_ACEnergy_head['Date'].dt.strftime('%Y')
    UPS_001_40Mod_ACEnergy_head = UPS_001_40Mod_ACEnergy_head.iloc[::,2:]
    
    # now = datetime.now() + timedelta(days=-1)
    # start_date_option = st.sidebar.date_input("Start of Dates", now) 
    # end_date_option = st.sidebar.date_input("End of Dates", now) 
    
    # start_date_option = start_date_option.strftime("%Y-%m-%d")
    # end_date_option = end_date_option.strftime("%Y-%m-%d") 
    
    
    # start_time_option = st.sidebar.time_input('Set Start Time', time(00, 00))
    # end_time_option = st.sidebar.time_input('Set End Time', time(23, 00))
    
    # start_time_option = start_time_option.strftime("%H:%M:%S")
    # end_time_option = end_time_option.strftime("%H:%M:%S") 
    
    try:    
        UPS_001_40Mod_ACEnergy_head = UPS_001_40Mod_ACEnergy_head.loc[start_date_option:end_date_option] ## Set Date
        # print(UPS_001_40Mod_ACEnergy_head.loc['2020-01-07'])
        UPS_001_40Mod_ACEnergy_head = UPS_001_40Mod_ACEnergy_head.between_time(start_time_option, end_time_option) ## Set Time
        
        ## Charting
        fig = px.bar(UPS_001_40Mod_ACEnergy_head.iloc[::,:-2], x=UPS_001_40Mod_ACEnergy_head.iloc[::,:-2].index, y=UPS_001_40Mod_ACEnergy_head.iloc[::,:-2].columns)
        
        # fig.update_layout(
        #     margin=dict(l=20, r=20, t=20, b=20)
        #     # paper_bgcolor="LightSteelBlue",
        # )
        
        st.plotly_chart(fig, use_container_width=True)
        
        #st.bar_chart(UPS_001_40Mod_ACEnergy_head.iloc[::,:-2])
        
        ##
        
        UPS_001_40Mod_ACEnergy_consumption = UPS_001_40Mod_ACEnergy_head['3QF1 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                               UPS_001_40Mod_ACEnergy_head['3QF1 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                               UPS_001_40Mod_ACEnergy_head['3QF1 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                               UPS_001_40Mod_ACEnergy_head['3QF2 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                               UPS_001_40Mod_ACEnergy_head['3QF2 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                               UPS_001_40Mod_ACEnergy_head['3QF2 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                               UPS_001_40Mod_ACEnergy_head['3QF3 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                               UPS_001_40Mod_ACEnergy_head['3QF3 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                               UPS_001_40Mod_ACEnergy_head['3QF3 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                               UPS_001_40Mod_ACEnergy_head['3QF4 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                               UPS_001_40Mod_ACEnergy_head['3QF4 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                               UPS_001_40Mod_ACEnergy_head['3QF4 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                               UPS_001_40Mod_ACEnergy_head['3QF5 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                               UPS_001_40Mod_ACEnergy_head['3QF5 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                               UPS_001_40Mod_ACEnergy_head['3QF5 electricity energy(L3)(kWh)Time Difference'].sum()
        
        html_str = f"""
        <style>
        p.a {{
          font: bold {20}px Courier;
        }}
        </style>
        <p class="a">40Module_ACEnergy_Consumption in KW:  {UPS_001_40Mod_ACEnergy_consumption}</p>
        """
        st.markdown(html_str, unsafe_allow_html=True)
        
    except:
        st.markdown("""
        <style>
        .big-font {
            font-size:100px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="big-font">No Available Data for this Date</p>', unsafe_allow_html=True)
        
        
def UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo():
    
    ## This is to just take the 1st five 
    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head = source_loading()[1]
    
    ## Make a period and covert it to index
    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Date'] = pd.to_datetime(UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Date']).dt.date
    
    
    ## Remove the Date Outliers Section
    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head = UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head[UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Date'] !=  pd.to_datetime('2021-07-16')]
    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head = UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head[UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Date'] !=  pd.to_datetime('2022-01-01')]
    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head = UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head[UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Date'] !=  pd.to_datetime('2022-04-22')]
    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head = UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head[UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Date'] !=  pd.to_datetime('2022-05-08')]
    ## Remove the Date Outliers Section
    
    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head["period"] = UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head["Date"].astype(str) +" "+ UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head["Time"].astype(str)
    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head["period"] = pd.to_datetime(UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['period'])
    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head = UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head.set_index('period')
    
    ## Make Year, Month and All Filter
    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Date'] = pd.to_datetime(UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Date'])
    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Month'] = UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Date'].dt.strftime('%B')
    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Year'] = UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Date'].dt.strftime('%Y')
    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head = UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head.iloc[::,2:]
    
    
    try:    
        UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head = UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head.loc[start_date_option:end_date_option] 
        # print(UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head.loc['2020-01-07'])
        UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head = UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head.between_time(start_time_option, end_time_option)
        
        fig = px.bar(UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head.iloc[::,:-2], x = UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head.iloc[::,:-2].index, 
                     y= UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head.iloc[::,:-2].columns)
        
        st.plotly_chart(fig, use_container_width=True)
        
        # st.bar_chart(UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head.iloc[::,:-2])
        
        UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_consumption = UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF1 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF2 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF3 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF4 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF5 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF6 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF7 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF8 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF9 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF10 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF11 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF12 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF13 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF14 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF15 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF16 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF17 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF18 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF19 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF20 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF21 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF22 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF23 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF24 electricity energy(L3)(kWh)Time Difference'].sum()
        
        
        html_str = f"""
        <style>
        p.a {{
          font: bold {20}px Courier;
        }}
        </style>
        <p class="a">40Module_UPS-001_ITB1_EnergyInfo_Consumption in KW:  {UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_consumption}</p>
        """
        st.markdown(html_str, unsafe_allow_html=True)
        
    except:
        st.markdown("""
        <style>
        .big-font {
            font-size:100px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="big-font">No Available Data for this Date</p>', unsafe_allow_html=True)
        

def UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo():
    
    
    ## This is to just take the 1st five 
    UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head = source_loading()[2]

    
    ## Make a period and covert it to index
    UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Date'] = pd.to_datetime(UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Date']).dt.date
    
    
    ## Remove the Date Outliers Section
    UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head = UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head[UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Date'] !=  pd.to_datetime('2021-07-16')]
    UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head = UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head[UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Date'] !=  pd.to_datetime('2022-01-01')]
    UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head = UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head[UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Date'] !=  pd.to_datetime('2022-04-22')]
    UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head = UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head[UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Date'] !=  pd.to_datetime('2022-05-08')]
    ## Remove the Date Outliers Section
    
    UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head["period"] = UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head["Date"].astype(str) +" "+ UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head["Time"].astype(str)
    UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head["period"] = pd.to_datetime(UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['period'])
    UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head = UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head.set_index('period')
    
    ## Make Year, Month and All Filter
    UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Date'] = pd.to_datetime(UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Date'])
    UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Month'] = UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Date'].dt.strftime('%B')
    UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Year'] = UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Date'].dt.strftime('%Y')
    UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head = UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head.iloc[::,2:]
    
    
    try:    
        UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head = UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head.loc[start_date_option:end_date_option] 
        # print(UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head.loc['2020-01-07'])
        UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head = UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head.between_time(start_time_option, end_time_option)
        
        fig = px.bar(UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head.iloc[::,:-2], x = UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head.iloc[::,:-2].index, 
                     y= UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head.iloc[::,:-2].columns)
        
        st.plotly_chart(fig, use_container_width=True)
        
        UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_consumption = UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['2QF1 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['2QF2 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['2QF3 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['2QF4 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['2QF5 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['2QF6 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['2QF7 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['2QF8 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['2QF9 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['2QF10 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['2QF11 electricity energy(L2)(kWh)Time Difference'].sum()
        
        html_str = f"""
        <style>
        p.a {{
          font: bold {20}px Courier;
        }}
        </style>
        <p class="a">40Module_UPS-001_ITB2_EnergyInfo_Consumption in KW:  {UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_consumption}</p>
        """
        st.markdown(html_str, unsafe_allow_html=True)
        
    except:
        st.markdown("""
        <style>
        .big-font {
            font-size:100px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="big-font">No Available Data for this Date</p>', unsafe_allow_html=True)
    
    
def UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo():
    
    ## This is to just take the 1st five 
    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head = source_loading()[3]

    
    ## Make a period and covert it to index
    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Date'] = pd.to_datetime(UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Date']).dt.date
    
    
    ## Remove the Date Outliers Section
    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head = UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head[UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Date'] !=  pd.to_datetime('2021-07-16')]
    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head = UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head[UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Date'] !=  pd.to_datetime('2022-01-01')]
    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head = UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head[UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Date'] !=  pd.to_datetime('2022-04-22')]
    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head = UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head[UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Date'] !=  pd.to_datetime('2022-05-08')]
    ## Remove the Date Outliers Section
    
    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head["period"] = UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head["Date"].astype(str) +" "+ UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head["Time"].astype(str)
    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head["period"] = pd.to_datetime(UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['period'])
    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head = UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head.set_index('period')
    
    ## Make Year, Month and All Filter
    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Date'] = pd.to_datetime(UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Date'])
    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Month'] = UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Date'].dt.strftime('%B')
    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Year'] = UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['Date'].dt.strftime('%Y')
    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head = UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head.iloc[::,2:]
    
    
    try:    
        UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head = UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head.loc[start_date_option:end_date_option] 
        # print(UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head.loc['2020-01-07'])
        UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head = UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head.between_time(start_time_option, end_time_option)
        
        fig = px.bar(UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head.iloc[::,:-2], x = UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head.iloc[::,:-2].index, 
                     y= UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head.iloc[::,:-2].columns)
        
        st.plotly_chart(fig, use_container_width=True)
        
        UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_consumption = UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF1 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF2 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF3 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF4 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF5 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF6 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF7 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF8 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF9 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF10 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF11 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF12 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF13 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF14 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF15 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF16 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF17 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF18 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF19 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF20 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF21 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF22 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF23 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_head['1QF24 electricity energy(L3)(kWh)Time Difference'].sum()
        
        html_str = f"""
        <style>
        p.a {{
          font: bold {20}px Courier;
        }}
        </style>
        <p class="a">40Module_UPS-02_ITB1_EnergyInfo_Consumption in KW:  {UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo_consumption}</p>
        """
        st.markdown(html_str, unsafe_allow_html=True)
        
    except:
        st.markdown("""
        <style>
        .big-font {
            font-size:100px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="big-font">No Available Data for this Date</p>', unsafe_allow_html=True)
    
 
def UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo():
    
    ## This is to just take the 1st five 
    UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head = source_loading()[4]
    
    ## Make a period and covert it to index
    UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Date'] = pd.to_datetime(UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Date']).dt.date
    
    
    ## Remove the Date Outliers Section
    UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head = UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head[UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Date'] !=  pd.to_datetime('2021-07-16')]
    UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head = UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head[UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Date'] !=  pd.to_datetime('2022-01-01')]
    UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head = UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head[UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Date'] !=  pd.to_datetime('2022-04-22')]
    UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head = UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head[UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Date'] !=  pd.to_datetime('2022-05-08')]
    ## Remove the Date Outliers Section
    
    UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head["period"] = UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head["Date"].astype(str) +" "+ UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head["Time"].astype(str)
    UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head["period"] = pd.to_datetime(UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['period'])
    UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head = UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head.set_index('period')
    
    ## Make Year, Month and All Filter
    UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Date'] = pd.to_datetime(UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Date'])
    UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Month'] = UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Date'].dt.strftime('%B')
    UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Year'] = UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['Date'].dt.strftime('%Y')
    UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head = UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head.iloc[::,2:]
    
    
    try:    
        UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head = UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head.loc[start_date_option:end_date_option] 
        # print(UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head.loc['2020-01-07'])
        UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head = UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head.between_time(start_time_option, end_time_option)
        
        fig = px.bar(UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head.iloc[::,:-2], x = UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head.iloc[::,:-2].index, 
                     y= UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head.iloc[::,:-2].columns)
        
        st.plotly_chart(fig, use_container_width=True)
        
        UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_consumption = UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['2QF1 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['2QF2 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['2QF3 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['2QF4 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['2QF5 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['2QF6 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['2QF7 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['2QF8 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['2QF9 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['2QF10 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                                    UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_head['2QF11 electricity energy(L2)(kWh)Time Difference'].sum()
        
        html_str = f"""
        <style>
        p.a {{
          font: bold {20}px Courier;
        }}
        </style>
        <p class="a">40Module_UPS-02_ITB2_EnergyInfo_Consumption in KW:  {UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo_consumption}</p>
        """
        st.markdown(html_str, unsafe_allow_html=True)
        
    except:
        st.markdown("""
        <style>
        .big-font {
            font-size:100px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="big-font">No Available Data for this Date</p>', unsafe_allow_html=True)
    

def UPS_18Mod_ACEnergy_EnergyInfo():
    
    ## This is to just take the 1st five 
    UPS_18Mod_ACEnergy_EnergyInfo_head = source_loading()[5]
    
    ## Make a period and covert it to index
    UPS_18Mod_ACEnergy_EnergyInfo_head['Date'] = pd.to_datetime(UPS_18Mod_ACEnergy_EnergyInfo_head['Date']).dt.date
    
    
    ## Remove the Date Outliers Section
    UPS_18Mod_ACEnergy_EnergyInfo_head = UPS_18Mod_ACEnergy_EnergyInfo_head[UPS_18Mod_ACEnergy_EnergyInfo_head['Date'] !=  pd.to_datetime('2021-07-16')]
    UPS_18Mod_ACEnergy_EnergyInfo_head = UPS_18Mod_ACEnergy_EnergyInfo_head[UPS_18Mod_ACEnergy_EnergyInfo_head['Date'] !=  pd.to_datetime('2022-01-01')]
    UPS_18Mod_ACEnergy_EnergyInfo_head = UPS_18Mod_ACEnergy_EnergyInfo_head[UPS_18Mod_ACEnergy_EnergyInfo_head['Date'] !=  pd.to_datetime('2022-04-22')]
    UPS_18Mod_ACEnergy_EnergyInfo_head = UPS_18Mod_ACEnergy_EnergyInfo_head[UPS_18Mod_ACEnergy_EnergyInfo_head['Date'] !=  pd.to_datetime('2022-05-08')]
    ## Remove the Date Outliers Section
    
    UPS_18Mod_ACEnergy_EnergyInfo_head["period"] = UPS_18Mod_ACEnergy_EnergyInfo_head["Date"].astype(str) +" "+ UPS_18Mod_ACEnergy_EnergyInfo_head["Time"].astype(str)
    UPS_18Mod_ACEnergy_EnergyInfo_head["period"] = pd.to_datetime(UPS_18Mod_ACEnergy_EnergyInfo_head['period'])
    UPS_18Mod_ACEnergy_EnergyInfo_head = UPS_18Mod_ACEnergy_EnergyInfo_head.set_index('period')
    
    ## Make Year, Month and All Filter
    UPS_18Mod_ACEnergy_EnergyInfo_head['Date'] = pd.to_datetime(UPS_18Mod_ACEnergy_EnergyInfo_head['Date'])
    UPS_18Mod_ACEnergy_EnergyInfo_head['Month'] = UPS_18Mod_ACEnergy_EnergyInfo_head['Date'].dt.strftime('%B')
    UPS_18Mod_ACEnergy_EnergyInfo_head['Year'] = UPS_18Mod_ACEnergy_EnergyInfo_head['Date'].dt.strftime('%Y')
    UPS_18Mod_ACEnergy_EnergyInfo_head = UPS_18Mod_ACEnergy_EnergyInfo_head.iloc[::,2:]
    
    
    try:    
        UPS_18Mod_ACEnergy_EnergyInfo_head = UPS_18Mod_ACEnergy_EnergyInfo_head.loc[start_date_option:end_date_option] 
        # print(UPS_18Mod_ACEnergy_EnergyInfo_head.loc['2020-01-07'])
        UPS_18Mod_ACEnergy_EnergyInfo_head = UPS_18Mod_ACEnergy_EnergyInfo_head.between_time(start_time_option, end_time_option)
        
        fig = px.bar(UPS_18Mod_ACEnergy_EnergyInfo_head.iloc[::,:-2], x = UPS_18Mod_ACEnergy_EnergyInfo_head.iloc[::,:-2].index, 
                     y= UPS_18Mod_ACEnergy_EnergyInfo_head.iloc[::,:-2].columns)
        
        st.plotly_chart(fig, use_container_width=True)
        
        UPS_18Mod_ACEnergy_EnergyInfo_consumption = UPS_18Mod_ACEnergy_EnergyInfo_head['3QF1 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                    UPS_18Mod_ACEnergy_EnergyInfo_head['3QF1 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                    UPS_18Mod_ACEnergy_EnergyInfo_head['3QF1 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                    UPS_18Mod_ACEnergy_EnergyInfo_head['3QF2 electricity energy(L1)(kWh)Time Difference'].sum()	+ \
                                                    UPS_18Mod_ACEnergy_EnergyInfo_head['3QF2 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                    UPS_18Mod_ACEnergy_EnergyInfo_head['3QF2 electricity energy(L3)(kWh)Time Difference'].sum()															
																		

        
        html_str = f"""
        <style>
        p.a {{
          font: bold {20}px Courier;
        }}
        </style>
        <p class="a">18Modular_UPS_ACEnergy_Consumption in KW:  {UPS_18Mod_ACEnergy_EnergyInfo_consumption}</p>
        """
        st.markdown(html_str, unsafe_allow_html=True)
        
    except:
        st.markdown("""
        <style>
        .big-font {
            font-size:100px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="big-font">No Available Data for this Date</p>', unsafe_allow_html=True)
        

def UPS_18Mod_ITB1_EnergyInfo():
    
    ## This is to just take the 1st five 
    UPS_18Mod_ITB1_EnergyInfo_head = source_loading()[6]
    
    ## Make a period and covert it to index
    UPS_18Mod_ITB1_EnergyInfo_head['Date'] = pd.to_datetime(UPS_18Mod_ITB1_EnergyInfo_head['Date']).dt.date
    
    
    ## Remove the Date Outliers Section
    UPS_18Mod_ITB1_EnergyInfo_head = UPS_18Mod_ITB1_EnergyInfo_head[UPS_18Mod_ITB1_EnergyInfo_head['Date'] !=  pd.to_datetime('2021-07-16')]
    UPS_18Mod_ITB1_EnergyInfo_head = UPS_18Mod_ITB1_EnergyInfo_head[UPS_18Mod_ITB1_EnergyInfo_head['Date'] !=  pd.to_datetime('2022-01-01')]
    UPS_18Mod_ITB1_EnergyInfo_head = UPS_18Mod_ITB1_EnergyInfo_head[UPS_18Mod_ITB1_EnergyInfo_head['Date'] !=  pd.to_datetime('2022-04-22')]
    UPS_18Mod_ITB1_EnergyInfo_head = UPS_18Mod_ITB1_EnergyInfo_head[UPS_18Mod_ITB1_EnergyInfo_head['Date'] !=  pd.to_datetime('2022-05-08')]
    ## Remove the Date Outliers Section
    
    UPS_18Mod_ITB1_EnergyInfo_head["period"] = UPS_18Mod_ITB1_EnergyInfo_head["Date"].astype(str) +" "+ UPS_18Mod_ITB1_EnergyInfo_head["Time"].astype(str)
    UPS_18Mod_ITB1_EnergyInfo_head["period"] = pd.to_datetime(UPS_18Mod_ITB1_EnergyInfo_head['period'])
    UPS_18Mod_ITB1_EnergyInfo_head = UPS_18Mod_ITB1_EnergyInfo_head.set_index('period')
    
    ## Make Year, Month and All Filter
    UPS_18Mod_ITB1_EnergyInfo_head['Date'] = pd.to_datetime(UPS_18Mod_ITB1_EnergyInfo_head['Date'])
    UPS_18Mod_ITB1_EnergyInfo_head['Month'] = UPS_18Mod_ITB1_EnergyInfo_head['Date'].dt.strftime('%B')
    UPS_18Mod_ITB1_EnergyInfo_head['Year'] = UPS_18Mod_ITB1_EnergyInfo_head['Date'].dt.strftime('%Y')
    UPS_18Mod_ITB1_EnergyInfo_head = UPS_18Mod_ITB1_EnergyInfo_head.iloc[::,2:]
    
    
    try:    
        UPS_18Mod_ITB1_EnergyInfo_head = UPS_18Mod_ITB1_EnergyInfo_head.loc[start_date_option:end_date_option] 
        # print(UPS_18Mod_ITB1_EnergyInfo_head.loc['2020-01-07'])
        UPS_18Mod_ITB1_EnergyInfo_head = UPS_18Mod_ITB1_EnergyInfo_head.between_time(start_time_option, end_time_option)

        fig = px.bar(UPS_18Mod_ITB1_EnergyInfo_head.iloc[::,:-2], x = UPS_18Mod_ITB1_EnergyInfo_head.iloc[::,:-2].index, 
                     y= UPS_18Mod_ITB1_EnergyInfo_head.iloc[::,:-2].columns)
        
        st.plotly_chart(fig, use_container_width=True)
        
        UPS_18Mod_ITB1_EnergyInfo_consumption = UPS_18Mod_ITB1_EnergyInfo_head['1QF1 electricity energy(L1)(kWh)Time Difference'].sum() + \
												UPS_18Mod_ITB1_EnergyInfo_head['1QF2 electricity energy(L2)(kWh)Time Difference'].sum() + \
												UPS_18Mod_ITB1_EnergyInfo_head['1QF3 electricity energy(L3)(kWh)Time Difference'].sum() + \
												UPS_18Mod_ITB1_EnergyInfo_head['1QF4 electricity energy(L1)(kWh)Time Difference'].sum() + \
												UPS_18Mod_ITB1_EnergyInfo_head['1QF5 electricity energy(L2)(kWh)Time Difference'].sum() + \
												UPS_18Mod_ITB1_EnergyInfo_head['1QF6 electricity energy(L3)(kWh)Time Difference'].sum() + \
												UPS_18Mod_ITB1_EnergyInfo_head['1QF7 electricity energy(L1)(kWh)Time Difference'].sum() + \
												UPS_18Mod_ITB1_EnergyInfo_head['1QF8 electricity energy(L2)(kWh)Time Difference'].sum() + \
												UPS_18Mod_ITB1_EnergyInfo_head['1QF9 electricity energy(L3)(kWh)Time Difference'].sum() + \
												UPS_18Mod_ITB1_EnergyInfo_head['1QF10 electricity energy(L1)(kWh)Time Difference'].sum() + \
												UPS_18Mod_ITB1_EnergyInfo_head['1QF11 electricity energy(L2)(kWh)Time Difference'].sum() + \
												UPS_18Mod_ITB1_EnergyInfo_head['1QF12 electricity energy(L3)(kWh)Time Difference'].sum() + \
												UPS_18Mod_ITB1_EnergyInfo_head['1QF13 electricity energy(L1)(kWh)Time Difference'].sum() + \
												UPS_18Mod_ITB1_EnergyInfo_head['1QF14 electricity energy(L2)(kWh)Time Difference'].sum() + \
												UPS_18Mod_ITB1_EnergyInfo_head['1QF15 electricity energy(L3)(kWh)Time Difference'].sum() + \
												UPS_18Mod_ITB1_EnergyInfo_head['1QF16 electricity energy(L1)(kWh)Time Difference'].sum() + \
												UPS_18Mod_ITB1_EnergyInfo_head['1QF17 electricity energy(L2)(kWh)Time Difference'].sum() + \
												UPS_18Mod_ITB1_EnergyInfo_head['1QF18 electricity energy(L3)(kWh)Time Difference'].sum() + \
												UPS_18Mod_ITB1_EnergyInfo_head['1QF19 electricity energy(L1)(kWh)Time Difference'].sum() + \
												UPS_18Mod_ITB1_EnergyInfo_head['1QF20 electricity energy(L2)(kWh)Time Difference'].sum() + \
												UPS_18Mod_ITB1_EnergyInfo_head['1QF21 electricity energy(L3)(kWh)Time Difference'].sum()
														
																		   
        html_str = f"""
        <style>
        p.a {{
          font: bold {20}px Courier;
        }}
        </style>
        <p class="a">18Modular_ITB1_EnergyInfo_Consumption in KW:  {UPS_18Mod_ITB1_EnergyInfo_consumption}</p>
        """
        st.markdown(html_str, unsafe_allow_html=True)
        
    except:
        st.markdown("""
        <style>
        .big-font {
            font-size:100px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="big-font">No Available Data for this Date</p>', unsafe_allow_html=True)
        

def UPS_18Mod_ITB2_EnergyInfo():
    
    ## This is to just take the 1st five 
    UPS_18Mod_ITB2_EnergyInfo_head = source_loading()[7]
    
    ## Make a period and covert it to index
    UPS_18Mod_ITB2_EnergyInfo_head['Date'] = pd.to_datetime(UPS_18Mod_ITB2_EnergyInfo_head['Date']).dt.date
    
    
    ## Remove the Date Outliers Section
    UPS_18Mod_ITB2_EnergyInfo_head = UPS_18Mod_ITB2_EnergyInfo_head[UPS_18Mod_ITB2_EnergyInfo_head['Date'] !=  pd.to_datetime('2021-07-16')]
    UPS_18Mod_ITB2_EnergyInfo_head = UPS_18Mod_ITB2_EnergyInfo_head[UPS_18Mod_ITB2_EnergyInfo_head['Date'] !=  pd.to_datetime('2022-01-01')]
    UPS_18Mod_ITB2_EnergyInfo_head = UPS_18Mod_ITB2_EnergyInfo_head[UPS_18Mod_ITB2_EnergyInfo_head['Date'] !=  pd.to_datetime('2022-04-22')]
    UPS_18Mod_ITB2_EnergyInfo_head = UPS_18Mod_ITB2_EnergyInfo_head[UPS_18Mod_ITB2_EnergyInfo_head['Date'] !=  pd.to_datetime('2022-05-08')]
    ## Remove the Date Outliers Section
    
    UPS_18Mod_ITB2_EnergyInfo_head["period"] = UPS_18Mod_ITB2_EnergyInfo_head["Date"].astype(str) +" "+ UPS_18Mod_ITB2_EnergyInfo_head["Time"].astype(str)
    UPS_18Mod_ITB2_EnergyInfo_head["period"] = pd.to_datetime(UPS_18Mod_ITB2_EnergyInfo_head['period'])
    UPS_18Mod_ITB2_EnergyInfo_head = UPS_18Mod_ITB2_EnergyInfo_head.set_index('period')
    
    ## Make Year, Month and All Filter
    UPS_18Mod_ITB2_EnergyInfo_head['Date'] = pd.to_datetime(UPS_18Mod_ITB2_EnergyInfo_head['Date'])
    UPS_18Mod_ITB2_EnergyInfo_head['Month'] = UPS_18Mod_ITB2_EnergyInfo_head['Date'].dt.strftime('%B')
    UPS_18Mod_ITB2_EnergyInfo_head['Year'] = UPS_18Mod_ITB2_EnergyInfo_head['Date'].dt.strftime('%Y')
    UPS_18Mod_ITB2_EnergyInfo_head = UPS_18Mod_ITB2_EnergyInfo_head.iloc[::,2:]
    
    
    try:    
        UPS_18Mod_ITB2_EnergyInfo_head = UPS_18Mod_ITB2_EnergyInfo_head.loc[start_date_option:end_date_option] 
        # print(UPS_18Mod_ITB2_EnergyInfo_head.loc['2020-01-07'])
        UPS_18Mod_ITB2_EnergyInfo_head = UPS_18Mod_ITB2_EnergyInfo_head.between_time(start_time_option, end_time_option)
        
        fig = px.bar(UPS_18Mod_ITB2_EnergyInfo_head.iloc[::,:-2], x = UPS_18Mod_ITB2_EnergyInfo_head.iloc[::,:-2].index, 
                     y= UPS_18Mod_ITB2_EnergyInfo_head.iloc[::,:-2].columns)
        
        st.plotly_chart(fig, use_container_width=True)
        
        UPS_18Mod_ITB2_EnergyInfo_consumption = UPS_18Mod_ITB2_EnergyInfo_head['2QF1 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                UPS_18Mod_ITB2_EnergyInfo_head['2QF2 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                UPS_18Mod_ITB2_EnergyInfo_head['2QF3 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                UPS_18Mod_ITB2_EnergyInfo_head['2QF4 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                UPS_18Mod_ITB2_EnergyInfo_head['2QF5 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                UPS_18Mod_ITB2_EnergyInfo_head['2QF6 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                UPS_18Mod_ITB2_EnergyInfo_head['2QF7 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                UPS_18Mod_ITB2_EnergyInfo_head['2QF8 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                UPS_18Mod_ITB2_EnergyInfo_head['2QF9 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                UPS_18Mod_ITB2_EnergyInfo_head['2QF10 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                UPS_18Mod_ITB2_EnergyInfo_head['2QF11 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                UPS_18Mod_ITB2_EnergyInfo_head['2QF12 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                UPS_18Mod_ITB2_EnergyInfo_head['2QF13 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                UPS_18Mod_ITB2_EnergyInfo_head['2QF14 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                UPS_18Mod_ITB2_EnergyInfo_head['2QF15 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                UPS_18Mod_ITB2_EnergyInfo_head['2QF16 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                UPS_18Mod_ITB2_EnergyInfo_head['2QF17 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                UPS_18Mod_ITB2_EnergyInfo_head['2QF18 electricity energy(L3)(kWh)Time Difference'].sum() + \
                                                UPS_18Mod_ITB2_EnergyInfo_head['2QF19 electricity energy(L1)(kWh)Time Difference'].sum() + \
                                                UPS_18Mod_ITB2_EnergyInfo_head['2QF20 electricity energy(L2)(kWh)Time Difference'].sum() + \
                                                UPS_18Mod_ITB2_EnergyInfo_head['2QF21 electricity energy(L3)(kWh)Time Difference'].sum()
        
        
														
        col1, col2 = st.columns(2)
        
        with col1:															   
            html_str = f"""
            <style>
            p.a {{
              font: bold {20}px Courier;
            }}
            </style>
            <p class="a">18Modular_ITB2_EnergyInfo_Consumption in KW:  {UPS_18Mod_ITB2_EnergyInfo_consumption}</p>
            """
            st.markdown(html_str, unsafe_allow_html=True)
        
            
    except:
        st.markdown("""
        <style>
        .big-font {
            font-size:100px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="big-font">No Available Data for this Date</p>', unsafe_allow_html=True)

    
if __name__ == '__main__':    
    
    ## Setting the Date and Time as global variable outside of the function
    start_date_option, end_date_option, start_time_option, end_time_option = date_time()

    
    option = st.sidebar.selectbox(
     'Data to be Analyze',
     ('All_Data','UPS_001_40Mod_ACEnergy_Energy', 'UPS_001_40Mod_Energy_ITB1_EnergyInfo', 'UPS_001_40Mod_Energy_ITB2_EnergyInfo', 'UPS_02_40Mod_Energy_ITB1_EnergyInfo', 'UPS_02_40Mod_Energy_ITB2_EnergyInfo',
      'UPS_18Mod_ACEnergy_EnergyInfo', 'UPS_18Mod_ITB1_EnergyInfo', 'UPS_18Mod_ITB2_EnergyInfo'))
    
    data_checkbox = st.sidebar.checkbox('Show Data', value=True)

    if data_checkbox:

        if option == 'All_Data':
            UPS_001_40Mod_ACEnergy_Energy()
    
            """------------"""
            
            UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo()
            
            """------------"""
            
            UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo()
            
            """------------"""
            
            UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo()
            
            """------------"""
            
            UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo()
            
            """------------"""
            
            UPS_18Mod_ACEnergy_EnergyInfo()
            
            """------------"""
            
            UPS_18Mod_ITB1_EnergyInfo()
            
            """------------"""
            
            UPS_18Mod_ITB2_EnergyInfo()
        
        elif option == 'UPS_001_40Mod_ACEnergy_Energy':
            UPS_001_40Mod_ACEnergy_Energy()
        
        elif option == 'UPS_001_40Mod_Energy_ITB1_EnergyInfo':
            UPS_001_40Mod_ACEnergy_Energy_ITB1_EnergyInfo()
            
        elif option == 'UPS_001_40Mod_Energy_ITB2_EnergyInfo':
            UPS_001_40Mod_ACEnergy_Energy_ITB2_EnergyInfo()
       
        elif option == 'UPS_02_40Mod_Energy_ITB1_EnergyInfo':
            UPS_02_40Mod_ACEnergy_Energy_ITB1_EnergyInfo
            
        elif option == 'UPS_02_40Mod_Energy_ITB2_EnergyInfo':
            UPS_02_40Mod_ACEnergy_Energy_ITB2_EnergyInfo()
        
        elif option == 'UPS_18Mod_ACEnergy_EnergyInfo':
            UPS_18Mod_ACEnergy_EnergyInfo()
        
        elif option == 'UPS_18Mod_ITB1_EnergyInfo':
            UPS_18Mod_ITB1_EnergyInfo()
        
        elif option == 'UPS_18Mod_ITB2_EnergyInfo':
            UPS_18Mod_ITB1_EnergyInfo()
    
    else:
        st.markdown("""
        <style>
        .big-font {
            font-size:100px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="big-font">No Available Data</p>', unsafe_allow_html=True)
    
    
    hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    