import matplotlib
matplotlib.use('Agg')
import numpy as np
import os
from matplotlib.pyplot import *
import tcn
import pickle as pkl
import pandas as pd
#from custom_classifier import create_custom_classifier



APR4 = pd.DataFrame(pd.read_pickle('bulla-O5-APR4-training-set-with-mej.pkl'))
MPA1 = pd.DataFrame(pd.read_pickle('bulla-O5-MPA1-training-set-with-mej.pkl'))

mej1 = 0.029999999
mej2 = 0.039999999
mej3 = 0.050000001
idx1_mej1 = np.random.choice(APR4.index[APR4['mej']==mej1],50,replace=False)
idx2_mej1 = np.random.choice(MPA1.index[MPA1['mej']==mej1],50,replace=False)
idx1_mej2 = np.random.choice(APR4.index[APR4['mej']==mej2],50,replace=False)
idx2_mej2 = np.random.choice(MPA1.index[MPA1['mej']==mej2],50,replace=False)
idx1_mej3 = np.random.choice(APR4.index[APR4['mej']==mej3],50,replace=False)
idx2_mej3 = np.random.choice(MPA1.index[MPA1['mej']==mej3],50,replace=False)

#print("Number of APR4 lightcurves with mej = 0.02999999:",len(idx1_mej1))
#print("Number of APR4 lightcurves with mej = 0.03999999:",len(idx1_mej2))
print("Number of APR4 lightcurves with mej = 0.050000001:",len(idx1_mej3))

#print("Number of MPA1 lightcurves with mej = 0.02999999:",len(idx2_mej1))
#print("Number of MPA1 lightcurves with mej = 0.03999999:",len(idx2_mej2))
#print("Number of MPA1 lightcurves with mej = 0.050000001:",len(idx2_mej3))


#print(APR4.loc[idx1_mej1,'mej'], MPA1.loc[idx2_mej1,'mej'])
#print(APR4.loc[idx1_mej2,'mej'], MPA1.loc[idx2_mej2, 'mej'])
'''
markers = ['.',',','o','v','^','<','>','1','2','3','4','8','s','p','P','*','h','H','+','x','X','D','d','|','_']
clf()
figure(figsize=(14,14))
subplot(321)
title(" mag vs time with common mej = {} \n Green: APR4 g, Red: MPA1 g".format(mej1))
ylabel("mag")
xlabel("mej")

for i in (idx1_mej1):
	print(APR4.loc[i,'mjd_g'])
	errorbar(APR4.loc[i,'mjd_g'],APR4.loc[i,'mag_g'],yerr=APR4.loc[i,'magerr_g'], ls='None', c='g',lw=0.5,marker=".")
	

for i in idx2_mej1:	
	errorbar(MPA1.loc[i,'mjd_g'],MPA1.loc[i,'mag_g'],yerr=MPA1.loc[i,'magerr_g'], ls='None', c='r',lw=0.5,marker=".")
	
subplot(322)
title("APR4 mag vs time with common mej = {}\n Green: APR4 r, Red: MPA1 r".format(mej1))
ylabel("mag")
xlabel("mej")
for i in (idx1_mej2):
	errorbar(APR4.loc[i,'mjd_r'],APR4.loc[i,'mag_r'],yerr=APR4.loc[i,'magerr_r'], ls='None', c='g',lw=0.5,marker=".")
for i in idx2_mej2:	
	errorbar(MPA1.loc[i,'mjd_r'],MPA1.loc[i,'mag_r'],yerr=MPA1.loc[i,'magerr_r'], ls='None', c='r',lw=0.5,marker=".")

subplot(323)
title("APR4 mag vs time with common mej = {}\n Green: APR4 g, Red: MPA1 g".format(mej2))
ylabel("mag")
xlabel("mej")
for i in (idx1_mej2):
	errorbar(APR4.loc[i,'mjd_g'],APR4.loc[i,'mag_g'],yerr=APR4.loc[i,'magerr_g'], ls='None', c='g',lw=0.5,marker=".")
for i in idx2_mej2:	
	errorbar(MPA1.loc[i,'mjd_g'],MPA1.loc[i,'mag_g'],yerr=MPA1.loc[i,'magerr_g'], ls='None', c='r',lw=0.5,marker=".")
subplot(324)
title("APR4 mag vs time with common mej = {}\n Green: APR4 r, Red: MPA1 r".format(mej2))
ylabel("mag")
xlabel("mej")
for i in (idx1_mej2):
	errorbar(APR4.loc[i,'mjd_r'],APR4.loc[i,'mag_r'],yerr=APR4.loc[i,'magerr_r'], ls='None', c='g',lw=0.5,marker=".")
for i in idx2_mej2:	
	errorbar(MPA1.loc[i,'mjd_r'],MPA1.loc[i,'mag_r'],yerr=MPA1.loc[i,'magerr_r'], ls='None', c='r',lw=0.5,marker=".")
subplot(325)
title("APR4 mag vs time with common mej = {}\n Green: APR4 g, Red: MPA1 g".format(mej3))
ylabel("mag")
xlabel("mej")
for i in (idx1_mej3):
	errorbar(APR4.loc[i,'mjd_g'],APR4.loc[i,'mag_g'],yerr=APR4.loc[i,'magerr_g'], ls='None', c='g',lw=0.5,marker=".")
for i in idx2_mej3:	
	errorbar(MPA1.loc[i,'mjd_g'],MPA1.loc[i,'mag_g'],yerr=MPA1.loc[i,'magerr_g'], ls='None', c='r',lw=0.5,marker=".")
subplot(326)
title("APR4 mag vs time with common mej = {}\n Green: APR4 r, Red: MPA1 r".format(mej3))
ylabel("mag")
xlabel("mej")
for i in (idx1_mej3):
	errorbar(APR4.loc[i,'mjd_r'],APR4.loc[i,'mag_r'],yerr=APR4.loc[i,'magerr_r'], ls='None', c='g',lw=0.5,marker=".")
for i in idx2_mej3:	
	errorbar(MPA1.loc[i,'mjd_r'],MPA1.loc[i,'mag_r'],yerr=MPA1.loc[i,'magerr_r'], ls='None', c='r',lw=0.5,marker=".")

tight_layout()
savefig('example5.jpg')
'''


































'''



g_1 = np.zeros(len(APR4))
r_1 = np.zeros(len(APR4))
for i in range(len(APR4)):
	
	if len(APR4.loc[i,'mag_g']) == 0   or len(APR4.loc[i,'mag_g'])==0 or len(APR4.loc[i,'mag_r'])==0 or len(APR4.loc[i,'mag_r']) == 0:
		g_1[i]=(0.00000000)
		r_1[i]=(0.00000000)
	else:
		t1 = (APR4.loc[i,'mag_g'])[-1] - (APR4.loc[i,'mag_g'])[0]
		t2 = (APR4.loc[i,'mag_r'])[-1] - (APR4.loc[i,'mag_r'])[0]
		g_1[i]=(t1)
		r_1[i]=(t2)
g_2 = np.zeros(len(MPA1))
r_2 = np.zeros(len(MPA1))
for i in range(len(MPA1)):
	if len(MPA1.loc[i,'mag_g']) == 0   or len(MPA1.loc[i,'mag_g'])==0 or len(MPA1.loc[i,'mag_r'])  == 0 or len(MPA1.loc[i,'mag_r']) ==0:
		g_2[i] =0.00000000
		g_2[i] =0.00000000
	else:
		t1 = (MPA1.loc[i,'mag_g'])[-1] - (MPA1.loc[i,'mag_g'])[0]
		t2 = (MPA1.loc[i,'mag_r'])[-1] - (MPA1.loc[i,'mag_r'])[0]
		g_2[i]=(t1)
		r_2[i]=(t2)
		

clf()
figure()
subplot(211)
title("Duration of LC vs mej")
ylabel("mag duration")
xlabel("Mej")
plot(APR4['mej'],(g_1),ls='None', c='r', label='APR4-g',lw=0.5,marker=".")
plot(MPA1['mej'],(g_2),ls='None', c='g', label='MPA1-g',lw=0.5,marker=".", alpha=0.2)
legend()
subplot(212)
title("Duration of LC vs mej")
ylabel("mag duration")
xlabel("Mej")
plot(APR4['mej'],(r_1),ls='None', c='r', label='APR4-r',lw=0.5,marker=".")
plot(MPA1['mej'],(r_2),ls='None', c='g', label='MPA1-r',lw=0.5,marker=".",alpha=0.2)

legend()
tight_layout()
savefig('example3.jpg')

'''

g_1 = np.zeros(len(APR4))
r_1 = np.zeros(len(APR4))
for i in range(len(APR4)):
	
	if len(APR4.loc[i,'mag_g']) == 0   or len(APR4.loc[i,'mag_g'])==0 or len(APR4.loc[i,'mag_r'])==0 or len(APR4.loc[i,'mag_r']) == 0:
		g_1[i]=(0.00000000)
		r_1[i]=(0.00000000)
	else:
		t1 = (APR4.loc[i,'mag_g'])[-1] - (APR4.loc[i,'mag_g'])[0]
		t2 = (APR4.loc[i,'mag_r'])[-1] - (APR4.loc[i,'mag_r'])[0]
		g_1[i]=(t1)
		r_1[i]=(t2)
g_2 = np.zeros(len(MPA1))
r_2 = np.zeros(len(MPA1))
for i in range(len(MPA1)):
	if len(MPA1.loc[i,'mag_g']) == 0   or len(MPA1.loc[i,'mag_g'])==0 or len(MPA1.loc[i,'mag_r'])  == 0 or len(MPA1.loc[i,'mag_r']) ==0:
		g_2[i] =0.00000000
		g_2[i] =0.00000000
	else:
		t1 = (MPA1.loc[i,'mag_g'])[-1] - (MPA1.loc[i,'mag_g'])[0]
		t2 = (MPA1.loc[i,'mag_r'])[-1] - (MPA1.loc[i,'mag_r'])[0]
		g_2[i]=(t1)
		r_2[i]=(t2)

figure()
subplot(223)
title("APR4 and MPA1 flux in g band with {} points".format(len(idx1g)))
ylabel("flux")
xlabel("mjd")
errorbar(apr4_mjd_g[idx1g], flux1g[idx1g], yerr=fluxerr1g[idx1g], ls='None', c='k', label='APR4',lw=0.5,marker=".")
errorbar(mpa1_mjd_g[idx2g], flux2g[idx2g], yerr=fluxerr2g[idx2g], ls='None', c='r', label='MPA1',lw=0.5,marker=".",alpha=0.4)
legend()

subplot(224)
title("APR4 and MPA1 flux in r band with {} points".format(len(idx1r)))
ylabel("flux")
xlabel("mjd")
errorbar(apr4_mjd_r[idx1r], flux1r[idx1r], yerr=fluxerr1r[idx1r], ls='None', c='k', label='APR4',lw=0.5,marker=".")
errorbar(mpa1_mjd_r[idx2r], flux2r[idx2r], yerr=fluxerr2r[idx2r], ls='None', c='r', label='MPA1',lw=0.5,marker=".",alpha=0.4)
legend()



	


