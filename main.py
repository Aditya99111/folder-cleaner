import os

def creat_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move_files(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}") 

if __name__ == "__main__":
        
    files = os.listdir()
    files.remove("main.py")
    creatfolder('Images')
    creatfolder('Docs')
    creatfolder('code')
    creatfolder('Media')
    creatfolder('Others')
    

    imgExts = [".png", ".jpg", ".jpeg",".webp",".svg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts ]

    docExts = [".txt", ".docx", "doc", ".pdf"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

    codeExts = [".py", ".html", ".css", ".js",".c",".cc",".c++"]
    code = [file for file in files if os.path.splitext(file)[1].lower() in codeExts]

    mediaExts = [".mp4", ".mp3", ".flv"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and (ext not in codeExts) and os.path.isfile(file):
            others.append(file)

    move("Images", images)
    move("Docs", docs)
    move("Media", medias)
    move("Others", others)
    move("code", code)
