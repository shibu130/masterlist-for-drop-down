import mysql.connector
with open("visa.txt","r") as  f :


    line=f.readlines()

stack=[]
dictionary={}
values=[]
j=1



for i in line:
    if j==1:
        dictionary[i.strip()]=[]
        j=j+1
        print("first standalone")
    elif '{' in i:
        print("opening")
        stack.append('{')
    elif '}' in i:
        print("closing")
        stack=[]
    else:
        if '{' in stack:
            a=list(dictionary.keys())[-1]
            values.append(i.strip())
            dictionary[a]=values
        else:
            print("standalone")
            values=[]
            dictionary[i.strip()]=[]
        

#change the values below
mydb = mysql.connector.connect(
  host="localhost",
  user="your_username",
  passwd="your_password",
  database="your_database"
)
mycursor=mydb.cursor()
           
    #table creation 

mycursor.execute("CREATE TABLE visatypes ( id int NOT NULL AUTO_INCREMENT ,country VARCHAR(20), visa VARCHAR(20)),PRIMARY KEY (id)")

#print(dictionary)
#count=0
for f,g in dictionary.items():
  #  print(f)
    for u in g:
       # print(u)
        sql = "INSERT INTO visatypes (country,visa) VALUES (%s, %s)"
        val = (f,u)
        mycursor.execute(sql, val)
     #   count=count+1
        mydb.commit()



