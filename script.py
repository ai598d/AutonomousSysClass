import aspose.words as aw
import os

folder_name = "Lecture5"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
doc = aw.Document("Lecture5.mht")
doc.save("Lecture5/Lecture5.html")




print("Folder created!")
print("Done")