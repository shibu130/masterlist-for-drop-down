import mysql.connector

with open("education.txt", "r") as f:

    line = f.readlines()

stack = []
dictionary = {}
values = []
j = 1


for i in line:
    if j == 1:
        dictionary[i.strip()] = []
        j = j + 1
        print("first standalone")
    elif "{" in i:
        print("opening")
        stack.append("{")
    elif "}" in i:
        print("closing")
        stack = []
    else:
        if "{" in stack:
            a = list(dictionary.keys())[-1]
            values.append(i.strip())
            dictionary[a] = values
        else:
            print("standalone")
            values = []
            dictionary[i.strip()] = []


mydb = mysql.connector.connect(
    host="localhost", user="imrankhan", passwd="imukhan@25", database="user"
)
mycursor = mydb.cursor()

# id              | bigint(20)   | NO   | PRI | NULL    | auto_increment |
# | course_category | varchar(255) | YES  |     | NULL    |                |
# | course_type


# print(dictionary)
# count=0
for f, g in dictionary.items():
    #  print(f)
    for u in g:
        # print(u)
        sql = "INSERT INTO educationlist (course_category,course_type) VALUES (%s, %s)"
        val = (f, u)
        mycursor.execute(sql, val)
        #   count=count+1
        mydb.commit()
        print("inserted row {0}".format(mycursor.lastrowid))


# print(count)


# mydb = mysql.connector.connect(
#   host="localhost",
#   user="imrankhan",
#   passwd="imukhan@25",
#   database="user"
# )


# cursor=mydb.cursor()


# print(dictionary.keys())

# d={"one":"","two":""}

# a=list(d.keys())[-1]
# print(a)
