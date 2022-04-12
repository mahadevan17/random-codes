import matplotlib.pyplot as plt
import mysql.connector as mys
mycon=mys.connect(host="localhost",user="root",password="admin",database="expenditure")
if mycon.is_connected()==True:
    print("success")
else:
    print("problem occured") 
cn=mycon.cursor()
def insert():
    s="expenses_"
    month=input("enter the month(expenses_monthYYYY): ")
    year=input("enter the year: ")
    table=s+month+year
    date=int(input("enter the date: "))
    money_spent=int(input("enter the amount: "))
    cn.execute('insert into {0} values({1},{2})'.format(table,date,money_spent))
    mycon.commit()
def plot():
    x=[]
    y=[]
    s="expenses_"
    month=input("enter the month(expenses_monthYYYY): ")
    year=input("enter the year: ")
    table=s+month+year
    cn.execute("select * from {0}".format(table,))
    results=cn.fetchall()
    print("date","money_spent")
    for i in results:
        print(i[0],i[1])        
        x.append(i[0])
        y.append(i[1])
    plt.plot(x,y,label='first line')
    plt.xlabel("date")
    plt.ylabel("money spent(each day)")
    plt.show()
while True:
    print("1)insert new date ")
    print("2)plot the graph ")
    n=int(input("enter the choice "))
    if n==1:
        insert()
        print("successfully done")
    elif n==2:
        plot()
    else:
        break
