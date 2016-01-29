import pyminizip
import requests
import os

# REQUIRED
# 1. Python 2.7
# 2. requests [ $ pip install requests ]
# 3. pyminizip

# function to request url
def request_url(url_get):
    headers = {}
    print("requesting.....")
    response = requests.request("GET", url_get, headers=headers)
    print("success")
    return response.text

# function to save your informations
def encrypt_file(password, file_to_encrypt, zip_name):
    pyminizip.compress(file_to_encrypt, zip_name, password, 5)
    delete_file_txt(file_to_encrypt)

# save file in same folder
def save_as_txt(file_name, file_content):
    f = open(file_name,'w')
    f.write(file_content)
    f.close()
    return file_name

# delete file (txt)
def delete_file_txt(file_name):
    if os.path.isfile(file_name):
        os.remove(file_name)


url_to_get        = raw_input("Url to GET: ")
file_name_to_save = "content_file.txt"
zip_name_to_save  = raw_input("Zip name (without .zip): ") + ".zip"
zip_password      = raw_input("Zip password: ")

#  save file
txt_file = save_as_txt(file_name_to_save, request_url(url_to_get))

# encrypt file
encrypt_file(zip_password, txt_file, zip_name_to_save)
print("Finish ;)")
