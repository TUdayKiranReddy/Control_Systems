import control as C
import numpy as np
import matplotlib.pyplot as plt

def first_order(tau):
	
	mag = -10*np.log10((w*tau)**2 + 1)
	phi = -180*np.arctan(w*tau)/np.pi

	w0 = w[w <= 1/tau]
	w1 = w[w > 1/tau]
	mag0 = (np.zeros(w0.shape))
	mag1 = (-20*np.log10(tau*w1))

	bode = dict()
	bode['mag'] = mag
	bode['mag_assym'] = np.append(mag0, mag1)
	bode['phi'] = phi

	return bode

def secound_order(eta, wn):

	mag = -10*np.log10(((1-(w/wn)**2)**2 + 4*((w/wn)*eta)**2))
	phi = -180*np.arctan((2*eta*w*wn)/(wn**2 - w**2))/np.pi
	phi_pos = phi[phi>0]
	phi_neg = phi[phi<0]
	phi = np.append(phi_neg, -180 + phi_pos)
	
	w0 = w[w <= wn]
	w1 = w[w > wn]
	mag0 = (np.zeros(w0.shape))
	mag1 = (-40*np.log10(w1/wn))
	
	bode = dict()
	bode['mag'] = mag
	bode['mag_assym'] = np.append(mag0, mag1)
	bode['phi'] = phi

	return bode

def add(bode1, bode2):
	bode = dict()
	
	bode['mag'] = bode1['mag'] + bode2['mag']
	bode['mag_assym'] =  bode1['mag_assym'] + bode2['mag_assym']
	bode['phi'] = bode1['phi'] + bode2['phi']
	
	return bode

def factor(k, bode_raw):
	bode = dict()
	
	bode['mag'] = 20*np.log10(k) + bode_raw['mag']
	bode['mag_assym'] = 20*np.log10(k) + bode_raw['mag_assym']
	bode['phi'] = bode_raw['phi']
	
	return bode
	
w = np.linspace(1e-2, 1e3, 1e6)


bode = add(first_order(0.05), secound_order(0.1, 100))
#bode = add(bode, secound_order(0.1, 100))

bode = factor(1, bode)

mag = bode['mag']
mag_assym = bode['mag_assym']
phi = bode['phi']


plt.figure()
plt.semilogx(w, mag)
plt.semilogx(w, mag_assym, '--r')
plt.title('Magnitude')
plt.xlabel(r'$\omega$')
plt.ylabel('dB')
plt.grid()

plt.figure()
plt.semilogx(w, phi)
plt.title('Phase('+r'$\phi$'+')')
plt.xlabel(r'$\omega$')
plt.ylabel('o')
plt.grid()

plt.show()
