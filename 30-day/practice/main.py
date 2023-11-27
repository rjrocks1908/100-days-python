try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not found")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")

# raise a exception
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be greater than 3 meters")

bmi = height / height ** 2
print(bmi)