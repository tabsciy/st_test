import streamlit as st

# Title of the app
st.title("Simple Interactive Streamlit App")

# Add a slider for user interaction
st.header("Interactive Slider")
slider_value = st.slider("Select a number", min_value=0, max_value=100, value=50)
st.write(f"Slider value: {slider_value}")

# Add a text input for user interaction
st.header("Text Input")
user_text = st.text_input("Enter some text", value="Hello, Streamlit!")
st.write(f"You entered: {user_text}")

# Display a dynamic calculation based on slider value
st.header("Dynamic Calculation")
squared_value = slider_value ** 2
st.write(f"The square of {slider_value} is {squared_value}")

# Add a button to trigger an action
if st.button("Click Me!"):
    st.success("Button clicked!")
    st.balloons()
