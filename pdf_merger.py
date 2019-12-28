from PyPDF2 import PdfFileMerger
import os
import glob
import fire

def mergefunction(output="MERGE"):
	files = glob.glob("*.pdf")
	cwd = os.getcwd()
	path = cwd+"\\"

	merger = PdfFileMerger()

	for file in files:
		merger.append(path+file)
	if not os.path.exists(path+output+".pdf"):
		merger.write(path+output+".pdf")
	merger.close()
	print("oki doki")

if __name__ == '__main__':
  fire.Fire(mergefunction)