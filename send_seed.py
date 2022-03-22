import csv
import requests
from urllib.parse import urljoin

baseUrl = ""
filename = ""

def sendDataToServer(data):
    r = requests.post(urljoin(baseUrl, 'messages'), data=data)
    return (r.status_code == 201, r.json())


def main():
    csvFile = open(filename)
    reader = csv.DictReader(csvFile)
    rowCounter = 0
    for row in reader:
        retryCounter = 0
        while True:
            (sendOk, returnMessage) = sendDataToServer(row)
            if sendOk:
                print("Row", rowCounter, "sent!")
                break
            else:
                print("Row", rowCounter, "failed to send :", returnMessage)
                print("retry:", retryCounter)
            retryCounter += 1

        rowCounter += 1

    csvFile.close()


if __name__ == "__main__":
    baseUrl = "http://54.202.87.52:3000/api/"
    #baseUrl = "http://localhost:3000/api/"
    filename = "../midterm-data/seed.csv"
    main()
