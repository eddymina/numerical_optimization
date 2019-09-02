import numpy as np
import matplotlib.pyplot as plt


# from autograd import elementwise_grad as egrad 
# import autograd.numpy as np
# def autograd(f,x,order=1):
# 	a= ''
# 	b= ''
# 	for i in range(order):
# 		a+='egrad('
# 		b += ')'

# 	return eval(a+'f'+b +'(x)')


def diff_grad(y,x,order=1,boundaries=False):

	"""
	Illustration of Numpy Gradient 
	"""
	
	assert(len(y)==len(x) )
	assert(type(order)==int)

	if order==0: return y

	for _ in range(order):
		deriv=[]

		# for i in range(1,len(x)-1):
		# 	deriv.append((y[i+1]-y[i-1])/(x[i+1]-x[i-1]))
		for i in range(1,len(y)-1):
		
			deriv.append(((y[i+1]-y[i-1])/(x[i+1]-x[i-1])))

		if boundaries:
			deriv.insert(0,((y[1]-y[0])/(x[1]-x[0])))
			deriv.append((y[len(x)-1]-y[len(x)-2])/(x[len(x)-1]-x[len(x)-2]))

		y = deriv

	return np.array(deriv)



def center_grad(f,x,order,h=1e-2,precision=2):

	assert(type(order)==int)
	assert(type(x) is np.ndarray)

	if order == 0:
		return f(x)

	elif order == 1:
		return np.round((f(x+h)-f(x-h))/(2*h),precision)

	elif order ==2: 
		return np.round((f(x+h)-2*f(x)+f(x-h))/(h**2),precision)

	elif order ==3: 
		return np.round((f(x+2*h)-f(x-2*h)-2*f(x+h)+2*f(x-h))/(h**3*2),precision)

	elif order ==4: 
		return np.round((f(x+2*h)+f(x-2*h)+6*f(x)-4*f(x+h)-4*f(x-h))/(h**4),precision)




def func(x):                 
	y = np.exp(-2.0 * x)
	return (1.0 - y) / (1.0 + y)




n=3
x = np.linspace(-7, 7, 200)

plt.plot(x,func(x),label='original func')
plt.plot(x,center_grad(func,x,n),color='r',label='center grad')
plt.plot(x,diff_grad(func(x),x,order=n,boundaries=True),color='b',label='diff grad')
plt.legend()
plt.show()




