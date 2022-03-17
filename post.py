import requests
from urllib.parse import urljoin

server_url = "http://localhost:3000/api/"

#mockup
def getReq():
    endpoint = "messages"
    r = requests.get(urljoin(server_url,endpoint))
    return (r.status_code == 200, r.json())
 
# def sendDataToServer(data):
#     r = requests.post(urljoin(baseUrl, 'messages'), data=data)
#     return (r.status_code == 201, r.text)

def postReq():
    endpoint = "messages"
    post_payload = {
        "uuid": "912a2576-a171-4d3f-9170-fd2ec64559a8",
        "author": "genesis",
        "message": "Hello world!",
        "likes" : 1
    }
    r = requests.post(
        url = urljoin(server_url,endpoint),
        data = post_payload
        )

    return (r.status_code == 200, r.json())


if __name__ == "__main__":
    # status, res = getReq()
    status, res = postReq()
    print(status)
    print(res)