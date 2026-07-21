import os
import hashlib
import json

print("""

  === FILE INTEGRITY MONITOR ===


""")
if os.path.exists("data/scan_results.json"):
    with open("data/scan_results.json", "r") as file:
        previous_scan = json.load(file)
else:
    previous_scan = {}

folder_path = input(" Enter folder path : ")
folder_path = folder_path.strip('"')

if not os.path.exists(folder_path):
    print("Folder does not exist.")

elif not os.path.isdir(folder_path):
    print("This is not a folder. ")

else:
    print("Valid Folder! ")

    scan_results = {}

    for current_folder, subfolders, files in os.walk(folder_path):

        for filename in files :
            full_path = os.path.join(current_folder, filename)
            with open ( full_path , "rb") as current_file :
                data = current_file.read()
            sha256_hash = hashlib.sha256(data)
            final_hash_object = sha256_hash.hexdigest() 
            scan_results[full_path] = final_hash_object

    print("Scan completed successfully.")
    print(f"Scanned {len(scan_results)} files.")

    new_file_count = 0
    for file_path in scan_results:
        if file_path not in previous_scan:
            print(f"New file: {file_path}")
            new_file_count +=1

    if new_file_count == 0:
        print("No new files detected!!")
    else:
        print(f"\nTotal new files = {new_file_count}") 

    modified_file_count = 0    
    for file_path in scan_results:
        if file_path in previous_scan:
            if previous_scan[file_path] != scan_results[file_path]:
                print(f"Modified file: {file_path}")
                modified_file_count +=1

    if modified_file_count == 0 :
        print("No files are modified!!")
    else:
        print(f"\nTotal modified files = {modified_file_count}")

    deleted_file_count = 0 
    for file_path in previous_scan:
        if file_path not in scan_results:
            print(f"Deleted file :{file_path}")
            deleted_file_count +=1 

    if deleted_file_count == 0 :
        print("No files are deleted!!") 
    else:
        print(f"\nTotal deleted files = {deleted_file_count}")


    with open("Scans/scan_results.json", "w") as file:
        json.dump(scan_results, file, indent=4)
