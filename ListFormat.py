import os
import os.path
from time import sleep
import io
folder = "Lists\\"


def SortMain(DLF=None):
	if DLF == None:
		Deck = raw_input("Enter the name of the deck for list reformatting.   ")
		DeckListPath = folder+Deck+" Deck List.txt"
		DLP = DeckListPath
	else:
		DLP = folder+DLF+".txt"


	LNum = 0
	LFile = open(DLP)


	with LFile as f:
		lines = f.read().splitlines()
		#print lines
	LFile.close()

	file1 = open(folder+DLF+" Format.txt", "wt")

	#print len(lines)
	for number in range(len(lines)):
		try:
			if lines[LNum] == lines[LNum + 1]:
				if lines[LNum] == lines[LNum + 2]:
					file1.write("3 " + lines[LNum]+"\r\n")
					LNum += 3
				else:
					file1.write("2 " + lines[LNum]+"\r\n")
					LNum += 2
			else:
				file1.write("1 " + lines[LNum]+"\r\n")
				LNum += 1
		except IndexError:
			pass
	file1.close()