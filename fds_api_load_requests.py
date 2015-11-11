# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 13:06:58 2015

@author: andrej
"""
import urllib
import logging
import json
import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
mpl.rcParams['font.size'] = 20
mpl.rcParams['axes.facecolor'] = 'white'
plt.style.use('ggplot')

def download_from_url(url):
    """Download url and return the content."""
    logging.debug('url %s', url)
    r = urllib.request.urlopen(url)
    data = r.read()
    data = data.decode(encoding='UTF-8')

    return data
    
url = 'https://fragdenstaat.de/api/v1/request/?limit=92&offset='

#print(data_decoded['objects'][0].keys())
print('load requests\n')
datasets = []
for offset in np.arange(9500,9592,500):
    complete_url = url + str(int(offset))
    data = download_from_url(complete_url)
    datasets.append(json.loads(data))
print('loading done')

np.save('request_data_until_'+str(offset+92),datasets)



