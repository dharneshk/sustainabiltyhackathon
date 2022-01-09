import matplotlib.pyplot as plt
import csv
import numpy as p



f = open("BO5341_IoTData.csv", 'r')
variable = f.readline()
print(variable)
x = variable.split(", ")
#print(x)
y=range(0,9999999)
with open('BO5341_IoTData.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    #for row in plots:
        #x.append(row[0])
        #y.append(int(row[2]))
xpoints = p.array(x)
ypoints = p.array(y)
plt.bar(x, y, color = 'g', width = 0.72)
plt.plot(xpoints, ypoints)
plt.show()
plt.xlabel('Carteria')
plt.ylabel('Energy')
plt.title('IoT Data visualisation')
plt.legend()
plt.show()
