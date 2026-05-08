 5/1:
count = 10
while count > 0:
    print(count)
    count -= 1
 6/1:
%timeit [x**2 for x in range(1000)]
%timeit (x**2 for x in range(1000))

a = 10
b = [1, 2, 3]
c = "hello"
%whos

%%html
<h1 style="color:blue; text-align:center;">
    My Python Notebook 🚀
</h1>
<p style="text-align:center;">
    Welcome to my project!
</p>
 6/2:
%timeit [x**2 for x in range(1000)]
%timeit (x**2 for x in range(1000))

a = 10
b = [1, 2, 3]
c = "hello"
%whos

%%html
<h1 style="color:blue; text-align:center;">
    My Python Notebook
</h1>
<p style="text-align:center;">
    Welcome to my project!
</p>
 6/3:
%timeit [x**2 for x in range(1000)]
%timeit (x**2 for x in range(1000))

a = 10
b = [1, 2, 3]
c = "hello"
%whos

%%html
<h1 style="color:blue; text-align:center;">
    My Python Notebook 🚀
</h1>
<p style="text-align:center;">
    Welcome to my project!
</p>
 6/4:
%timeit [x**2 for x in range(1000)]
%timeit (x**2 for x in range(1000))

a = 10
b = [1, 2, 3]
c = "hello"
%whos

%%html
<h1 style="color:blue; text-align:center;">
    My Python Notebook
</h1>
<p style="text-align:center;">
    Welcome to my project!
</p>
 6/5:
%timeit [x**2 for x in range(1000)]
%timeit (x**2 for x in range(1000))

a = 10
b = [1, 2, 3]
c = "hello"
%whos

%%html
<h1 style="color:blue; text-align:center;">
    My Python Notebook
</h1>
<p style="text-align:center;">
    Welcome to my project!
</p>
 6/6:
%timeit [x**2 for x in range(1000)]
%timeit (x**2 for x in range(1000))

a = 10
b = [1, 2, 3]
c = "hello"
%whos

%%html
<h1 style="color:blue; text-align:center;">
    My Python Notebook
</h1>
 6/7:
%timeit [x**2 for x in range(1000)]
%timeit (x**2 for x in range(1000))

a = 10
b = [1, 2, 3]
c = "hello"
%whos

%%html
<h1 style="color:blue">My Python Notebook</h1>
 6/8:
%timeit [x**2 for x in range(1000)]
%timeit (x**2 for x in range(1000))

a = 10
b = [1, 2, 3]
c = "hello"
%whos

%%html
<h1 style="color:maroon">My Python Notebook</h1>
 6/9:
%timeit [x**2 for x in range(1000)]
%timeit (x**2 for x in range(1000))

a = 10
b = [1, 2, 3]
c = "hello"
%whos

%%html
<h1>My Python Notebook</h1>
 7/1:
numbers = [2,4,6]
cubes = [n**3 for n in numbers]
cubes
 8/1:
variables = [
    ("Movie Genre", "Nominal"),
    ("Exam Letter Grade", "Ordinal"),
    ("Temperature in Celsius", "Interval"),
    ("Height in cm", "Ratio"),
    ("Number of Siblings", "Ratio")
]

for var, classification in variables:
    print(f"{var} → {classification}")
 9/1:
%cd ../
%pwd
 9/2:
%cd ../
%ls
 9/3:
with open('me.txt', 'w') as f:
    f.write("Name: Bryce Koch\n")
with open('me.txt', 'r') as f:
    print(f.read())
 9/4:
my_dict = {"name": "Bryce Koch", "favorite_courses": ['Calculus 3','OOP','Algorithms']}
with open("courses.json", "w") as f:
    json.dump(my_dict, f)
with open("courses.json", "r") as f:
    loaded_dict = json.load(f)
loaded_dict
 9/5:
import json
my_dict = {"name": "Bryce Koch", "favorite_courses": ['Calculus 3','OOP','Algorithms']}
with open("courses.json", "w") as f:
    json.dump(my_dict, f)
with open("courses.json", "r") as f:
    loaded_dict = json.load(f)
loaded_dict
 9/6:
rows = [["Name", "Bryce"], ["Age", 23], ["Class", 'Spatial Data and Mapping']]
with open("info.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
with open("info.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
 9/7:
import csv
rows = [["Name", "Bryce"], ["Age", 23], ["Class", 'Spatial Data and Mapping']]
with open("info.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
with open("info.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
10/1:
df = pd.read_csv("info.csv")
df
10/2:
import pandas as pd
df = pd.read_csv("info.csv")
df
10/3:
import pandas as pd
df = pd.read_csv("info.csv")
df
10/4:
import pandas as pd

data = """Name,Age,Score
Alice,23,90
Bob,25,85
Charlie,22,95
"""
with open("students.csv", "w") as f:
    f.write(data)

df = pd.read_csv("students.csv")
df
10/5: df.head()
10/6:
df.to_csv("students_copy.csv", index=False)
%ls *.csv
10/7:
df.to_excel("students.xlsx", index=False)

# Read Excel file
pd.read_excel("students.xlsx")
10/8:
df.to_excel("students.xlsx", index=False)

pd.read_excel("students.xlsx")
11/1:
y = np.cos(x)

plt.plot(x, y,color='red', label="cos(x)")
plt.title("Line Plot Example")
plt.xlabel("x")
plt.ylabel("cos(x)")
plt.legend()
plt.show()
11/2:
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
11/3:
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
11/4:
y = np.cos(x)

plt.plot(x, y,color='red', label="cos(x)")
plt.title("Line Plot Example")
plt.xlabel("x")
plt.ylabel("cos(x)")
plt.legend()
plt.show()
11/5:
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, label="sin(x)")
plt.title("Line Plot Example")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
plt.show()
11/6:
y = np.cos(x)

plt.plot(x, y,color='red', label="cos(x)")
plt.title("Line Plot Example")
plt.xlabel("x")
plt.ylabel("cos(x)")
plt.legend()
plt.show()
11/7:
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)

plt.scatter(x, y, c=colors, alpha=0.6, cmap='viridis')
plt.title("Scatter Plot Example")
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar(label="color scale")
plt.show()
11/8:
categories = ["A", "B", "C", "D"]
values = [5, 7, 3, 8]

plt.bar(categories, values)
plt.title("Bar Plot Example")
plt.xlabel("Category")
plt.ylabel("Value")
plt.show()
11/9:
categories = ["Reading", "Gaming", "Cooking", "Sports"]
values = [5, 7, 3, 8]

plt.bar(categories, values)
plt.title("Bar Plot Example")
plt.xlabel("Category")
plt.ylabel("Value")
plt.show()
11/10:
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin(x)", linestyle="--", color="blue")
plt.plot(x, y2, label="cos(x)", linestyle=":", color="red")
plt.title("Customized Line Plot")
plt.xlabel("x (radians)")
plt.ylabel("value")
plt.legend()
plt.grid(True)
plt.show()
11/11:
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin(x)", linestyle="--", color="blue", linewidth=2)
plt.plot(x, y2, label="cos(x)", linestyle=":", color="red", linewidth=2)
plt.title("Customized Line Plot")
plt.xlabel("x (radians)")
plt.ylabel("value")
plt.legend()
plt.grid(True)
plt.show()
11/12:
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin(x)", linestyle="--", color="blue", linewidth=2)
plt.plot(x, y2, label="cos(x)", linestyle=":", color="red", linewidth=2)
plt.title("Customized Line Plot")
plt.xlabel("x-value")
plt.ylabel("y-value")
plt.legend()
plt.grid(True)
plt.show()
