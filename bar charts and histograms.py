import matplotlib.pyplot as plt

def f(x):
    r = []
    for x_num in x:
        r += [2 ** x_num]
    return r
def f2(x):
    r = []
    for x_num in x:
        r += [-(2 ** x_num)]
    return r

x1 = [1,3,5,7,9]
x2 = [2,4,6,8,10]
y1 = f(x1)
y2 = f(x2)


plt.bar(x1,y1, label='One', color='#ff0000')
plt.bar(x2,y2, label='Two', color='#0000ff')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Hi there')
plt.legend()

plt.savefig("bar charts and histograms1.png")


population_ages = [19, 23, 60, 74, 50, 5, 9, 13, 90, 88, 12]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
plt.savefig("bar charts and histograms2.png")
