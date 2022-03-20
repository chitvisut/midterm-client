from numpy import row_stack
import requests
from urllib.parse import urljoin
import sqlite3

server_url = "http://localhost:3000/api/"

con = sqlite3.connect("midterm.db")
cur = con.cursor()

cur.execute(''' CREATE TABLE data (
                        uuid TEXT PRIMARY KEY UNIQUE,
                        author TEXT NOT NULL,
                        message TEXT NOT NULL,
                        likes INTEGER NOT NULL,
                        count INTEGER NOT NULL
                        )''')

# sql = """INSERT INTO data (uuid, author, message, likes, count) VALUES (?, ?, ?, ?, ?)"""

# values = [
#     ("aaa111","boy","dscdsvsv",1,1),
#     ("aaa222","ploy","dsdddsvsv",2,2),
#     ("aaa333","pailin","dsdddssdsfs",3,3),
#     ("aaa444","pine","dsdddssdsfds",4,4)]

# cur.executemany(sql, values)

#cur.execute("INSERT INTO data VALUES ('aaa111','Boy','i love ploy','123')")

# con.commit()

# # rows =  cur.execute('SELECT * FROM data')
# print(list(rows))

con.close()

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
    #status, res = postReq()
    # print(status)
    # print(res)
    print("hello world")