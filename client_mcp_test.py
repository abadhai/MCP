import requests

def test_multiply(a,b):
    response = requests.post("http://127.0.0.1:8089/path/mcp/multiply", json={"a":a,"b":b})
    if response.status_code ==200:
        print(response.json()["result"])
    else:
        print("there was an issue")    


if __name__== "__main__":
    test_multiply(6,7)