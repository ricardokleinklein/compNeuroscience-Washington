"""
	Week 4 coding exercises
"""

import os
import pickle
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
	# Load dataset
	with open('tuning3_4.pickle', 'rb') as f:
		data = pickle.load(f)

	# plt_idx=1
	# for neuron in ['neuron1', 'neuron2', 'neuron3', 'neuron4']:
	# 	data_mat = data[neuron]
	# 	neuron_exp = np.mean(data_mat, axis=0)
	# 	plt.subplot(2, 2, plt_idx)
	# 	plt.plot(data['stim'])
	# 	plt.gca().set_title(neuron)
	# 	plt_idx += 1
	# plt.show()

	# plt_idx=1
	# for neuron in ['neuron1', 'neuron2', 'neuron3', 'neuron4']:
	# 	data_mat = data[neuron]
	# 	fano = np.var(data_mat, axis=0) / np.mean(data_mat, axis=0)
	# 	plt.subplot(2, 2, plt_idx)
	# 	plt.plot(fano)
	# 	plt.gca().set_title(neuron)
	# 	plt_idx += 1
	# plt.show()

	with open('pop_coding.pickle', 'rb') as f:
		data_pop = pickle.load(f)
	
	for i in ['1', '2', '3', '4']:
		r_max = np.max(np.mean(data['neuron' + i], axis=0))
		arg = np.divide(np.mean(data_pop['r'+i]), r_max)
		

