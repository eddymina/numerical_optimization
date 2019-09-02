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



def center_grad(f,x,order,h=1e-2,precision=6):

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

	elif order>=5:
		return "NO SUPPORT FOR DERIV > 4th order"




def func(x):                 
	return  1. / (1. + np.exp(-x))

x = np.linspace(-7, 7, 200)

def sample():

	plt.subplot(121)
	plt.title('Looking @ center taylor series approx gradient')
	plt.plot(x,func(x),label='original sigmoid func')
	plt.plot(x,center_grad(func,x,1),label='center grad order 1')
	plt.plot(x,center_grad(func,x,2),label='center grad order 2')
	plt.plot(x,center_grad(func,x,3),label='center grad order 3')
	plt.plot(x,center_grad(func,x,4),label='center grad order 4')
	plt.legend()

	plt.subplot(122)
	plt.title('Looking @ numerical gradient')
	plt.plot(x,func(x),label='original sigmoid func')
	plt.plot(x,diff_grad(func(x),x,order=1,boundaries=True),label='diff grad order 1')
	plt.plot(x,diff_grad(func(x),x,order=2,boundaries=True),label='diff grad order 2')
	plt.plot(x,diff_grad(func(x),x,order=3,boundaries=True),label='diff grad order 3')
	plt.plot(x,diff_grad(func(x),x,order=4,boundaries=True),label='diff grad order 4')
	plt.legend()

	plt.show()




sample()
