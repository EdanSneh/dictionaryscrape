import json

file = open("dictionary.json","r")
file2 = open("word.json","w")

jsonfile = json.loads(file.read())

for element in jsonfile:
	file2.write(element+",")

