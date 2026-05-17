
# file = open("file.txt", "w")
# try:
#     file.write("Hey This is file")
# finally:
#     file.close()

# another way of writing to file "with"

with open("file.txt", "w") as file:
    file.write("Hey I am writing this file using 'with'")

with open("file.txt", "r") as readFile: # behind the seen __enter__() and __exit__() these two call itself
    file.read()


