import csv
import requests
from urllib.parse import urljoin

# baseUrl = "http://10.2.110.61/api/"
baseUrl = "localhost:3000/api/"
filename = "seed.csv"

def sendDataToServer(data):
    r = requests.post(urljoin(baseUrl, 'msgs'), data=data)
    return (r.status_code == 200, r.json())


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
    # filename = input("Filename : ")
    # baseUrl = input(
    #     "Base URL with trailing / (e.g. http://10.2.110.61/api/) : ")
    baseUrl = "http://localhost:3000/api/"
    filename = "seed.csv"
    main()
