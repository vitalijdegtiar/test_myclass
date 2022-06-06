from api import Moyclass
from settings import apiKey

mc = Moyclass()

def test_get_token_valid_apiKey(apiKey = apiKey):
    status, result = mc.get_token(apiKey)
    assert status == 200
    assert "accessToken" in result