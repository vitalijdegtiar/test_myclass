import requests

class Moyclass:
    def __init__(self):
        self.base_url = "https://api.moyklass.com/"

    def get_token(self, apiKey):

        headers = {
            "apiKey": apiKey
                    }

        res = requests.post(self.base_url+'v1/company/auth/getToken', headers=headers)
        status = res.status_code

        result = ""
        try:
            result = res.json()
        except:
            result = res.text()

        return status, result