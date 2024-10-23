import pandas as pd

def get_numerical_df(df, numerical_features):
    """
    Creates a DataFrame containing only numerical features.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        numerical_features (list): List of numerical feature names.
    
    Returns:
        pd.DataFrame: DataFrame containing only numerical features.
    """
    return df[numerical_features]

def test_get_numerical_df():
    # Mock a DataFrame
    mock_df = pd.DataFrame(data={
        'Age': [22, 38, 26, 35],
        'Fare': [7.25, 71.83, 7.92, 53.10],
        'Survived': [0, 1, 1, 0]
    })
    numerical_features = ['Age', 'Fare']
    
    numerical_df = get_numerical_df(mock_df, numerical_features)
    
    assert not numerical_df.empty, "Numerical DataFrame should not be empty"
    assert all(col in numerical_df.columns for col in numerical_features), "All numerical features should be present"
    assert numerical_df.shape[1] == len(numerical_features), "Numerical DataFrame should have the correct number of columns"

# Run the test
test_get_numerical_df()
