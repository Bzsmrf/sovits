from main import *


artistDictionary = {}
artistDictionary['Drake']  = "so-vits-svc-fork\src\so_vits_svc_fork\inference\drake05 G_166400.pth config.json 0"
artistDictionary['Eminem'] = "so-vits-svc-fork\src\so_vits_svc_fork\inference\eminem general model 86k.zip G_86400.pth  config.json 0"
artistDictionary['Kanye']  = "so-vits-svc-fork\src\so_vits_svc_fork\inference\ye200k G_199200.pth config.json 0"
print("Artist List: Drake, Eminem, Kanye.")
name = input("Enter Artist: ")
def convert_with_sovits(artistDictioary, name):
    if name not in artistDictioary:
        print("Invalid Artist")
        return
    myList = artistDictioary[name].split()
    infer(input_path='input/input.wav', output_path= 'output/output.wav', model_path = ' '.join(myList[0:-3]) + "/" + myList[-3], config_path = ' '.join(myList[0:-3]) + "/" + myList[-2], speaker = myList[-1])
convert_with_sovits(artistDictionary, name)