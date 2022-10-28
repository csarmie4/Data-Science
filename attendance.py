import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file = "attendance.txt"
data = np.loadtxt(file, dtype=str)

data = pd.DataFrame(data, columns = ["names"])
attendance = {"Arden": 0, "Stella": 0, "Arianna": 0, "Shalini": 0, "Ruby": 0, "Elle": 0, "Amelia": 0, "Sadie": 0, "Jessica": 0, "Katie": 0, "Violet": 0, "Mina": 0}


def attendance_count(data):
    """Return a dictionary with counts of 
    occurrences as value for each key."""
    miss_name = []

    for entry in data:
        if entry in attendance.keys():
            attendance[entry] += 1
        
        else:
            miss_name.append(entry)
            print(miss_name)
    
    return attendance

count_entries = attendance_count(data["names"])
print(count_entries)

fig, ax = plt.subplots()
x, y = zip(*sorted(attendance.items()))
ax.bar(x, y)
ax.set_xticklabels(x, rotation=90)
plt.show()
