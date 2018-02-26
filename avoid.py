# Avoid using '', [], and {} as default parameters to funtions
# prefer names=None to names=[] for default parameters

## Harmful
def f(a, L=[]):
	L.append(a)
	return L
print(f(1))
print(f(2))
print(f(3))


## Idiomatic
# If we don't want the default to be shared between subsequent calls,
# we can write the function like this instead

def f(a, L=None):
	if L is None:
		L=[]
	L.append(a)
	return L
print(f(1))
print(f(2))
print(f(3))
