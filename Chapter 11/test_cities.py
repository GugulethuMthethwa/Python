import pytest
from city_functions import city_country

def test_city_country():
    """Test that city_country returns the correct format."""
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'

# Uncomment the following line to run the tests directly with pytest
# if __name__ == "__main__":
#     pytest.main()