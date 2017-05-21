#!/usr/bin/python

import matplotlib.pyplot as plt

# Generate files with ./pid | grep "Total Error: " > <controller>_total_error.txt
files = { 'pid': '../build/pid_total_error.txt',
          'pd' : '../build/pd_total_error.txt',
          'p'  : '../build/p_total_error.txt'
        }

data = {}
for key in files.keys():
  print('Processing %s controller file %s ...' % (key.upper(), files[key]))
  data[key] = []
  with open(files[key], 'r') as f:
    for line in f:
      line = line.strip().split('Total Error: ')
      if (len(line) > 1):
        data[key].append(float(line[1]))

# determine data file with minimum number of points or cap at 2K samples
max_samples = min(len(data['pid']), len(data['pd']), len(data['p']), 2000)
x = range(max_samples)
print('Maximum number of samples is: %d' % max_samples)

plt.plot(x, data['p'][0:max_samples])
plt.plot(x, data['pd'][0:max_samples])
plt.plot(x, data['pid'][0:max_samples])
plt.ylim((-100, 1500))
plt.xlabel('Sample')
plt.ylabel('Total Error')
plt.title('PID Controller Error')
plt.grid(True)
plt.legend(['P', 'PD', 'PID'])
plt.show()
