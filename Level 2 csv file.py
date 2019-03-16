import csv
import random 
import os 

def filename(val):
    x="file_"+str(val)+".csv"
    val=val+1
    return x

def create(path):
    rows=["#","Num1","Num2","Num3","Num4","Num5"]
    with open(path, 'w' ) as myfile:
         wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
         wr.writerow(rows)
def add(path,val):
    with open(path, 'a' ) as myfile:
         wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
         wr.writerow(rand(val))

def rand(val):
    l=random.sample(range(1, 100), 4)
    l.insert(0,val)
    return l

def file_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return file_info.st_size
    

def main():
    i=0
    while(1):
        path="C:\\Users\\Forge\\Desktop\\Round2\\"+filename(i)
        create(path)
        j=0
        while(file_size(path) <2000):
            j=j+1
            add(path,j)
        i+=1
        path="C:\\Users\\Forge\\Desktop\\Round2\\"+filename(i)
        print("file 1 created")
    
if __name__ == "__main__":
    main()
