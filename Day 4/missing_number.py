'''You are presented with two arrays, all containing positive integers. One of the arrays will have one extra number, see below:

[1,2,3] and [1,2,3,4] should return 4

[4,66,7] and [66,77,7,4] should return 77'''

def find_missing(x,y):
	sum_x= sum(x)
	sum_y= sum(y)

	if sum_x== sum_y:
		return 0
	if sum_x > sum_y:
		return sum_x - sum_y
	else:
		return sum_y - sum_x

