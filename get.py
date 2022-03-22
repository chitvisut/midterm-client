import requests
import csv
from urllib.parse import urljoin
import json

#server_url = "http://54.202.87.52:3000/api/"
server_url = "http://localhost:3000/api/"

#mockup
def getReq():
    endpoint = "messages"
    r = requests.get(urljoin(server_url, endpoint))
    return (r.status_code == 201, r.json())

if __name__ == "__main__":

    status, res = getReq()

    keys = res["data"][0].keys()

    with open('test3.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(res["data"])

    print(status)
    # print(res["data"])