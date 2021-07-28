import streamlit as st
import numpy as np
import pandas as pd

st.title('Dimension explorer')

with st.beta_expander('Dynatrace credentials'):
    form = st.form(key='dt_credentials_form')
    dt_url = form.text_input(label='Dynatrace URL')
    dt_token = form.text_input(label='Dynatrace API key')
    submit = form.form_submit_button(label='Apply')



if submit:
    # fetch available metrics kind of 'Prettyname (id), dimKey1, dimKey2, dimKey4'
    METRICS = ["business.shop.revenue, city, country, region, store", 
        "demo.service.requestcount, cl_ip, cl_jar, cl_path, cl_port, cl_processname, cl_service, cl_tech, Host (dt.entity.ftrace:host), Process (dt.entity.ftrace:process), Service (dt.entity.ftrace:service), response_code, srv_ip, srv_port, srv_processname, srv_service, srv_tech"
        "demo.service.responsetime, cl_ip, cl_jar, cl_path, cl_port, cl_processname, cl_service, cl_tech, Host (dt.entity.ftrace:host), Process (dt.entity.ftrace:process), Service (dt.entity.ftrace:service), response_code, srv_ip, srv_port, srv_processname, srv_service, srv_tech"
        ]
    st.selectbox('Search metric', options=METRICS)
    
    
    








