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


#file classification
print("\n" + "-"*20 + " FILE CLASSIFICATION " + "-"*20)
classified_files = {
    "PDFs": [],
    "Images": [],
    "Videos": [],
    "Documents": [],
    "Spreadsheets": [],
    "Other": []
}
for file in files:
    if "." in file:
        extension = "." + file.split(".")[-1].lower()
    else:
        extension = ""
    found = False
    
    for category, extensions in file_categories.items():
        if extension in extensions:
            classified_files[category].append(file)
            found = True
            break

    if not found:
        classified_files["Other"].append(file)

print("\n========== CLASSIFIED FILES ==========")

for category, file_list in classified_files.items():
    print(category, ":", file_list)

#counting files 
print("\n" + "-"*20 + " COUNTING FILES " + "-"*20)            
category_counts = {}
for category, file_list in classified_files.items():
    category_counts[category] = len(file_list)

print("\n========== FILE SUMMARY ==========")

for category, count in category_counts.items():
    print(category, ":", count)
total_classified_files = sum(category_counts.values())
print("\nTotal Classified Files:", total_classified_files)     

#Creating reusable function
def organize_files(files, file_categories):

    classified_files = {
        "PDFs": [],
        "Images": [],
        "Videos": [],
        "Documents": [],
        "Spreadsheets": [],
        "Other": []
    }

    # Classify files
    for file in files:

        if "." in file:
            extension = "." + file.rsplit(".", 1)[-1].lower()
        else:
            extension = ""

        found = False

        for category, extensions in file_categories.items():

            if extension in extensions:

                classified_files[category].append(file)
                found = True
                break

        if not found:
            classified_files["Other"].append(file)

    # Count files
    category_counts = {}

    for category, file_list in classified_files.items():
        category_counts[category] = len(file_list)

    # Display report
    print("\n========== ORGANIZER REPORT ==========")

    for category, file_list in classified_files.items():
        print(category, ":", file_list)

    print("\n========== CATEGORY COUNTS ==========")

    for category, count in category_counts.items():
        print(category, ":", count)

    print("\nTotal Files:", sum(category_counts.values()))

    return classified_files


# CALL THE FUNCTION

print("\n========== REUSABLE FUNCTION TEST ==========")

result = organize_files(files, file_categories)
