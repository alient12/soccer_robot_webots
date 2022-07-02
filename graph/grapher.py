import numpy as np
import matplotlib.pyplot as plt


vr_arr = np.load('vr_arr.npy')
vl_arr = np.load('vl_arr.npy')
er_arr = np.load('er_arr.npy')
ep_arr = np.load('ep_arr.npy')

fig = plt.figure()
ax = fig.add_subplot(111)

time_arr = np.arange(0, vr_arr.shape[0])

plt.plot(time_arr, vr_arr, label='vr', color='r')
plt.plot(time_arr, vl_arr, label='vl', color='b')
plt.plot(time_arr, er_arr[:1465], label='er', color='g')
plt.plot(time_arr, ep_arr[:1465], label='ep', color='y')
plt.legend()

plt.savefig('graph.png')
plt.savefig('graph.pdf')
plt.show()