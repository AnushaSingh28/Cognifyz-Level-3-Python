import pandas as pd
import os

def clean_data(input_file):
    """
    This function loads the data, cleans it, and returns the cleaned data.
    """
    try:
        data = pd.read_csv(input_file)
        
        # Print column names before stripping spaces
        print("Column Names before stripping:", data.columns)
        
        # Strip any leading/trailing spaces from column names
        data.columns = data.columns.str.strip()
        
        # Print column names after stripping spaces
        print("Column Names after stripping:", data.columns)

        
        if 'Amount' not in data.columns:
            raise ValueError("Column 'Amount' not found in the dataset")

        # Remove duplicate rows
        data.drop_duplicates(inplace=True)

        # Fill missing values (if any)
        data.ffill(inplace=True)

        # Remove any rows where the 'Amount' column is negative (if applicable)
        data = data[data['Amount'] >= 0]
        
        # Convert 'Date' to datetime format if it exists
        if 'Date' in data.columns:
            data['Date'] = pd.to_datetime(data['Date'], errors='coerce', dayfirst=True)

        return data
    except Exception as e:
        print(f"Error in clean_data: {e}")
        return None

def generate_report(data, output_file):
    """
    This function generates a summary report (average, sum, etc.) and saves it to an output file.
    """
    try:
        # Generate summary statistics (for example, total and average of 'Amount' column)
        summary = data[['Amount']].agg(['sum', 'mean', 'min', 'max', 'std'])
        
        # Save summary statistics to a CSV file
        summary.to_csv(output_file)
        print(f"Report saved to {output_file}")
    except Exception as e:
        print(f"Error in generate_report: {e}")

def save_cleaned_data(data, output_file):
    """
    This function saves the cleaned data to a CSV file.
    """
    try:
        data.to_csv(output_file, index=False)
        print(f"Cleaned data saved to {output_file}")
    except Exception as e:
        print(f"Error in save_cleaned_data: {e}")

def automate_task(input_file, cleaned_output_file, report_output_file):
    """
    This function automates the whole process: cleaning data, generating a report, and saving the results.
    """
    
    cleaned_data = clean_data(input_file)
    
    if cleaned_data is not None:
        
        save_cleaned_data(cleaned_data, cleaned_output_file)
          
        generate_report(cleaned_data, report_output_file)


base_dir = r"C:\Users\HP\OneDrive\Desktop\Cognifyz_Python_development_intership_task\Level-3"

input_file = os.path.join(base_dir, 'monthly_sales.csv')  
cleaned_output_file = os.path.join(base_dir, 'cleaned_sales_data.csv') 
report_output_file = os.path.join(base_dir, 'sales_summary_report.csv')  

automate_task(input_file, cleaned_output_file, report_output_file)
