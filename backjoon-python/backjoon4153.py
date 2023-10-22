triangle=[3]
while (1):
	triangle=list(map(int,input().split()))
	if triangle.count(0)==3:
		break
	triangle.sort()
	max = triangle[2]
	min = triangle[0]
	mid = triangle[1]
	if max**2 == (mid**2+min**2):
		print("right")
	else:
		print("wrong")
