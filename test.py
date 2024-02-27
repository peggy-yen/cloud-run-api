import requests

class MakeApiCall:

    def get_data(self, api):
        response = requests.get(f"{api}")
        if response.status_code == 200:
            print("sucessfully fetched the data")
        else:
            print(f"Hello person, there's a {response.status_code} error with your request")

    def __init__(self, api):
        self.get_data(api)


if __name__ == "__main__":
    api_call_1 = MakeApiCall("http://104.199.144.30/")
    api_call_2 = MakeApiCall("http://10.20.0.4/")
