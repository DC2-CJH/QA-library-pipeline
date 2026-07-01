"""Example test to demonstrate pytest.

Copy this pattern for your own tests!
"""

#import pytest
#import pandas as pd


#@pytest.fixture
#def sample_df():
#    """Sample DataFrame for testing."""
#    return pd.DataFrame({
#        'id': [1, 2, 3],
#        'name': ['Alice', 'Bob', 'Charlie']
#    })


#def test_example(sample_df):
#    """Example test - shows pytest working."""
#    assert len(sample_df) == 3
#    assert 'id' in sample_df.columns
#    assert sample_df['id'].is_unique

# Attempt 1 - splitting out the tests
#import pytest
#import pandas as pd


#@pytest.fixture
#def sample_df():
#    """Sample DataFrame for testing."""
#    return pd.DataFrame({
#        'id': [1, 2, 3],
#        'name': ['Alice', 'Bob', 'Charlie']
#    })

#def test_example_Length(sample_df):
#    """Example test - shows pytest working."""
#    assert len(sample_df) == 3

#def test_example_IDs(sample_df):
#    """Example test - shows pytest working."""
#    assert 'id' in sample_df.columns

#def test_example_Unique(sample_df):
#    """Example test - shows pytest working."""
#    assert sample_df['id'].is_unique

# Attempt 2 - More ID's/entries into the data (4, 5 and 6)
import pytest
import pandas as pd


@pytest.fixture
def sample_df():
    """Sample DataFrame for testing."""
    return pd.DataFrame({
        'id': [1, 2, 3, 4, 5 ,6],
        'name': ['Alice', 'Bob', 'Charlie', 'Bob', 'Adam', 'Sarah']
    })

def test_example_Length(sample_df):
    """Example test - shows pytest working."""
    assert len(sample_df) == 6

def test_example_IDs(sample_df):
    """Example test - shows pytest working."""
    assert 'id' in sample_df.columns

def test_example_Unique(sample_df):
    """Example test - shows pytest working."""
    assert sample_df['id'].is_unique