import matplotlib.pyplot as plt

def generate_pie_charts():
    labels = ['a','b','c']
    values = [14,15,16]
    
    fig, ax= plt.subplots()
    ax.pie(values, labels = labels)
    plt.savefig("py.png")
    plt.close()