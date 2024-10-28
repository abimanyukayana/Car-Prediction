# Import libraries
import streamlit as st
import pandas as pd
import pickle

# Load model and pipeline
with open('model.pkl','rb')as file_1:
    model = pickle.load(file_1)

with open('pipeline_pkl','rb')as file_2:
    pipeline = pickle.load(file_2)

# Set page configuration
st.set_page_config(
    page_title="Car Price Prediction",
    initial_sidebar_state='expanded'
)

# Function to run the Streamlit model predictor
def run():
    # Set Title
    st.title('Car Price Prediction')

    # Sub Title
    st.subheader('This page focuses on predicting car prices based on car specifications.')
    st.markdown('---')
    st.image('prediksimobil.jpg')  

    # Create a form for user input
    st.markdown('## Input Car Data')
    with st.form('car_form'):
        name = st.text_input('Car Name', 'Enter the car name...')
        brand = st.selectbox('Brand', ['Toyota', 'Mercedes-Benz', 'Holden', 'Hyundai', 'Other'])
        model = st.text_input('Model', 'Enter the car model...')
        year = st.number_input('Year of Manufacture', min_value=1886, max_value=2024, value=2020)
        kilometers = st.number_input('Kilometers Driven (km)', min_value=0, value=50000)
        car_type = st.selectbox('Type', ['Sedan', 'Wagon', 'Hatchback', 'Sportswagon', 'Other'])
        gearbox = st.selectbox('Gearbox', ['Automatic', 'Manual'])
        fuel = st.selectbox('Fuel Type', ['Unleaded Petrol', 'Diesel', 'Electric'])
        color = st.selectbox('Color', ['Grey', 'Black', 'White', 'Red', 'Blue', 'Other'])

        submitted = st.form_submit_button("Predict Price")

    # Creating a dataframe from user input
    car_data = {
        'Name': name,
        'Brand': brand,
        'Model': model,
        'Year': year,
        'Kilometers': kilometers,
        'Type': car_type,
        'Gearbox': gearbox,
        'Fuel': fuel,
        'Color': color
    }

    df_car = pd.DataFrame([car_data])

    # Display the car data
    st.subheader("Entered Car Data")
    st.dataframe(df_car)

    # Make prediction after the form is submitted
    if submitted:
        # Preprocess the data
        processed_data = pipeline.transform(df_car)

        # Predict using the model
        prediction = model.predict(processed_data)

        # Display the prediction result
        st.success(f'Predicted Car Price: RM {prediction[0]:,.2f}')

if __name__ == '__main__':
    run()
