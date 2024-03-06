import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Mengonversi path relatif menjadi absolut
base_path = os.path.dirname(__file__)
rideshare_path = os.path.join(base_path, 'rideshare_kaggle.csv')

# Load data
df_rideshare = pd.read_csv(rideshare_path)  

# Define Streamlit app
def main():
    # Set page title
    st.title('Uber & Lfyt Visualization')
    st.write("Welcome to the Uber & Lfyt Visualization Dashboard")
    st.markdown('---')

    # Display scatter plot
    st.subheader('Visualization of the comparison of the number of uber and lyft transports')
    st.write("Based on existing visualizations that Uber transportation has 385663 data and Lyft transportation has 307408 data.")
    df_rideshare['cab_type'].value_counts()
    # Membuat visualisasi data
    f, ax = plt.subplots(figsize=(10, 5))
    ax = sns.countplot(x='cab_type', data=df_rideshare)  # Update kolom di sini
    plt.title('Comparison of Uber and Lyft Transportation usage')
    st.pyplot(f)  # Menampilkan plot di Streamlit
    st.markdown('---') 

    # Display bar chart
    st.subheader('Visualization of the average price of Uber & Lyft transport types')
    st.write("Based on the visualization that the average price of uber and lyft is different. It can be seen from, the average price of using the Lyft transportation type is higher (17.351396) than the Uber transportation type (15.795343).")
    # Calculate average price
    average_prices = df_rideshare.groupby('cab_type')['price'].mean().sort_values()
    # Create bar chart
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(average_prices.index, average_prices.values, color=['blue', 'red'])
    ax.set_title('The average price of Uber & Lyft transport types', fontsize=20)
    ax.set_xlabel('Cab Type', fontsize=20)
    ax.set_ylabel('Price', fontsize=20)
    plt.xticks(rotation=45)
    # Show plot in Streamlit
    st.pyplot(fig)
    st.markdown('---')

    # Display scatter plot
    st.subheader('Visualization of the relationship between weather and ride price')
    st.write("Explore how ride prices vary with different weather conditions.")
    
    # Plot ride price over temperature
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.scatterplot(data=df_rideshare, x='temperature', y='price')
    plt.title('Ride Price Over Temperature')
    plt.xlabel('Temperature')
    plt.ylabel('Price')
    st.pyplot(fig)
    st.markdown('---')

    # Display scatter plot
    st.subheader('Visualization of travel patterns')
    st.write("Explore travel patterns, such as the most common destinations, travel times, and distances.")
    
    # Plot common destinations
    st.subheader('Most Common Destinations')
    top_destinations = df_rideshare['destination'].value_counts().head(10)
    st.bar_chart(top_destinations)
    
    # Plot travel times
    st.subheader('Travel Times')
    fig, ax = plt.subplots()
    sns.histplot(df_rideshare['hour'], bins=24, kde=True, ax=ax)
    ax.set_xlabel('Hour of Day')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of Travel Times')
    st.pyplot(fig)
    
    # Plot distances
    st.subheader('Travel Distances')
    fig, ax = plt.subplots()
    sns.histplot(df_rideshare['distance'], bins=20, kde=True, ax=ax)
    ax.set_xlabel('Distance')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of Travel Distances')
    st.pyplot(fig)


# Run Streamlit app
if __name__ == '__main__':
    main()

