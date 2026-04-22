# 1. Importing Streamlit
import streamlit as st

# 2. Initializing session state variables
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'name' not in st.session_state:
    st.session_state['name'] = None
if 'phone' not in st.session_state:
    st.session_state['phone'] = None

# 3. Checking if user is already logged in
if st.session_state['logged_in']:
    
    # 4. Display success message for logged-in user
    st.success(f"You are already logged in as {st.session_state['name']}!")
    
    # 5. Button to navigate to menu page
    if st.button("Go to Menu", use_container_width=True):
        st.switch_page("pages/menu.py")
    
    # 6. Logout button and clearing session data
    if st.button("Log out"):
        st.session_state['logged_in'] = False
        st.session_state['name'] = None
        st.session_state['phone'] = None
        st.rerun()

# 7. If user is NOT logged in
else:
    
    # 8. Page title and instructions
    st.title("Sign In 🔑")
    st.write("Please sign in to access the menu.")
    
    # 9. Creating sign-in form
    with st.form("signin_form"):
        
        # 10. Input fields
        email = st.text_input("Email", placeholder="example@gmail.com")
        password = st.text_input("Password", type="password")
        
        # 11. Submit button
        submit = st.form_submit_button("Sign In", use_container_width=True)
        
        # 12. Form validation and login logic
        if submit:
            if email and password:
                st.session_state['logged_in'] = True