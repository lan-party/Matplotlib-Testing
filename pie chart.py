import matplotlib.pyplot as plt

slices = [3, 6, 9, 12, 15]
things = ['test1', 'test2', 'test3', 'test4', 'test5']
a = [1]*100
b = ["that's", "enough", "slices", ""]*25

plt.pie(slices, labels=things)
plt.pie(a, labels=b)
plt.savefig("pie chart.png")
