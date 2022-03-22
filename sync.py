import requests
import csv
from urllib.parse import urljoin
import sqlite3

server_url = "http://54.202.87.52:3000/api/"
#server_url = "http://localhost:3000/api/"

def get_count():
    # con = sqlite3.connect("midterm.db")
    # cur = con.cursor()
    # count =  list(cur.execute('SELECT MAX(count) FROM data '))[0]
    # con.close()
    # if count[0] is None:
    #     count = 0
    # else:
    #     count = count[0]
    count = 0
    return count

def sync(count):
    endpoint = "messages"
    sync_payload = {
        "count": count
    }
    r = requests.get(urljoin(server_url,endpoint), data=sync_payload)
    return (r.status_code == 201, r.json())

def write_csv(res):
    keys = res["data"][0].keys()
    with open('sync.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(res["data"])
    
    print("successfully write csv")

# def write_csv2(res):
#     keys = res["cdata"][0].keys()
#     with open('sync2.csv', 'w', newline='') as output_file:
#         dict_writer = csv.DictWriter(output_file, keys)
#         dict_writer.writeheader()
#         dict_writer.writerows(res["cdata"])
    
#     print("successfully write csv")


def main():
    con = sqlite3.connect("midterm.db")
    cur = con.cursor()

if __name__ == "__main__":
    # status, res = sync()
    count = get_count()
    status, res = sync(count)

    write_csv(res)

    print(res["valid"])
    print(res["data"])
    
    print(count)
    #print(res)
    