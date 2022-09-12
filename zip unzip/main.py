import zipfile

file = "C:\\Users\\a.cuko\\Desktop\\DEV\\100 Projects\\zip unzip\\zip\\contain.zip"
targetdir = "C:\\Users\\a.cuko\\Desktop\\DEV\\100 Projects\\zip unzip\\unzip\\container"


with zipfile.ZipFile(file,"r") as zip_ref:
    zip_ref.extractall(targetdir)