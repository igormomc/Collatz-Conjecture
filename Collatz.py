import matplotlib.pyplot as plt
import numpy as np; np.random.seed(2)

def MakeGraph():
    tall = int(input("Give me a number: "))
    print(tall)
    x = []
    y = []
    counter = 1

    x.append(tall)
    y.append(counter)
    while tall != 1:
        if(tall %2 == 0):
            tall = tall // 2
            counter+=1
            y.append(counter)
            print(tall)
        elif(tall %2 != 0):
            tall = tall * 3 + 1
            counter+=1
            y.append(counter)
            print(tall)
        x.append(tall)


    print("steps to took to find 1: " + str(counter) + " Steps")

    
    plt.plot(y, x,color='red', linestyle='dashed', linewidth = 1,
            marker='o', markerfacecolor='blue', markersize=7)
            
            
    
    # setting x and y axis range
    plt.ylim(1,max(x) + 5)
    plt.xlim(1,counter + 5)
    
    # naming the x axis
    plt.xlabel('Steps')
    # naming the y axis
    plt.ylabel('Number Value')
    
    # giving a title to my graph
    plt.title('Collatz Conjecture')
    
    # function to show the plot
    plt.show()
    return
    
MakeGraph()