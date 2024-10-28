# Import library
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run():
    # Set Title
    st.title('Cars Price Dataset Analysis')

    # Sub Title
    st.subheader('Halaman ini menampilkan Exploratory Data Analysis (EDA) dari Dataset Harga Mobil')

    # Markdown
    st.markdown('---')

    # Import images
    st.image('prediksimobil.jpg')

    # Title
    st.markdown('## Dataframe Cars Price')

    # Load data
    data = pd.read_csv('cars_info.csv')

    # Menampilkan dataframe di Streamlit
    st.dataframe(data.head(20))
    st.markdown('---')

    # Bagian EDA
    st.markdown('## Exploratory Data Analysis (EDA)')

    # Distribusi Harga Mobil
    st.markdown('### Distribution of Car Prices')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data['Price'], bins=30, kde=True, ax=ax, color='skyblue')
    ax.set_title('Distribution of Car Prices')
    ax.set_xlabel('Price')
    ax.set_ylabel('Count')
    st.pyplot(fig)

    # Distribusi Harga Mobil berdasarkan Jenis Bahan Bakar
    st.markdown('### Car Price Distribution by Fuel Type')
    fuel_options = st.selectbox('Pilih Jenis Bahan Bakar:', data['Fuel'].unique())
    fuel_price_data = data[data['Fuel'] == fuel_options]
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='Fuel', y='Price', data=fuel_price_data, ax=ax, palette='Set2')
    ax.set_title(f'Price Distribution for {fuel_options} Cars')
    ax.set_xlabel('Fuel Type')
    ax.set_ylabel('Price')
    st.pyplot(fig)

    # Distribusi Harga Mobil berdasarkan Tahun
    st.markdown('### Distribution of Car Prices by Year')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='Year', y='Price', data=data, ax=ax, palette='Set1')
    ax.set_title('Price Distribution by Year of Manufacture')
    ax.set_xlabel('Year')
    ax.set_ylabel('Price')
    st.pyplot(fig)

    # Korelasi antara Fitur dan Harga
    st.markdown('### Correlation between Features and Price')
    correlation = data.corr()
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(correlation, annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
    ax.set_title('Correlation Heatmap')
    st.pyplot(fig)

if __name__ == '__main__':
    run()
