import pandas as pd

def display_unique_values(df, categorical_features):
    """
    Displays unique values for each categorical feature in the DataFrame.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        categorical_features (list): List of categorical feature names.
    
    Returns:
        dict: A dictionary where keys are feature names and values are the unique values.
    """
    unique_values = {}
    for feature in categorical_features:
        unique_values[feature] = df[feature].unique().tolist()
    return unique_values

def test_display_unique_values():
    # Mock a DataFrame
    mock_df = pd.DataFrame(data={
        'Sex': ['male', 'female', 'female', 'male'],
        'Embarked': ['S', 'C', 'S', 'Q']
    })
    categorical_features = ['Sex', 'Embarked']
    
    unique_values = display_unique_values(mock_df, categorical_features)
    
    assert isinstance(unique_values, dict), "The result should be a dictionary"
    assert 'Sex' in unique_values and 'Embarked' in unique_values, "Both categorical features should be in the result"
    assert sorted(unique_values['Sex']) == ['female', 'male'], "Unique values for 'Sex' should be correct"
    assert sorted(unique_values['Embarked']) == ['C', 'Q', 'S'], "Unique values for 'Embarked' should be correct"

# Run the test
test_display_unique_values()

