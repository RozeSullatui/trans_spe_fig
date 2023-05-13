# -*- coding: utf-8 -*-
import wave
import numpy as np
import struct
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import re
import pandas as pd
import os

# Commented out IPython magic to ensure Python compatibility.
# %cd '/content/drive/MyDrive/AI'

os.chdir('Sounds')
os.getcwd()

df = pd.read_csv('audio.csv')

tag = 0
for i in list(df['audio_data']):
  samplingFrequency, signalData = read(i)
  thing = re.findall('[a-z]+', i)
  f, ax = plt.subplots()
  # スペクトログラムをプロットする。
  Pxx, freqs, bins, im = ax.specgram(signalData[:,0], Fs=samplingFrequency, cmap='jet')
  plt.ylabel("Frequency")
  plt.xlabel("Time")
  plt.colorbar(im).set_label('Intensity [dB]')
  if df.loc[tag,'class']==0:
    plt.savefig("fig_specgram/truth/" + thing[8].split('.')[0] + '_' +thing[9].split('.')[0] + '.png')
  else:
    plt.savefig("fig_specgram/lie/" + thing[8].split('.')[0] + '_' +thing[9].split('.')[0] + '.png')
  if i ==i+"_1.wav":
    plt.show()
  plt.close(f)
  print(i)
  tag += 1