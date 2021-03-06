# -*- coding: utf-8 -*-
# Copyright 2009 James Hensman
# Licensed under the Gnu General Public license, see COPYING

from kernels import *
		
def sample_1D(Nsamples=10):
	myRBF = RBF(1,.1)
	myLIN = linear(1,1)
	xlin = np.linspace(-10,10,100).reshape(100,1)
	K1 = myRBF(xlin,xlin)+np.eye(100)*1e-9
	Kchol1 = np.linalg.cholesky(K1)
	K2 = myLIN(xlin,xlin)+np.eye(100)*1e-9
	Kchol2 = np.linalg.cholesky(K2)
	samples1 = np.dot(np.random.randn(Nsamples,100),Kchol1.T)
	samples2 = np.dot(np.random.randn(Nsamples,100),Kchol2.T)
	pylab.figure()
	pylab.plot(xlin,samples1.T )
	pylab.figure()
	pylab.plot(xlin,samples2.T )
	pylab.figure()
	pylab.imshow(K1)
	pylab.figure()
	pylab.imshow(K2)
	

def sample_2D(Nsamples=5):
	myRBF = RBF(1,.1)
	xx,yy = np.mgrid[-10:10:50j,-10:10:50j]
	XX = np.vstack((xx.flatten(),yy.flatten())).T
	K = myRBF(XX,XX)
	Kchol = np.linalg.cholesky(K+np.eye(2500,2500)*1e-9)
	samples = np.dot(np.random.randn(Nsamples,2500),Kchol.T)
	for sample in samples:
		pylab.figure()
		sample = sample.reshape(50,50)
		pylab.contourf(xx,yy,sample)
	pylab.figure()
	pylab.imshow(K)
	

	
def sample_combined(Nsamples):
	mykernel = combined(1000,.1,.1,0.0)
	xx,yy = np.mgrid[-10:10:50j,-10:10:50j]
	XX = np.vstack((xx.flatten(),yy.flatten())).T
	K = mykernel(XX,XX)
	Kchol = np.linalg.cholesky(K+np.eye(2500,2500)*1e-9)
	samples = np.dot(np.random.randn(Nsamples,2500),Kchol.T)
	samples = [e.reshape(50,50) for e in samples]
	for sample in samples:
		pylab.figure()
		pylab.contourf(xx,yy,sample,40)
	pylab.figure()
	pylab.imshow(K)
	
def sample_1D_poly(Nsamples=10):
	myPoly = polynomial(1,5)
	xlin = np.linspace(-2,2,100).reshape(100,1)
	K = myPoly(xlin,xlin)+np.eye(100)*1e-7
	Kchol = np.linalg.cholesky(K)
	samples = np.dot(np.random.randn(Nsamples,100),Kchol.T)
	pylab.figure()
	pylab.plot(xlin,samples.T )
	pylab.figure()
	pylab.imshow(K)
	
	
if __name__=="__main__":
	import numpy as np
	import pylab
	#sample_1D()
	#sample_2D()
	sample_1D_poly()
	#sample_combined(10)
	
	
	pylab.show()
	
	