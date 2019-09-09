from profile_func import profile_dec

@profile_dec
def test(n):
	for i in range(n):
		i *= 1
	return i

if __name__ == "__main__":
	n = 100000
	M = test(n)
	print(M)