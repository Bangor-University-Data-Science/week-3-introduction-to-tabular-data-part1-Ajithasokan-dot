import pandas as pd

def create_summary_table(df):
    """
    Creates a summary table for the DataFrame, providing information about each feature.
    
    Args:
        df (pd.DataFrame): The DataFrame to summarize.
    
    Returns:
        pd.DataFrame: A summary DataFrame with feature names, data types, missing values, and unique counts.
    """
    summary_data = {
        'Feature Name': df.columns,
        'Data Type': df.dtypes.values,
        'Has Missing Values?': df.isnull().any().values,
        'Number of Unique Values': df.nunique().values
    }
    
    return pd.DataFrame(summary_data)

def test_create_summary_table():
    # Mock a DataFrame
    mock_df = pd.DataFrame(data={
        'Age': [22, 38, 26, 35, None],
        'Sex': ['male', 'female', 'female', 'male', 'male'],
        'Survived': [0, 1, 1, 0, 1]
    })
    
    summary_df = create_summary_table(mock_df)
    
    assert 'Feature Name' in summary_df.columns, f"Summary should include 'Feature Name'. Found columns: {summary_df.columns.tolist()}"
    assert 'Data Type' in summary_df.columns, f"Summary should include 'Data Type'. Found columns: {summary_df.columns.tolist()}"
    assert 'Has Missing Values?' in summary_df.columns, f"Summary should include 'Has Missing Values?'. Found columns: {summary_df.columns.tolist()}"
    assert 'Number of Unique Values' in summary_df.columns, f"Summary should include 'Number of Unique Values'. Found columns: {summary_df.columns.tolist()}"

# Run the test
test_create_summary_table()
