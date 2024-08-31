import os
enter_path = "E:\\STUDY\\Python\\python_programs\\project\\word_to_html"
today = os.path.basename(enter_path)

for filename in os.listdir(f"{enter_path}"):
    print(filename)
    file_path = os.path.join(f"{enter_path}/{today}",filename)
    print(file_path)
    # try:
    #     if(os.path.isfile(file_path)):
    #         os.remove(file_path)
    # except OSError as error:
    #     print(error)
    print(os.path.basename(filename))    
