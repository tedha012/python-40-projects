from os import linesep
import googletrans

translator = googletrans.Translator()

read_file_path = r"./transtext.txt"

with open(read_file_path, "r") as f:
    readLines = f.readlines()

for lines in readLines:
    result1 = translator.translate(lines, dest="ko")
    print(result1.text)
