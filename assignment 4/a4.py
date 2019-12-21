import os
import csv
current_dir = os.path.dirname(__file__)
# csv file name
filename = "a4.csv"

# writing to csv file
with open(os.path.join(current_dir, filename), 'a') as csvfile:
    # creating a csv writer object
    fdnames=['phone no','email add','home add']
    writer=csv.writer(csvfile,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(fdnames)

def getdetails():
    n=int(input("enter no. : "))
    email=input("email id : ")
    add=input("address: ")
    mydict=[n,email,add]
    with open(os.path.join(current_dir, filename),'a')as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(mydict)
def search():
    print("1.phone no 2. email id 3. address")
    ch=int(input("enter choice : "))
    with open(os.path.join(current_dir, filename),'r')as csvfile :
        reader=csv.reader(csvfile)
        if ch == 1:
             no=input("enter:")
             line=0
             for row in reader:
                  if line!=0:
                      if line%2==0:
                            if row[0]==no:
                                print({row[1]})
                                print({row[2]})
                  line+=1
        elif ch==2:
            email=input("enter:")
            line=0
            for row in reader:
                if line!=0:
                    if line%2==0:
                        if row[1]==email:
                            print({row[0]})
                            print({row[2]})
                line+=1
        elif ch==3:
            add=input("enter:")
            line=0
            for row in reader:
                if line!=0:
                    if line%2==0:
                        if row[2]==add:
                            print({row[0]})
                            print({row[1]})
                line+=1


ch=0
while ch!=3:
    print( "1. add contact\n2.search contact\n3.exit")
    ch=int(input("enter choice "))
    if ch==1 :
        getdetails()
        print("done")
    elif ch==2:
        search()