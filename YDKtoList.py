import os
import os.path
from time import sleep
import io
User = raw_input("What is your user name? (Must be exact)  ")
EC = 0


NCC = 0


IDCC = 0     

NamePath = ("CardNames.txt")
#NameList = open(NamePath).read().splitlines()

IDPath = ("CardIDs.txt")
#IDList = open(IDPath).read().splitlines()

DekPath = ("C:\\Users\\"+User+"\\AppData\\Roaming\\YGOPro\\deck\\")
DekInput = raw_input("Input deck file name (e.g. HERO.ydk)")
Dek = DekPath + DekInput +".ydk"
#DekList = open(Dek).read().splitlines()

file1 = open(DekInput+" Deck List.txt", "wt")

with open(Dek) as DekFile:
    for entry in DekFile:
        #print entry
        #print "Good"
        EC += 1
        with open(IDPath) as IDFile:
            for IDCheck in IDFile:
                #print "ok"
                #print IDCheck
                IDCC += 1
                if entry == IDCheck:
                    #print "ID Found."
                    with open(NamePath) as NameFile:
                        for NameCheck in NameFile:
                            NCC += 1
                            #print "NameChecking"
                            #print IDCC
                            #print NCC
                            if IDCC == NCC:
                                #print "Fileing..."
                                toFile = NameCheck
                                #print "Filed"
                                file1.write(toFile)
                        NCC = 0
            IDCC = 0
    EC = 0

file1.close()
print "Done."
raw_input("Press Enter to quit.")
#print NCC
#print IDCC

