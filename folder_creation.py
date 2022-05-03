import os
from datetime import date

parent_dir = os.path.dirname(os.path.abspath(__file__))

print(os.path.abspath(__file__), type(os.path.abspath(__file__)))
print(parent_dir, type(parent_dir))


def create_folder_files():
    # Returns the current local date
    today = date.today()
    print(today)
    today_format = today.strftime("%d-") + today.strftime("%b-") + today.strftime("%Y")
    print(today_format)
    folder_name = str(today_format)
    print(folder_name)
    path = os.path.join(parent_dir,folder_name)

    print(path)
    isdir = os.path.isdir(path)
    print(isdir)

    k = 1
    while(isdir):
        temp = path
        temp += str("_"+str(k))
        k += 1
        isdir = os.path.isdir(temp)
        if isdir == False:
            path = temp

    os.mkdir(path)

    # Create BTEQ folder:
    path_bteq = os.path.join(path,"Sample")
    os.mkdir(path_bteq)

    # Create deploy.conf
    deploy_path = os.path.join(path,"xyz.txt")
    with open(deploy_path,'w') as fp:
        x = """Sample/xyz.txt"""
        fp.write(x)
    
    # Create file inside Bteq folder
    # query_txt_path = os.path.join(path_bteq,"script.txt")
    # with open(query_txt_path, 'w') as fp:
    #     pass

if __name__ == '__main__':
    create_folder_files()


