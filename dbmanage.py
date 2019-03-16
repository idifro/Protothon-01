import tkinter as tk
import csv
import uuid
from datetime import datetime


r = tk.Tk()
r.title('Registration Database')
r.geometry("500x500")
tk.Label(r, text='Enter Name').grid(row=0,column=0)
tk.Label(r, text='Enter Mobile number').grid(row=1,column=0)
tk.Label(r, text='Enter Email').grid(row=2,column=0)
tk.Label(r, text='Enter Institution').grid(row=3,column=0)
tk.Label(r, text='Search column').grid(row=5,column=0)
tk.Label(r, text = 'Enter name to search').grid(row=6,column=0)


name = tk.Entry(r) 
mobileno = tk.Entry(r)
email = tk.Entry(r)
insti = tk.Entry(r)
search = tk.Entry(r)


name.grid(row=0, column=1) 
mobileno.grid(row=1, column=1)
email.grid(row=2, column=1)
insti.grid(row=3, column=1)
search.grid(row=6, column=1)





def writecsv():
    global name,mobileno,email,insti,a
    n=name.get()
    m=mobileno.get()
    e=email.get()
    i=insti.get()
    a = uuid.uuid4().hex
    now = datetime.now()
    ts = datetime.timestamp(now)
    
    with open('C:\\Users\\Harshavardhan\\Desktop\\Protothon SW\\RegDatabase.csv', 'w', newline='') as f:
        w=csv.writer(f, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        w.writerow([n,m,e,i,ts,a])
        
def readcsv():
    rows=[]
    names=[]

    
    
    with open('C:\\Users\\Harshavardhan\\Desktop\\Protothon SW\\RegDatabase.csv') as csv_file:
        s=search.get()
        csv_reader = csv.reader(csv_file, delimiter=',',quoting = csv.QUOTE_ALL)
        for row in csv_reader:
            names.append(row[0])
        i=0
        length = len(names)
        print(length)
        while i<length:
            if(s == names[i]):
                index1 = i
                break
            else:
                i=i+1
    
    csv_file.close()
    
    tk.Label(r, text='Name').grid(row=8,column=0)
    tk.Label(r, text='Mobile number').grid(row=9,column=0)
    tk.Label(r, text='Email').grid(row=10,column=0)
    tk.Label(r, text='Institution').grid(row=11,column=0)
    tk.Label(r, text='TimeStamp').grid(row=12,column=0)
    tk.Label(r, text='UUID No').grid(row=13,column=0)

    with open('C:\\Users\\Harshavardhan\\Desktop\\Protothon SW\\RegDatabase.csv') as csvfile:
        readCSV = list(csv.reader(csvfile, delimiter=','))
        row_you_want = readCSV[index1]
        row1=8
        for x in range(len(row_you_want)): 
            tk.Label(r,text=row_you_want[x]).grid(row=row1,column=1)
            row1 = row1+1
            print("\n")
    
    
    
    
write = tk.Button(r, text='Submit', command=writecsv)
write.grid(row=4,column=1)

read = tk.Button(r, text='Search', command=readcsv)
read.grid(row=7,column=1)




r.mainloop()