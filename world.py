import json

def openFile():
    with open('countries.json') as f:
        collectedData = json.loads(f.read())
        return collectedData

def listData():
    worldInfo = openFile()
    for info in worldInfo:
        print("{country} has {popMillion} million people {leadCity} {language}".format(**info))

def editData():
    whichCountry = input("What country would you like to edit?")
    changeCapital = input("what is the new capital city? ")
    
    oldVersion = openFile()

    newVersion = []
    
    print (changeCapital)
    
    for each in oldVersion:
        if(each['country']== whichCountry):
            print("new")
            print(each['leadCity'])
            newRow = {}
            newRow['language'] = each['language']
            newRow['country'] = each['country']
            newRow['popMillion'] = each['popMillion']
            newRow['leadCity'] = changeCapital
            newVersion.append(newRow)
        else:
            newRow = {}
            newRow['language'] = each['language']
            newRow['country'] = each['country']
            newRow['popMillion'] = each['popMillion']
            newRow['leadCity'] = each['leadCity']
            newVersion.append(newRow)
    with open('countries.json','w') as f:
        f.write(json.dumps(newVersion))
        

    listData()    



def menu():
    choices = [
        "view worlds",
        "change world details"
    ]
    for each in range(len(choices)):
        print("{}. {}".format(each + 1, choices[each]))
        
    yourChoice = int(input("please select"))
    
    if yourChoice == 1:
        listData()
    elif yourChoice == 2:
        editData()
    else:
        print("didn't understand?")
def main():
    menu()

main()