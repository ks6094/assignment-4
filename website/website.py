import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(uploaded_file)

        # Handle empty DataFrame
        if df.empty:
            st.warning("The uploaded CSV file is empty.")
        else:
            # Display the DataFrame
            st.write("Data Preview:")
            st.dataframe(df.head(), use_container_width=True)

            # Display basic statistics
            st.write("Basic Statistics:")
            st.write(df.describe())

            # Filter Data
            st.write("Filter Data")
            column = st.selectbox("Select a column to filter by", df.columns)
            column_values = df[column].unique()
            selected_value = st.selectbox("Select a value", column_values)
            filtered_df = df[df[column] == selected_value]

            # Handle empty filtered DataFrame
            if filtered_df.empty:
                st.warning("No data matches the selected filter criteria.")
            else:
                st.write("Filtered Data:")
                st.dataframe(filtered_df, use_container_width=True)

                # Plot data
                st.write("Plot data")
                x_axis = st.selectbox("Select X-axis", df.columns)
                y_axis = st.selectbox("Select Y-axis", df.columns)

                if st.button("Generate Plot"):
                    plt.figure(figsize=(10, 6))
                    plt.scatter(df[x_axis], df[y_axis], alpha=0.7)
                    plt.title(f"{y_axis} vs {x_axis}")
                    plt.xlabel(x_axis)
                    plt.ylabel(y_axis)
                    st.pyplot(plt)

    except Exception as e:
        st.error(f"An error occurred: {e}")

