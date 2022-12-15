import streamlit
import pandas

streamlit.title("My Parents Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text("1. Masala Dosa")
streamlit.text("2. Idly")
streamlit.text("3. Wada Pav")
streamlit.text("4. Bread Omellete")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
