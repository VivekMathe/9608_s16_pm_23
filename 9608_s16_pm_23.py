#Task 1
f_name = input("First Name : ")
s_name = input("Second Name : ")

print(f_name + " " + s_name)
print(f_name[:1] + " " + s_name)
print(s_name + ", " + f_name)
print("Mr " + f_name[:1] + " " + s_name)
print("Dear Mr " + s_name)
print("First Name: " + f_name + ", Second Name: " + s_name)
print(f_name + " " + s_name.upper())

#Task 2
def ValidateUserID(id):
    id_l = id[:3].lower()
    if id_l.islower() == True:
        return True
    else:
        return False

#Task 3
f = open("membership.txt", "w")
a = int(input("How many memebers are there? : "))
for x in range(a):
    
    id = input("Enter the members ID : ")
    while ValidateUserID(id) == False:
        print("\nInvalid Format")
        id = input("Enter the members ID : ")

    f.write(id + "\n")

    name = input("Enter the members name : ")
    f.write(name + "\n")
    
f.close()
f = open("membership.txt", "r")
i = 0
data = [line[:-1] for line in f]
f.close()
rows = int(len(data) / 2)

print("ID        Name")
for x in range(rows):

    print(data[i], end = "    ")
    i += 1
    print(data[i])
    i += 1

id = []
name = []

for x in range(len(data)):
    if (x % 2) == 0:
        id.append(x)
    
    else:
        name.append(x)

search = input("Enter the name of the searched user : ")
for x in range(len(name)):
    if search.lower() == name[x].lower():
        print(id[x])

    elif (x == (len(name) - 1) and search.lower() != name[x].lower()):
        print("User Not Found")


ap = int(input("How many members would you like to add"))
f = open("membership.txt", "a")

for x in range(ap):
    id = input("Enter the members ID : ")
    while ValidateUserID(id) == False:
        print("\nInvalid Format")
        id = input("Enter the members ID : ")

    f.write(id + "\n")

    name = input("Enter the members name : ")
    f.write(name + "\n")

f.close()
f = open("membership.txt", "r")
data = [line[:-1] for line in f]
f.close()
users = int(len(data) / 2)
i = 0
f = open("membership_1.txt", "w")

print("The Club Now Needs to save additional information such as the telephone number and the membership start date for each user")
for x in range(users):

    f.write(data[i])
    i += 1

    f.write(data[i])
    i += 1
    
    b = input("Enter User " + str(x+1) + "'s Telephone Number : ")
    f.write(b + "\n")
    c = input("Enter User " + str(x+1) + "'s Membership Start Date : ")
    f.write(c + "\n")