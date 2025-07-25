import streamlit as st

# Page configuration
st.set_page_config(page_title="My Streamlit App", page_icon="✨", layout="centered")

# App title and intro
st.title("🌟 Welcome to My Streamlit App")
st.write("This is a basic template to build your awesome Streamlit app.")

# Sidebar
st.sidebar.title("📚 Navigation")
page = st.sidebar.radio("Choose a section:", ["Home", "About", "Contact"])

# Routing logic
if page == "Home":
    st.header("🏠 Home Page")
    st.write("This is the main content area.")
    name = st.text_input("Enter your name:")
    if name:
        st.success(f"Hello, {name}! 👋 Welcome to the app.")

elif page == "About":
    st.header("ℹ️ About This App")
    st.write("This app is built using [Streamlit](https://streamlit.io/). It's designed to be modular and extendable.")

elif page == "Contact":
    st.header("📬 Contact")
    st.write("You can reach us at: `bairu.chennakeshava05@gmail.com`")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
