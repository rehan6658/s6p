import os
import sys
import subprocess

links_dict = {
    "601": [
        "https://nig-veloper.github.io/s6p/601/1.txt", "https://nig-veloper.github.io/s6p/601/2.txt", "https://nig-veloper.github.io/s6p/601/3.txt", "https://nig-veloper.github.io/s6p/601/4.txt", "https://nig-veloper.github.io/s6p/601/5.txt", "https://nig-veloper.github.io/s6p/601/6.txt", "https://nig-veloper.github.io/s6p/601/7.txt", "https://nig-veloper.github.io/s6p/601/8.txt", "https://nig-veloper.github.io/s6p/601/9.txt", "https://nig-veloper.github.io/s6p/601/theory.txt", "https://nig-veloper.github.io/s6p/601/10.txt"],

    "602": [
        "https://nig-veloper.github.io/s6p/602/1.txt", "https://nig-veloper.github.io/s6p/602/2.txt", "https://nig-veloper.github.io/s6p/602/3.txt", "https://nig-veloper.github.io/s6p/602/4.txt", "https://nig-veloper.github.io/s6p/602/5.txt", "https://nig-veloper.github.io/s6p/602/6.txt", "https://nig-veloper.github.io/s6p/602/7.txt", "https://nig-veloper.github.io/s6p/602/8.txt"],

    "604": [
        "https://nig-veloper.github.io/s6p/604/1.txt", "https://nig-veloper.github.io/s6p/604/2.txt", "https://nig-veloper.github.io/s6p/604/3.txt", "https://nig-veloper.github.io/s6p/604/4.txt", "https://nig-veloper.github.io/s6p/604/5.txt", "https://nig-veloper.github.io/s6p/604/6.txt", "https://nig-veloper.github.io/s6p/604/7.txt", "https://nig-veloper.github.io/s6p/604/8.txt", "https://nig-veloper.github.io/s6p/604/9.txt"],
    
    "606": [
        "https://nig-veloper.github.io/s6p/606/1.txt", "https://nig-veloper.github.io/s6p/606/2.txt", "https://nig-veloper.github.io/s6p/606/3.txt", "https://nig-veloper.github.io/s6p/606/4.txt", "https://nig-veloper.github.io/s6p/606/5.txt", "https://nig-veloper.github.io/s6p/606/6.txt", "https://nig-veloper.github.io/s6p/606/7.txt", "https://nig-veloper.github.io/s6p/606/8.txt", "https://nig-veloper.github.io/s6p/606/9.txt", "https://nig-veloper.github.io/s6p/606/mongo.txt", "https://nig-veloper.github.io/s6p/606/10.txt"
    ],

    "607":[
        "https://nig-veloper.github.io/s6p/607/1.txt", "https://nig-veloper.github.io/s6p/607/2.txt", "https://nig-veloper.github.io/s6p/607/3.txt", "https://nig-veloper.github.io/s6p/607/4.txt", "https://nig-veloper.github.io/s6p/607/5.txt", "https://nig-veloper.github.io/s6p/607/7.txt", "https://nig-veloper.github.io/s6p/607/8.txt", "https://nig-veloper.github.io/s6p/607/9.txt","https://nig-veloper.github.io/s6p/607/10.txt"

    ]
}


if len(sys.argv) > 1:
    arg = sys.argv[1]
else:
    print("Enter subject code ( python get_subject.py 601 )")
    sys.exit()


if arg in links_dict:
    links = links_dict[arg]
else:
    print("Invalid subject code")
    sys.exit()


base_location = input("Enter Abs Folder location eg(C:/Users/) : ")
dir_name = "{}{}".format(base_location, arg)
os.makedirs(dir_name, exist_ok=True)


for link in links:
    file_name = os.path.basename(link)
    file_path = os.path.join(dir_name, file_name)
    subprocess.call(['curl', '-s', '-o', file_path, link])
    print("Downloaded {link} to {file_path}".format(link=link, file_path=file_path))
