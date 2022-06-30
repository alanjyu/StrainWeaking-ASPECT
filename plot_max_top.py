# plotting time vs maximum topography

import matplotlib.pyplot as plt
import numpy as np


# import stats file from line 29
stats_h22 = open(r'C:\Users\alanj\Downloads\output-heron_2022\statistics').readlines()[28:] # heron_2022

stats_15aif = open(r'C:\Users\alanj\Downloads\output-heron_2022_15ang\statistics').readlines()[28:] # heron_2022_15aif

stats_10coh = open(r'C:\Users\alanj\Downloads\output-heron_2022_10coh\statistics').readlines()[28:] # heron_2022_10coh

stats_25wf = open(r'C:\Users\alanj\Downloads\output-heron_2022_halfwf\statistics').readlines()[28:] # heron_2022_.25wf

stats_h19 = open(r'C:\Users\alanj\Downloads\output-heron_2019\statistics').readlines()[28:] # heron_2019

stats_a13 = open(r'C:\Users\alanj\Downloads\output-allken_2013\statistics').readlines()[28:] # allken_2013

stats_b13 = open(r'C:\Users\alanj\Downloads\output-brune_2013\statistics').readlines()[28:] # brune_2013

stats_g21 = open(r'C:\Users\alanj\Downloads\output-gouiza_2021\statistics').readlines()[28:] # gouiza_2021

stats_g21v = open(r'C:\Users\alanj\Downloads\output-gouiza_2021_viscous\statistics').readlines()[29:] # gouiza_2021_viscous


# append each line into a stripped list
r_h22 = []
for s in stats_h22:
  r_h22.append(s.strip().split())

r_15aif = []
for s in stats_15aif:
  r_15aif.append(s.strip().split())

r_10coh = []
for s in stats_10coh:
  r_10coh.append(s.strip().split())

r_25wf = []
for s in stats_25wf:
  r_25wf.append(s.strip().split())

r_h19 = []
for s in stats_h19:
  r_h19.append(s.strip().split())

r_a13 = []
for s in stats_a13:
  r_a13.append(s.strip().split())

r_b13 = []
for s in stats_b13:
  r_b13.append(s.strip().split())

r_g21 = []
for s in stats_g21:
  r_g21.append(s.strip().split())

r_g21v = []
for s in stats_g21v:
  r_g21v.append(s.strip().split())


# time in yr
t_h22 = np.zeros(len(r_h22))
t_15aif = np.zeros(len(r_15aif))
t_10coh = np.zeros(len(r_10coh))
t_25wf = np.zeros(len(r_25wf))
t_h19 = np.zeros(len(r_h19))
t_a13 = np.zeros(len(r_a13))
t_b13 = np.zeros(len(r_b13))
t_g21 = np.zeros(len(r_g21))
t_g21v = np.zeros(len(r_g21v))


# max topography in km
mt_h22 = np.zeros(len(r_h22))
for i in range(len(r_h22)):
  t_h22[i] = float(r_h22[i][1])/1e7 # convert yr to myr
  mt_h22[i] = float(r_h22[i][22])/1e3 # convert m to km

mt_15aif = np.zeros(len(r_15aif))
for i in range(len(r_15aif)):
  t_15aif[i] = float(r_15aif[i][1])/1e7
  mt_15aif[i] = float(r_15aif[i][22])/1e3

mt_10coh = np.zeros(len(r_10coh))
for i in range(len(r_10coh)):
  t_10coh[i] = float(r_10coh[i][1])/1e7
  mt_10coh[i] = float(r_10coh[i][22])/1e3

mt_25wf = np.zeros(len(r_25wf))
for i in range(len(r_25wf)):
  t_25wf[i] = float(r_25wf[i][1])/1e7
  mt_25wf[i] = float(r_25wf[i][22])/1e3

mt_h19 = np.zeros(len(r_h19))
for i in range(len(r_h19)):
  t_h19[i] = float(r_h19[i][1])/1e7
  mt_h19[i] = float(r_h19[i][22])/1e3

mt_a13 = np.zeros(len(r_a13))
for i in range(len(r_a13)):
  t_a13[i] = float(r_a13[i][1])/1e7
  mt_a13[i] = float(r_a13[i][22])/1e3

mt_b13 = np.zeros(len(r_b13))
for i in range(len(r_b13)):
  t_b13[i] = float(r_b13[i][1])/1e7
  mt_b13[i] = float(r_b13[i][22])/1e3

mt_g21 = np.zeros(len(r_g21))
for i in range(len(r_g21)):
  t_g21[i] = float(r_g21[i][1])/1e7
  mt_g21[i] = float(r_g21[i][22])/1e3

mt_g21v = np.zeros(len(r_g21v))
for i in range(len(r_g21v)):
  t_g21v[i] = float(r_g21v[i][1])/1e7
  mt_g21v[i] = float(r_g21v[i][23])/1e3


# plt.plot(t_h22, mt_h22, label='EXP-1')
# plt.plot(t_15aif, mt_15aif, label='EXP-9')
# plt.plot(t_10coh, mt_10coh, label='EXP-10')
# plt.plot(t_25wf, mt_25wf, label='EXP-11')
# plt.plot(t_h19, mt_h19, label='EXP-12')
# plt.plot(t_a13, mt_a13, label='EXP-13')
# plt.plot(t_b13, mt_b13, label='EXP-14')
# plt.plot(t_g21, mt_g21, label='EXP-15')

fig, ax = plt.subplots(1, 2, figsize=(12.5, 6))


# first subplot
ax[0].plot(t_h22, mt_h22, label='EXP-1', color='blue')
ax[0].plot(t_h19, mt_h19, label='EXP-12', linestyle='--', color='black')
ax[0].plot(t_a13, mt_a13, label='EXP-13', linestyle='--', color='gray')
ax[0].plot(t_b13, mt_b13, label='EXP-14', linestyle='--', color='lightgray')

ax[0].set_xlim([0, 2.5])
ax[0].set_ylim([0, 6])
ax[0].set_xlabel('Time (m.y.)', fontweight="bold")
ax[0].set_ylabel('Maximum Topography (km)', fontweight="bold")
ax[0].grid(linestyle='dotted')
ax[0].legend(loc="upper right")


# second subplot
ax[1].plot(t_h22, mt_h22, label='EXP-1', color='blue')
ax[1].plot(t_15aif, mt_15aif, label='EXP-9', linestyle='-.', color='darkred')
ax[1].plot(t_10coh, mt_10coh, label='EXP-10', linestyle=':', color='turquoise')
ax[1].plot(t_25wf, mt_25wf, label='EXP-11', linestyle='--', color='red')
ax[1].plot(t_g21, mt_g21, label='EXP-15')

ax[1].set_xlim([0, 2.5])
ax[1].set_ylim([0, 6])
ax[1].set_xlabel('Time (m.y.)', fontweight="bold")
ax[1].grid(linestyle='dotted')
ax[1].legend(loc="upper right")


# show figure

plt.tight_layout()
plt.show() # showing figure