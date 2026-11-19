("="*30 + "FILE CLASSIFICATION ENGINE " + "="*30)

#sample files 
print("-"*20 + " SAMPLE FILES " + "-"*20)
files = ["invoice.pdf",
        "photo.jpg",
        "image.heic",
        "video.mp4",
        "apple.mov",
        "report.docx",
        "data.xlsx",
        "logo.png",
        "notes.txt",
        "su.csv",
        "presentation.pptx",
        "design.heic",
        "README"]
print(files)
print("Total files: ", len(files))

#file category
print("-"*20 + " FILE CATEGORIES " + "-"*20)
file_categories = {
    "Images" : [".jpg", ".heic", ".png"],
    "Videos" : [".mp4", ".mov"],
    "Documents" : [ ".pptx",".docx", ".txt"],
    "PDFs" : [".pdf"],
    "Spreadsheets" : [".xlsx", ".csv"],
    "Other" : [] 
}
print(file_categories)

#file extraction
print("-"*20 + " FILE EXTENSIONS " + "-"*20)
file_extensions = []
for file in files:
    if "." in file:
        file_extensions.append("."+file.split(".")[-1])
print(file_extensions)
print("Number of extensions: " ,len(file_extensions))
