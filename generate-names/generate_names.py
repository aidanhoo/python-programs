import json

def readJsonFile():
    with open("names.json", "r") as file:
        firstNames = json.load(file)
        print(firstNames)
        return firstNames

def main():
    readJsonFile()

if __name__ == "__main__":
    main()