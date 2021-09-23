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

x = [1,2,3,4,5]
y1 = f(x)
y2 = f2(x)


plt.plot(x,y1, label='One')
plt.plot(x,y2, label='Two')
plt.xlabel('Plot Number')
plt.ylabel('Var')
plt.title('Hi there')
plt.legend()

plt.savefig("legends titles and labels.png")
