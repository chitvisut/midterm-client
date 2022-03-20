import csv
import requests
from urllib.parse import urljoin

baseUrl = ""
filename = ""
#"000067a3-c7ad-4e45-9a32-657d619c86a1,lovesickIcecream0,e91a31,419302"
#"912a2576-a171-4d3f-9170-fd2ec64559a8"

def putReq(id,data):
    r = requests.post(urljoin(baseUrl, "00000b10-a899-40bc-8779-9ff3dbe30777"), data=data)
    return (r.status_code == 201, r.json())

def main():
    id = "00000b10-a899-40bc-8779-9ff3dbe30777"

    put_payload = {
        #"uuid": "00000b10-a899-40bc-8779-9ff3dbe30777",
        "author": "genesis",
        "message": "Hello world!",
        "likes" : 1
    }

    (sendOk, returnMessage) = putReq(id,put_payload)

    print(sendOk, returnMessage)


if __name__ == "__main__":
    #baseUrl = "http://54.202.87.52:3000/api/massages"
    baseUrl = "http://localhost:3000/api/msg/"
    filename = "../midterm-data/seed.csv"
    main()
