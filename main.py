# 1
counter = 0

def increment_counter():
    global counter
    counter += 1
    print(f"Increment value: {counter}")

def reset_counter():
    global counter
    counter = 0
    print(f"Reset value: {counter}")

increment_counter()
increment_counter()
increment_counter()

reset_counter()

print(f"Global value: {counter}")

# 2
import os

print("Directory: ", os.getcwd())
print("List of files and directories: ", os.listdir())

os.mkdir("test_dir")
print("New directory created")

os.chdir("test_dir")
print("New working directory: ", os.getcwd())

with open("test_file.txt", "w") as file:
    file.write("This is a test file.")

print("A file created.")

os.remove("test_file.txt")
print("File deleted.")

os.chdir("..")
os.rmdir("test_dir")
print("Directory deleted.")

# 3

def divide_num(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    else:
        return result
    finally:
        print("Operation completed")

a = float(input("Enter a number: "))
b = float(input("Enter another number: "))

result = divide_num(a, b)
if result is not None:
    print(f"Result: {result}")