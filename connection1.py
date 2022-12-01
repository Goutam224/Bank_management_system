from types import NoneType
import mysql.connector as s
import datetime as t
sqlcon=s.connect(
        host="localhost",
        username="root",
        password="",
        database="bank")       


c=sqlcon.cursor(buffered=True)


def accountnone():
         query='select accountno from account where accountno=accountno'
         """c=sqlcon.cursor()"""
         c.execute(query)
         myresult=c.fetchone()
         if (myresult is None):
         # print("-----Sorry😔 You Don't Have Any Data In Your Database Please Create An Account-----")
          createAccount()
         else :
          checkaccount()          


def checkaccount():
         query='select accountno from account where accountno=accountno'
         """c=sqlcon.cursor()"""
         c.execute(query)
         myresult=c.fetchone()
         r=int(myresult[0])
         acn=int(input("Enter Account Number For Verification :"))
         if (r==acn):
          print("-----Sorry This Account Number Is Already Exist Try Using Different Account Number-----")
          main()
         else:
          createAccount()        


def createAccount():
          accountno= input("Enter the Account Number : ")
          name= input("Enter The Account Holder Name : ")
          gender=input("Enter Gender : ")
          dob= input("Enter the Date Of Birth(YYYY-MM-DD): ")
          address=input("Enter Your City:")
          openbal=int(input("Enter Opening Balance:"))
          data1=(accountno,name,gender,dob,address,openbal)
          data2=(accountno,name,openbal)
          sql1='insert into account values(%s,%s,%s,%s,%s,%s)'
          sql2='insert into amount values(%s,%s,%s)'
          """c=sqlcon.cursor()"""
          c.execute(sql1,data1)
          c.execute(sql2,data2)
          sqlcon.commit()
          print()
          print("-----Account Successfully Created-----")
          print()
          print("Your Account Number Is:",accountno)
          print()
          main()


def checknonedeposit():
         query='select accountno from account where accountno=accountno'
         """c=sqlcon.cursor()"""
         c.execute(query)
         myresult=c.fetchone()
         if (myresult is None):
          print("-----Sorry😔 You Don't Have Any Data In Your Database Please Create An Account-----")
          main()
         else :
          checkdeposit()  


def checkdeposit():
         query='select accountno from account where accountno=accountno'
         """c=sqlcon.cursor()"""
         c.execute(query)
         myresult=c.fetchone()
         r=int(myresult[0])
         acn=int(input("Enter Account Number For Verification :"))
         if (r==acn):
          depositamount()
         else:
          print("-----Sorry This Account Number Is Not Exist Try Using Different Account Number-----")
          main()


def depositamount():
        amount=int(input("Enter The Amount That You Want To Deposit:"))
        accountno=input("Enter The Account Number :")
        query='select balance from amount where accountno=%s'
        data=(accountno,)
        """c=sqlcon.cursor()"""
        c.execute(query,data)
        myresult=c.fetchone()
        temp=myresult[0]+amount
        sql='update amount set balance=%s where accountno=%s'
        d=(temp,accountno)
        c.execute(sql,d)
        sqlcon.commit()
        print("-----Amount Is Deposited Successfully On-----",t.datetime.now())
        print()
        main()


def checknonewithdraw():
         query='select accountno from account where accountno=accountno'
         """c=sqlcon.cursor()"""
         c.execute(query)
         myresult=c.fetchone()
         if (myresult is None):
          print("-----Sorry😔 You Don't Have Any Data In Your Database Please Create An Account-----")
          main()
         else :
          checkwithdraw()


def checkwithdraw():
         query='select accountno from account where accountno=accountno'
         """c=sqlcon.cursor()"""
         c.execute(query)
         myresult=c.fetchone()
         r=int(myresult[0])
         acn=int(input("Enter Account Number For Verification :"))
         if (r==acn):
          withdrawamount()
         else:
          print("-----Sorry This Account Number Is Not Exist Try Using Different Account Number-----")
          main()


def withdrawamount():
    amount=int(input("Enter The Amount That You Want To Withdraw:"))
    accountno=input("Enter The Account Number:")
    query='select balance from amount  where accountno=%s'
    data=(accountno,)
    """c=sqlcon.cursor()"""
    c.execute(query,data)
    myresult=c.fetchone()
    r=(myresult[0])
    if (r>=amount):
     temp=myresult[0]-amount
     sql='update amount set balance=%s where accountno=%s'
     d=(temp,accountno)
     c.execute(sql,d)
     sqlcon.commit()
     print("-----Your Withdraw Is Successful----- ")
     main()
    else:
        print("-----You Have Insufficient Balance In Your Account-----")
    print()   


def checknonebalance():
         query='select accountno from account where accountno=accountno'
         """c=sqlcon.cursor()"""
         c.execute(query)
         myresult=c.fetchone()
         if (myresult is None):
          print("-----Sorry😔 You Don't Have Any Data In Your Database Please Create An Account-----")
          main()
         else :
          checkbalance()


def checkbalance():
         query='select accountno from account where accountno=accountno'
         """c=sqlcon.cursor()"""
         c.execute(query)
         myresult=c.fetchone()
         r=int(myresult[0])
         acn=int(input("Enter Account Number For Verification :"))
         if (r==acn):
          balance()
         else:
          print("-----Sorry This Account Number Is Not Exist Try Using Different Account Number-----")
          main()


def balance():
    accountno=input("Enter The Account Number :")
    query='select balance from amount where accountno=%s'
    data=(accountno,)
    """c=sqlcon.cursor()"""
    c.execute(query,data)
    myresult=c.fetchone()
    print("Balance For Account Number.",accountno,"Is:",myresult[0])
    main()


def checknonedetail():
         query='select accountno from account where accountno=accountno'
         """c=sqlcon.cursor()"""
         c.execute(query)
         myresult=c.fetchone()
         if (myresult is None):
          print("-----Sorry😔 You Don't Have Any Data In Your Database Please Create An Account-----")
          main()
         else :
          checkdetail()


def checkdetail():
         query='select accountno from account where accountno=accountno'
         """c=sqlcon.cursor()"""
         c.execute(query)
         myresult=c.fetchone()
         r=int(myresult[0])
         acn=int(input("Enter Account Number For Verification :"))
         if (r==acn):
          displaydetail()
         else:
          print("-----Sorry This Account Number Is Not Exist Try Using Different Account Number-----")
          main()


def displaydetail():
    accountno=input("Enter Account Number :")
    query='select * from account where accountno=%s'
    data=(accountno,)
    """c=sqlcon.cursor()"""
    c.execute(query,data)
    myresult=c.fetchone()
    query1='select balance from amount where accountno=%s'
    data1=(accountno,)
    c.execute(query1,data1)
    result=c.fetchone()
    r=int(result[0])
    print("Total Balance In Your Account Is :",r)
    print()
    print("AccountNO.  Name        Gender           DOB              City        OpeningBal     Account Opening Date")
    for i in myresult:
        print(i,end="         ")
    print()
    main()


def closenone():
         query='select accountno from account where accountno=accountno'
         """c=sqlcon.cursor()"""
         c.execute(query)
         myresult=c.fetchone()
         if myresult is None:
            print("-----Sorry😔 You Don't Have Any Data In Your Database Please Create An Account-----")
            main()
         else:
            checkcloseaccount()


def checkcloseaccount():
         query='select accountno from account where accountno=accountno'
         """c=sqlcon.cursor()"""
         c.execute(query)
         myresult=c.fetchone()
         r=int(myresult[0])
         acn=int(input("Enter Account Number That You Want To Delete :"))
         if (acn==r):
            closeaccount()
         else:
            print("-----Sorry This Account Number Is Not Exist Try Using Different Account Number-----")
            main()


def closeaccount():
    accountno=input("Enter Account Number:")
    query1='delete from account where accountno=%s'
    query2='delete from amount where accountno=%s'
    data=(accountno,)
    """c=sqlcon.cursor()"""
    c.execute(query1,data)  
    c.execute(query2,data)  
    sqlcon.commit()
    print("Account Closed Successfully")
    print()
    main()


def main():
    print("\t     -----😊🏦WELCOME TO THE DEMO BANK🏦😊-----")
    print("""\n    \t     1. OPEN NEW ACCOUNT
             2. DEPOSIT AMOUNT
             3. WITHDRAW AMOUNT
             4. BALANCE INQUIRY
             5. DISPLAY CUSTOMER DETAILS
             6. CLOSE AN ACCOUNT""")
    ch=input("Enter Choice between 1-6 :")
    while True:
     if (ch == '1'):
        accountnone()
     elif (ch =='2'):
        checknonedeposit()
     elif (ch=='3'):
        checknonewithdraw()
     elif (ch == '4'):
        checknonebalance()
     elif (ch=='5'):
        checknonedetail()
     elif (ch=='6'):
        closenone()
     else :
         print("Invalid Choice")
         main()
main()
    
     