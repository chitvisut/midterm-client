import requests
from urllib.parse import urljoin

def postReq(data):
    r = requests.post("http://localhost:3000/api/messages", data=data)
    return (r.status_code == 201, r.json())

def putReq(id,data):
    r = requests.put(urljoin("http://localhost:3000/api/messages/", id), data=data)
    return (r.status_code == 201, r.json())

def delReq(id):
    r = requests.delete(urljoin("http://localhost:3000/api/messages/", id))
    return (r.status_code == 201, r.json())

def main():

    # post_payload = {
    #     "uuid": "aaa111",
    #     "author": "genesis",
    #     "message": "Hello world!",
    #     "likes" : 1
    # }

    # status, res = postReq(post_payload)
    # print(status, res["message"])

    # post_payload = {
    #     "uuid": "bbb222",
    #     "author": "genesis",
    #     "message": "Hello world!",
    #     "likes" : 1
    # }

    # status, res = postReq(post_payload)
    # print(status, res["message"])

    # post_payload = {
    #     "uuid": "ccc333",
    #     "author": "genesis",
    #     "message": "Hello world!",
    #     "likes" : 1
    # }

    # status, res = postReq(post_payload)
    # print(status, res["message"])

    # post_payload = {
    #     "uuid": "ddd444",
    #     "author": "genesis",
    #     "message": "Hello world!",
    #     "likes" : 1
    # }

    # status, res = postReq(post_payload)
    # print(status, res["message"])

    # post_payload = {
    #     "uuid": "ddd444",
    #     "author": "genesis",
    #     "message": "Hello world!",
    #     "likes" : 1
    # }

    # status, res = postReq(post_payload)
    # print(status, res["message"])

    # post_payload = {
    #     "uuid": "eee555",
    #     "author": "genesis",
    #     "message": "Hello world!",
    #     "likes" : 1
    # }

    # status, res = postReq(post_payload)
    # print(status, res["message"])

    # post_payload = {
    #     "uuid": "fff666",
    #     "author": "genesis",
    #     "message": "Hello world!",
    #     "likes" : 1
    # }

    # status, res = postReq(post_payload)
    # print(status, res["message"])

    # post_payload = {
    #     "uuid": "ggg777",
    #     "author": "genesis",
    #     "message": "Hello world!",
    #     "likes" : 1
    # }

    # status, res = postReq(post_payload)
    # print(status, res["message"])

    # post_payload = {
    #     "uuid": "hhh888",
    #     "author": "genesis",
    #     "message": "Hello world!",
    #     "likes" : 1
    # }

    # status, res = postReq(post_payload)
    # print(status, res["message"])

    # post_payload = {
    #     "uuid": "iii999",
    #     "author": "genesis",
    #     "message": "Hello world!",
    #     "likes" : 1
    # }

    # status, res = postReq(post_payload)
    # print(status, res["message"])

    post_payload = {
        "uuid": "iii999",
        "author": "genesis",
        "message": "Hello world!",
        "likes" : 1
    }

    status, res = postReq(post_payload)
    print(status, res["message"])

    post_payload = {
        "uuid": "jjj123",
        "author": "genesis",
        "message": "Hello world!",
        "likes" : 1
    }

    status, res = postReq(post_payload)
    print(status, res["message"])

    uuid = "bbb222"
    post_payload = {
        "author": "change",
        "message": "Hey World",
        "likes" : 1
    }

    status, res = putReq(uuid, post_payload)
    print(status, res["message"])

    uuid = "jjj123"
    post_payload = {
        "author": "change",
        "message": "Hey World",
        "likes" : 1
    }

    status, res = putReq(uuid, post_payload)
    print(status, res["message"])

    uuid = "ccc333"
    status, res = delReq(uuid)
    print(status, res["message"])

    uuid = "bbb333"
    status, res = delReq(uuid)
    print(status, res["message"])

    uuid = "bbb222"
    status, res = delReq(uuid)
    print(status, res["message"])


if __name__ == "__main__":
    main()
