import matplotlib.pyplot as plt

x =[1,2,3,4]
y =[1500,1200,1100,1800]

#plt.plot(x,y) #em linhas
#plt.show()
legend= ["janeiro", "fevereiro", "março", "abril"]
##plt.xticks(x,legend)
#plt.plot(x,y)
#plt.show()
plt.bar(x,y)
plt.ylabel("sales in us$")
plt.title("monthly.sales")
plt.show()

