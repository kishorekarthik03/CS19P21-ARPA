def IsPrime():
	a=11
	flag=0
	for i in range(2,a):
		if(a%i!=0):
			continue
		else:
			flag=1
			break
	if(flag==1):
		return "Not a Prime"
	else:
		return "Prime"