def ans(io, y, n, msg=""):
	while True:
		if io == y:
			if msg is not "":
				print msg
			break
		elif io == n:
			break
		else:
			io = raw_input("Please enter {} or {}  ".format(y, n))
			continue

