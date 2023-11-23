from Libraries import *
import streamlit as st

st.write('Vivash')
countries = ['Sri Lanka', 'Australia', 'Canada', 'USA', 'India', 'China', 'New Zealand', 'Egypt', 'Quatar', 'Mexico']
flag_code = {"Sri Lanka":"lk","USA":"us","Canada":"ca","India":"in","China":"cn", "Zew Zealand":"nz", "Egypt":"eg", "Mexico":"mx"}
data_types = ['cases', 'deaths', 'recovered']
country = st.sidebar.selectbox('Pick up a country', countries)
days = st.sidebar.slider('days', min_value=1, max_value=90, step=1)
data_type = st.sidebar.multiselect('Pick data types', data_types)
st.title("Covid Dashboard")
st.metric('Selected country', country)
st.image(f"https://flagcdn.com/80x60/{flag_code[country]}.png")
#total deaths,recoveries and cases
total_cases = get_historic_cases(country,str(days))
total_deaths = get_historic_deaths(country,str(days))
total_recoveries = get_historic_recoveries(country,str(days))
#total_df = pd.concat([total_cases, total_deaths, total_recoveries], axis=1).astype(int)
#daily deaths,recoveries and cases
daily_cases = get_daily_cases(country,str(days))
daily_deaths = get_daily_deaths(country,str(days))
daily_recoveries = get_daily_recoveries(country,str(days))
daily_df = pd.concat([daily_cases, daily_deaths, daily_recoveries], axis=1).astype(int)
#yesterday deaths,recoveries and cases
yesterday_cases = get_yesterday_cases(country)
yesterday_deaths = get_yesterday_deaths(country)
yesterday_recoveries = get_yesterday_recoveries(country)
#yesterday_df = pd.concat([yesterday_cases, yesterday_deaths, yesterday_recoveries], axis=1).astype(int)
#st.metric('Yesterday cases', yesterday_cases)
#st.metric('Yesterday deaths', yesterday_deaths)
#st.metric('Yesterday recoveries', yesterday_recoveries)
col1,col2,col3 = st.columns(3)
col1.metric('Yesterday Cases',yesterday_cases)
col2.metric('Yesterday Deaths',yesterday_deaths)
col3.metric('Yesterday Recoveries',yesterday_recoveries)
st.line_chart(daily_df)
st.video('https://www.youtube.com/watch?v=Ma07a6svw5w')







