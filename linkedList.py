class Node:
	def __init__(self,data,next):
		self.data=data
		self.next= next
n1=Node("Hey",None)
n2=Node("This",n1)
n3=Node("is",n2)
n4=Node("Aishwarya",n3)
n5=Node("Karanth",n4)
head=n5
fasterpointer=head
slowerpointer=head
while fasterpointer.next !=None and fasterpointer.next.next!=None:
	fasterpointer=fasterpointer.next.next
	slowerpointer=slowerpointer.next
print(slowerpointer.data)
