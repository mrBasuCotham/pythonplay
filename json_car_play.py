import json
def fetchData():
    with open('cars.json') as f:
      collectedData = json.loads(f.read())
      return collectedData

def printData():
  carData = fetchData()
  for each in carData:
    print (f"{each['brand']} {each['model']} {each['type']} {each['mpg']} ")

def main():
   printData()

main()