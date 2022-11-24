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
my_fruit_list.multiselect("Pick some fruits:" ,list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
