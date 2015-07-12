import os, os.path, io, sys
from time import sleep
from ListFormat import SortMain
import YesOrNo as yon
import sqlite3 as lite
if os.path.exists("CardIDs.txt"):
	os.remove("CardIDs.txt")
if os.path.exists("CardNames.txt"):
	os.remove("CardNames.txt")


User = raw_input("What is your WINDOWS user name? (Must be exact)  ")

con = lite.connect("C:\\Users\\"+User+"\\AppData\\Roaming\\YGOPro\\cards.cdb")

with con:
	IDST = open("CardIDs.txt", "w")
	NMS = open("CardNames.txt", "w")
	cur = con.cursor() 
	print "OK"	
	cur.execute("SELECT * FROM texts")
	
	while True:
		row = cur.fetchone()
		if row == None:
			break
		NMS.write("%s\n" % row[1].encode('utf-8'))
		IDST.write("%s\n" % row[0])
		
		# This will create a new file or **overwrite an existing file**.
		
		#IDST.writelines(row[0]) # Write a sequence of strings to a file
		
	NMS.close()
	IDST.close()
if not os.path.exists("Lists\\"): os.makedirs("Lists\\")
folder = "Lists\\"



DekFolder = "C:\\Users\\"+User+"\\AppData\\Roaming\\YGOPro\\deck\\"


	
path = (DekFolder)
dirList=os.listdir(path)
mylst = map(lambda each:each.strip(".ydk"), dirList)

EC = 0


NCC = 0


IDCC = 0     

NamePath = ("CardNames.txt")
#NameList = open(NamePath).read().splitlines()

IDPath = ("CardIDs.txt")
#IDList = open(IDPath).read().splitlines()

DekPath = (DekFolder)
for pname in mylst:
	print pname
print ""
print "Input deck file name from the list"
DekInput = raw_input()
Dek = DekPath + DekInput +".ydk"
#DekList = open(Dek).read().splitlines()
DekOut = DekInput+" Deck List"
DekOutF = folder+DekOut+".txt"

file1 = open(DekOutF, "wt")

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
clean = raw_input("Would you like to format?  ")
yon.ans(clean, "y", "n", "Format complete")
SortMain(DekOut)
raw_input("Press Enter to quit.")
#print NCC
#print IDCC


