from main import *


artistDictionary = {}
artistDictionary['Drake']  = "G_166400.pth config.json 0"
artistDictionary['Eminem'] = ""
artistDictionary['Kanye']  = ""
print("Artist List: Drake, Eminem, Kanye.")
name = input("Enter Artist: ")
def convertAudio(artistDictioary, name):
    if name not in artistDictioary:
        print("Invalid Artist")
        return
    myList = artistDictioary[name].split()
    infer(input_path='input/input.wav', output_path= 'output/output.wav', model_path = myList[0], config_path = myList[1], speaker = myList[2])
convertAudio(artistDictionary, name)
