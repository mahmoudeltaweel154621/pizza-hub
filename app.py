#import libraries
import streamlit as st

#creating files to pages
home_page = st.Page(
    page='pages/home.py',
    title='Home Page',
    icon='🏠',
    default= True
)

chatbot_page = st.Page(
    page='pages/chatbot.py',
    title='Talk with AI', 
    icon='✨'

)
menu_page = st.Page(
    page='pages/menu.py',
    title='Explore Menu',
    icon='🍽️'

)
signin_page = st.Page(
    page='pages/signin.py',
    title='Sign In',
    icon='🔑'

)
signup_page = st.Page(
    page='pages/signup.py',
    title='Sign Up',
    icon='📝'

)


all_pages= st.navigation(
    pages=[chatbot_page,home_page,menu_page,signin_page,signup_page],
    position='top'
    )
all_pages.run()















































































































































