from time import time
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

import pycuda.autoinit
from pycuda import gpuarray
from pycuda.elementwise import ElementwiseKernel


mandel_ker = ElementwiseKernel(
"pycuda::complex<float> *lattice, float *mandelbrot_graph, int max_iters, float upper_bound",
"""
mandelbrot_graph[i] = 1;

pycuda::complex<float> c = lattice[i];
pycuda::complex<float> z(0,0);

for (int j = 0; j<max_iters; j++){
	z = z*z+c;

	if(abs(z)>upper_bound){
		mandelbrot_graph[i] = 0;
		break;
	}
}
""",
"mandel_ker")

def gpu_mandelbrot(width, height, real_low, real_high, imag_low, imag_high, max_iters, upper_bound):

	real_vals = np.matrix(np.linspace(real_low, real_high, width), dtype=np.complex64)
	imag_vals = np.matrix(np.linspace(imag_high, imag_low, height), dtype=np.complex64) * 1j
	mandelbrot_lattice = np.array(real_vals + imag_vals.transpose(), dtype=np.complex64)

	mandelbrot_lattice = gpuarray.to_gpu(mandelbrot_lattice)

	mandelbrot_graph_gpu = gpuarray.empty(shape=mandelbrot_lattice.shape, dtype=np.float32)

	mandel_ker(mandelbrot_lattice, mandelbrot_graph_gpu, np.int32(max_iters), np.float32(upper_bound))

	mandelbrot_graph = mandelbrot_graph_gpu.get()

	return mandelbrot_graph

if __name__ == '__main__':
	t1 = time()
	mandel = gpu_mandelbrot(512,512,-2,2,-2,2,256,2)
	t2 = time()
	mandel_time = t2 - t1

	t1 = time()
	fig = plt.figure(1)
	plt.imshow(mandel, extent=(-2,2,-2,2))
	t2 = time()
	plot_time = t2-t1

	print('It took {} seconds to calculate Mandelbrot graph'.format(mandel_time))
	print('It took {} seconds to plot image'.format(plot_time))

	plt.show()
