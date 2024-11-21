import streamlit as st
import pandas as pd
import plotly.express as px

# Title and Description
st.title("Interactive Data Visualization Tool")
st.write("""
Upload a dataset in CSV format and select the type of visualization you want to create.
This tool supports interactive visualizations for enhanced data exploration.
""")

# File Uploads
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        # Load data
        data = pd.read_csv(uploaded_file)
        st.write("## Dataset Preview")
        st.write(data.head())
        
        # Data Info
        st.write("### Data Details")
        st.write("Number of Rows:", data.shape[0])
        st.write("Number of Columns:", data.shape[1])
        st.write("Column Names:", list(data.columns))
        st.write("Data Types:", data.dtypes)
        
        # Select Plot Type
        st.write("## Select Visualization Type")
        plot_type = st.selectbox("Choose a plot type", ["Scatter Plot", "Line Plot", "Bar Plot", "Histogram", "Box Plot", "Heatmap"])

        # Common options for all plots (excluding Heatmap)
        if plot_type != "Heatmap":
            x_col = st.selectbox("Select X-axis", data.columns)
            y_col = st.selectbox("Select Y-axis", data.columns)
        
        # Generate plots based on the selected type
        if st.button("Generate Plot"):
            if plot_type == "Scatter Plot":
                fig = px.scatter(data, x=x_col, y=y_col, title=f'Scatter Plot of {x_col} vs {y_col}')
                st.plotly_chart(fig)

            elif plot_type == "Line Plot":
                fig = px.line(data, x=x_col, y=y_col, title=f'Line Plot of {x_col} vs {y_col}')
                st.plotly_chart(fig)

            elif plot_type == "Bar Plot":
                fig = px.bar(data, x=x_col, y=y_col, title=f'Bar Plot of {x_col} vs {y_col}')
                st.plotly_chart(fig)

            elif plot_type == "Histogram":
                fig = px.histogram(data, x=x_col, title=f'Histogram of {x_col}')
                st.plotly_chart(fig)

            elif plot_type == "Box Plot":
                fig = px.box(data, x=x_col, y=y_col, title=f'Box Plot of {y_col} by {x_col}')
                st.plotly_chart(fig)

            elif plot_type == "Heatmap":
                # For heatmap, no need for x_col, y_col selection
                corr_matrix = data.corr()  # Calculate correlation matrix
                fig = px.imshow(corr_matrix, title="Correlation Heatmap")
                st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Error: {e}")
