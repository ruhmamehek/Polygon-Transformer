import math
import ast
import matplotlib.pyplot as plt

#Name: Ruhma Mehek Khan
#Roll Number: 2018362
#Group: 3
#Section: B
#HomeAssignment 3


def Translation(x,y):

	"""
	Translates every point by the given amount, as entered by the user, 
	using matrix for Linear Transformations.

	Arguments: Co-ordinates of the points that need to be translated
	Output: The co-ordinates of the point after translating them by the required amount

	"""

	Translating_Matrix=[[1,0,x1],[0,1,y1],[0,0,1]]
	Operating_matrix=[[x],[y],[1]]
	x_output=Translating_Matrix[0][0]*Operating_matrix[0][0]+Translating_Matrix[0][1]*Operating_matrix[1][0]+Translating_Matrix[0][2]*Operating_matrix[2][0]
	y_output=Translating_Matrix[1][0]*Operating_matrix[0][0]+Translating_Matrix[1][1]*Operating_matrix[1][0]+Translating_Matrix[1][2]*Operating_matrix[2][0]
	return x_output, y_output

def Scaling(x,y):

	"""
	Scales each point by the given amount, as entered by the user,
	using matrix for Linear Transformations.

	Arguments: Co-ordinates of the points that need to be scaled
	Output: The co-ordinates of the point after scaling them by the required amount
	
	"""

	Rotating_Matrix=[[s1,0,0],[0,s2,0],[0,0,1]]
	Operating_matrix=[[x],[y],[1]]
	x_output=Rotating_Matrix[0][0]*Operating_matrix[0][0]+Rotating_Matrix[0][1]*Operating_matrix[1][0]+Rotating_Matrix[0][2]*Operating_matrix[2][0]
	y_output=Rotating_Matrix[1][0]*Operating_matrix[0][0]+Rotating_Matrix[1][1]*Operating_matrix[1][0]+Rotating_Matrix[1][2]*Operating_matrix[2][0]
	return x_output, y_output

def Rotation(x,y):

	"""
	Rotates each point by the given angle, as entered by the user, about the origin,
	using matrix for Linear Transformations.

	Arguments: Co-ordinates of the points that need to be rotated about the origin
	Output: The co-ordinates of the point after rotating them by the required amount, about the origin
	
	"""

	Operating_matrix=[[x],[y],[1]]
	Rotating_Matrix=[[math.cos(theta), -math.sin(theta), 0],[math.sin(theta), math.cos(theta),0],[0,0,1]]
	x_output=Rotating_Matrix[0][0]*Operating_matrix[0][0]+Rotating_Matrix[0][1]*Operating_matrix[1][0]+Rotating_Matrix[0][2]*Operating_matrix[2][0]
	y_output=Rotating_Matrix[1][0]*Operating_matrix[0][0]+Rotating_Matrix[1][1]*Operating_matrix[1][0]+Rotating_Matrix[1][2]*Operating_matrix[2][0]
	return x_output, y_output

#_______________________________________________________________________________________________________________________________________

#Identifying the shape on which the linear transformations have to be applied

Shape=input("Enter shape name: ")
Shape=Shape.lower()

#_________________________________________FOR POLYGONS__________________________________________________________________________________

if Shape[0]=="p" :
	x_coordinates=ast.literal_eval(input("Enter x-coordinates as a list: "))
	y_coordinates=ast.literal_eval(input("Enter y-coordinates as a list: "))
	# takes the x and y-coordinates of the shape to be plotted from the user

	plt.ion() # makes the plot interactive
	plt.plot(x_coordinates+[x_coordinates[0]],y_coordinates+[y_coordinates[0]])
	plt.pause(.00001)
	plt.show()
	# plotting the initial shape

	order=input() # Takes the linear transformation to be applied from the user.
	while order!= "quit":

		#Translation
		if order[0]=="T":
			temp_x=[]
			temp_y=[]
			x1,y1=list(map(float, order[1:].split()))
			for i in range (len(x_coordinates)):
				x=x_coordinates[i]
				y=y_coordinates[i]
				outputs=Translation(x,y)
				temp_x.append(outputs[0])
				temp_y.append(outputs[1])
				# applying translation on each vertex about the origin and storing that in a list
			x_coordinates=temp_x
			y_coordinates=temp_y
			print("x_coordinates", x_coordinates)
			print("y_coordinates", y_coordinates)
			plt.ion() # makes the plot interactive
			plt.plot(x_coordinates+[x_coordinates[0]],y_coordinates+[y_coordinates[0]])
			plt.pause(.00001)
			plt.show()
			#plots the transformed polygon
		
		# Rotation	
		if order[0]=="R":
			temp_x=[]
			temp_y=[]
			i=order.split()
			theta=float(i[-1])
			theta=(theta/180)*3.14 # converts the angle into radians
			for i in range (len(x_coordinates)):
				x=x_coordinates[i]
				y=y_coordinates[i]
				outputs=Rotation(x,y)
				temp_x.append(outputs[0])
				temp_y.append(outputs[1])
				# applying rotation on each vertex about the origin and storing that in a list
			x_coordinates=temp_x
			y_coordinates=temp_y
			print("x_coordinates", x_coordinates)
			print("y_coordinates", y_coordinates)
			plt.ion() # makes the plot interactive
			plt.plot(x_coordinates+[x_coordinates[0]],y_coordinates+[y_coordinates[0]])
			plt.pause(.00001)
			plt.show()
			#plots the transformed polygon

		# Scaling
		if order[0]=="S":
			temp_x=[]
			temp_y=[]
			s1, s2= list(map(float, order[1:].split()))
			for i in range (len(x_coordinates)):
				x=x_coordinates[i]
				y=y_coordinates[i]
				outputs=Scaling(x,y)
				temp_x.append(outputs[0])
				temp_y.append(outputs[1])
				# Scaling each vertex about the origin and storing that in a list
			x_coordinates=temp_x
			y_coordinates=temp_y
			print("x_coordinates", x_coordinates)
			print("y_coordinates", y_coordinates)
			plt.ion() # makes the plot interactive
			plt.plot(x_coordinates+[x_coordinates[0]],y_coordinates+[y_coordinates[0]])
			plt.pause(.00001)
			#plots the transformed polygon

		order=input() # takes the input of the next transformation to be performed


#____________________________________________FOR DISC__________________________________________________________________________________

else:
	k=list(map(float, input("Enter disc attributes: ").split()))
	if len(k)==3:
		c1,c2,r=k[0],k[1], k[2] # stores the coordinates for center and the radius
		a=r 
		b=r
		# storing the major and minor axis, generalizing a circle into an ellipse
		o1y=c2
		o1x=c1+r
		o2y=c2+r
		o2x=c1
		# storing the coordinates of the end of major and minor axes
	if len(k)==4:
		c1,c2,a,b=k[0],k[1],k[2],k[3]
		o1x=c1+a
		o1y=c2
		o2y=c2+b
		o2x=c1


	x_coordinates=[]
	y_coordinates=[]
	i=0
	while i<4*3.14:
		x=a*math.cos(i)+c1
		y=b*math.sin(i)+c2
		x_coordinates.append(x)
		y_coordinates.append(y)
		i=i+0.01
		# converting the ellipse into its parametric form to get the coordinates of various points on it

	plt.ion() # makes the plot interactive
	plt.plot(x_coordinates[0:len(x_coordinates)//2],y_coordinates[0:len(y_coordinates)//2])
	plt.grid(color='lightgray',linestyle='--')
	plt.pause(0.0001)
	# plots the inputted circle


	order=input() # User prompt to get the required linear transformation

	while order!= "quit": # stop once the user enters the command quit
		if order[0]=="T": # Translation
			temp_x=[]
			temp_y=[]
			x1,y1=list(map(float, order[1:].split()))
			for i in range (len(x_coordinates)):
				x=x_coordinates[i]
				y=y_coordinates[i]
				outputs=Translation(x,y)
				temp_x.append(outputs[0])
				temp_y.append(outputs[1])
			x_coordinates=temp_x
			y_coordinates=temp_y
			centers=Translation(c1,c2) # Translating centers about the origin
			c1,c2=centers[0], centers[1]
			o1x,o1y=Translation(o1x,o1y)
			o2x,o2y=Translation(o2x,o2y)
			# applying translation on the end points of major and minor axes
			print("ellipse", c1, c2, a, b,)
			plt.ion() # makes the plot interactive
			plt.plot(x_coordinates+[x_coordinates[0]],y_coordinates+[y_coordinates[0]])
			plt.pause(.00001)
			# plots the transformed ellipse

		if order[0]=="S": #Scaling
			temp_x=[]
			temp_y=[]
			s1, s2= list(map(float, order[1:].split()))
			for i in range (len(x_coordinates)):
				x=x_coordinates[i]
				y=y_coordinates[i]
				outputs=Scaling(x,y)
				temp_x.append(outputs[0])
				temp_y.append(outputs[1])
			x_coordinates=temp_x
			y_coordinates=temp_y
			centers=Scaling(c1,c2) # Scaling centers about the origin
			c1,c2=centers[0], centers[1] 

			o1x,o1y=Scaling(o1x,o1y)
			o2x,o2y=Scaling(o2x,o2y)
			# scales the vertices (the end points of major and minor axes) about the origin

			a=abs(((c1-o1x)**2+(c2-o1y)**2)**0.5) # calculates the length of major-axis of the ellipse
			b=abs(((c1-o2x)**2+(c2-o2y)**2)**0.5) # calculates the length of minor-axis of the ellipse
			print("ellipse", c1, c2, a, b,)	

			plt.ion() # makes the plot interactive
			plt.plot(x_coordinates+[x_coordinates[0]],y_coordinates+[y_coordinates[0]])
			plt.pause(.00001)
			# plots the transformed ellipse


		if order[0]=="R": # Rotation
			temp_x=[]
			temp_y=[]
			i=order.split()
			theta=float(i[-1])
			theta=(theta/180)*3.14 # converts the angle of rotation into radians
			for i in range (len(x_coordinates)):
				x=x_coordinates[i]
				y=y_coordinates[i]
				outputs=Rotation(x,y)
				temp_x.append(outputs[0])
				temp_y.append(outputs[1])
			x_coordinates=temp_x
			y_coordinates=temp_y
			c1,c2=Rotation(c1,c2) # Rotating centers about the origin

			o1x,o1y=Rotation(o1x,o1y)
			o2x,o2y=Rotation(o2x,o2y)
			# rotates the vertices (the end points of major and minor axes) about the origin

			a=abs(((c1-o1x)**2+(c2-o1y)**2)**0.5) # calculates the length of major-axis of the ellipse
			b=abs(((c1-o2x)**2+(c2-o2y)**2)**0.5) # calculates the length of minor-axis of the ellipse
			print("ellipse", c1, c2, a, b,)

			plt.ion() # makes the plot interactive
			plt.plot(x_coordinates+[x_coordinates[0]],y_coordinates+[y_coordinates[0]])
			plt.pause(.00001)
			# plots the transformed ellipse

		order=input()

#___________________________________________________THE END____________________________________________________________________________
