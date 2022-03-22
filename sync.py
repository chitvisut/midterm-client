import sys
import requests
import csv
from urllib.parse import urljoin
import sqlite3

server_url = "http://54.202.87.52:3000/api/"
#server_url = "http://localhost:3000/api/"

def get_count():
    con = sqlite3.connect("midterm.db")
    cur = con.cursor()
    rows =  cur.execute('SELECT * FROM count')
    count = list(rows)[0][1]
    con.close()
    return count

def update_count(count):
    con = sqlite3.connect("midterm.db")
    cur = con.cursor()
    sql = 'UPDATE count SET count = ? WHERE mark = "current"'
    rows =  cur.execute(sql, [count])
    con.commit()
    print(rows)
    con.close()

def get_all():
    con = sqlite3.connect("midterm.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    sql = """SELECT * FROM data"""
    rows = cur.execute(sql)
    ldata = [{k: item[k] for k in item.keys()} for item in rows]
    con.close()
    return ldata


def get_fromlite(valid):
    con = sqlite3.connect("midterm.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    values = valid
    sql = "SELECT * FROM data WHERE uuid IN ({})".format(" ,".join("?" * len(values)))
    rows =  cur.execute(sql, values)
    ldata = [{k: item[k] for k in item.keys()} for item in rows]
    con.close()
    return ldata

def drop_fromlite(valid):
    con = sqlite3.connect("midterm.db")
    cur = con.cursor()
    values = valid
    sql = " DELETE FROM data WHERE uuid NOT IN ({})".format(" ,".join("?" * len(values)))
    cur.execute(sql, values)
    con.commit()
    print("successfully clear outdated data")
    con.close()

def postall_tolite(data):
    con = sqlite3.connect("midterm.db")
    cur = con.cursor()
    sql = """INSERT INTO data (uuid, author, message, likes) VALUES (?, ?, ?, ?)"""

    values = []
    for item in data:
        values.append((item["uuid"], item["author"], item["message"], item["likes"]))

    #print(values)
    cur.executemany(sql, values)
    con.commit()
    con.close()

def remall_tolite():
    con = sqlite3.connect("midterm.db")
    cur = con.cursor()
    sql = """DELETE FROM data"""

    cur.execute(sql)
    con.commit()
    print("successfully all data")
    con.close()

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

def write_csv2(res):
    keys = res[0].keys()
    with open('sync.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(res)
    
    print("successfully write csv")

def main():
    count = get_count()
    print(count)
    status, res = sync(count)
    if res["count"] == count:
        ldata = get_all()
        write_csv2(ldata)
        return print("client is up to date no need to update")

    if res["valid"]:
        print("query somedata from sqlite + data res")
        ldata = get_fromlite(res["valid"])
        #print(res["data"])
        if res["data"]:
            for item in res["data"]:
                ldata.append(item)

        print("then update sqlite and make csv")
        write_csv2(ldata)
        #print(res["valid"])
        drop_fromlite(res["valid"])
        postall_tolite(res["data"])
        update_count(res["count"])
        print("successfully update to local database")

    else:
        print("no valid data on client")
        if count != 0:
            remall_tolite()

        #make csv
        write_csv(res)
        postall_tolite(res["data"])
        update_count(res["count"])
        print("successfully update to local database")

    print(status)
    print(res["message"])

if __name__ == "__main__":
    #remall_tolite()
    if sys.argv:
        server_url = sys.argv[1]
    print("connect to "+server_url)
    main()

 

