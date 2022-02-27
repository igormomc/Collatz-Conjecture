import matplotlib.pyplot as plt
import numpy as np;

np.random.seed(2)

tall = int(input("Give me a number: "))
print(tall)
x = []
y = []
counter = 1

x.append(tall)
y.append(counter)
while tall != 1:
    if (tall % 2 == 0):
        tall = tall // 2
        counter += 1
        y.append(counter)
        print(tall)
    elif (tall % 2 != 0):
        tall = tall * 3 + 1
        counter += 1
        y.append(counter)
        print(tall)
    x.append(tall)

print("steps to 1: " + str(counter))


def animate_plot_with_lines():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_ylim([0, max(y)])
    ax.set_xlim([0, max(x)])
    ax.set_xlabel('Number')
    ax.set_ylabel('Steps')
    ax.set_title('Collatz')
    if counter > 30:
        line, = ax.plot(x, y, 'r-')
    else:
        line, = ax.plot(x, y, 'bo-')
    for i in range(len(x)):
        line.set_xdata(x[:i])
        line.set_ydata(y[:i])
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.pause(0.1)
    plt.show()


animate_plot_with_lines()
