import streamlit as st

x = st.slider("Select a value")
st.write(x, "squared is", x * x)

if __name__ == '__main__':
  st.set_option('server.enableCORS', True)