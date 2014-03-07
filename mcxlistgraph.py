from mcxnowapi import McxNowSession
import requests
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib 
import datetime
import pytz
import time




def write_hist_data():
	S = McxNowSession('yungcrypt', 'n0t3ncrypted')
	cur = raw_input('what currency are we working with?: ')

	cur_history = S.GetCurrencyHistoryOrders(cur)
	#Data is returned in lists [time,type,ammt,ammtbtc,price]
	#opens the file for writing
	file_open = open('mcxlistgraph.txt', 'w')
	file_open.truncate()
	count = 0
	while count < 24:
		
			
		time = str(cur_history[count][0])
		price = str(cur_history[count][4])
		file_open.write(time)
		#file_open.write(amount)
		file_open.write(' ')
		file_open.write(price)
		
		if count < 23:
			newline = "\n"
			file_open.write(newline)
		count +=1


	file_open.close()





	

def graph_data():

	x = []
	y = []

	read_file = open('mcxlistgraph.txt', 'r')
	sep_file = read_file.read().split('\n')
	
	
	for pair in sep_file:
		XY = pair.split(' ')
		x.append(float(XY[0]))
		y.append(float(XY[1]))

	
	x = np.array(x)
	y = np.array(y)
	fig=plt.figure()
	rect = fig.patch
	ax1 = fig.add_subplot(1,1,1, axisbg='white') #height x Width x chart#
	rect.set_facecolor('black')


	#ax1.plot_date(md.epoch2num(x), y, 'c', linewidth=4)
	est=pytz.timezone('US/Eastern')
	ax1.plot_date(md.epoch2num(x), y,tz=est,linestyle='dashed',xdate=True)
	ax1.tick_params(axis='x', colors='red')
	ax1.tick_params(axis='y', colors='red')
	
	plt.setp(plt.xticks()[1], rotation=30)

	
	ax1.grid(True)
	plt.show()
	print y
	
#def animate():

		
write_hist_data()
graph_data()





