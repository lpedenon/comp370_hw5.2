import matplotlib.pyplot as plt


plt.plot([1,2,3,4],[1,2,3,4])

plt.xlabel('X-axis Label') 
plt.ylabel('Y-axis Label') 
plt.title('My Matplotlib Plot')

plt.show()

plt.savefig('my_plot.png')   # save as an image file