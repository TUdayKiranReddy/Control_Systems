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
	
	pw0 = w[w <= factor/tau]
	pwi = w[(factor/tau < w)*(w <= 1/(tau*factor))]
	pw1 = w[w > 1/(tau*factor)]
	phi_0 = np.zeros(pw0.shape)
	phi_i = 45*(np.log10(pwi*tau/factor))/np.log10(factor)
	phi_1 = -90*np.ones(pw1.shape)
	
	bode = dict()
	bode['mag'] = mag
	bode['mag_assym'] = np.append(mag0, mag1)
	bode['phi'] = phi
	bode['phi_assym'] = np.append(phi_0, np.append(phi_i, phi_1))

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

	pw0 = w[w <= factor*wn]
	pwi = w[(factor*wn < w)*(w <= wn/(factor))]
	pw1 = w[w > wn/(factor)]
	phi_0 = np.zeros(pw0.shape)
	phi_i = 90*(np.log10(pwi/(factor*wn)))/np.log10(factor)
	phi_1 = -180*np.ones(pw1.shape)
	
	bode = dict()
	bode['mag'] = mag
	bode['mag_assym'] = np.append(mag0, mag1)
	bode['phi'] = phi
	bode['phi_assym'] = np.append(phi_0, np.append(phi_i, phi_1))

	return bode

def add(bode1, bode2):
	bode = dict()
	
	bode['mag'] = bode1['mag'] + bode2['mag']
	bode['mag_assym'] =  bode1['mag_assym'] + bode2['mag_assym']
	bode['phi'] = bode1['phi'] + bode2['phi']
	bode['phi_assym'] = bode1['phi_assym'] + bode2['phi_assym']
	
	return bode

def sub(bode1, bode2):
	bode = dict()
	
	bode['mag'] = bode1['mag'] - bode2['mag']
	bode['mag_assym'] =  bode1['mag_assym'] - bode2['mag_assym']
	bode['phi'] = bode1['phi'] - bode2['phi']
	bode['phi_assym'] = bode1['phi_assym'] - bode2['phi_assym']
	
	return bode

def constant_factor(k, bode_raw):
	bode = dict()
	
	bode['mag'] = 20*np.log10(k) + bode_raw['mag']
	bode['mag_assym'] = 20*np.log10(k) + bode_raw['mag_assym']
	bode['phi'] = bode_raw['phi']
	bode['phi_assym'] = bode_raw['phi_assym']
	
	return bode
	
w = np.linspace(1e-2, 1e3, 1e6)			### omega range
factor = 0.2							### factor for phase assymptotes

bode = sub(secound_order(0.1, 100), first_order(0.5))			## TF = (s/2 + 1)(1e4)/(s^2 + 20s + 1e4)
bode = constant_factor(1, bode)

mag = bode['mag']
mag_assym = bode['mag_assym']
phi = bode['phi']
phi_assym = bode['phi_assym']


plt.figure()
plt.semilogx(w, mag)
plt.semilogx(w, mag_assym, '--r')
plt.title('Magnitude')
plt.xlabel(r'$\omega$')
plt.ylabel('dB')
plt.grid()

plt.figure()
plt.semilogx(w, phi)
plt.semilogx(w, phi_assym, '--g')
plt.title('Phase('+r'$\phi$'+')')
plt.xlabel(r'$\omega$')
plt.ylabel('o')
plt.grid()

plt.show()
