# fileStore=open("ayush.txt","r")  # open readonly mode
# fileContent=fileStore.read()  # i am reading
# print(fileContent)

# f=open("ayush.txt","w")

# f.write(" Ayush is smart boy345")
# f.seek(0)
# content=f.read()
# print(content)

# content=f.readline()
# print(content)
# content=f.readline()
# print(content)
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

# f = open('myfile.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()

with open("data.txt","r+") as f:
    # f.seek(5)
    f.truncate(8)
    content=f.readline()
    print(content)
