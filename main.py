import os

print("Current Working Directory:", os.getcwd())

print(os.listdir())





print(os.listdir())


print(os.chdir("demo_dir"))


print("Changed Working Directory:", os.getcwd())


print(os.listdir())


with open("example.txt", "w") as file:
    file.write("Hello, World!")

print(os.listdir())


print(os.chdir(".."))
print("Reverted Working Directory:", os.getcwd())

print(os.listdir())



print(os.chdir("demo_dir"))

print("Changed Working Directory Again:", os.getcwd())

print(os.listdir())