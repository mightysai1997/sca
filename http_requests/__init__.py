# This is your custom http-requests library
def get(url):
    import requests
    return requests.get(url)

def post(url, data):
    import requests
    return requests.post(url, data)

