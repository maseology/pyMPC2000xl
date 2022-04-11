

import numpy as np
import wave
import matplotlib.pyplot as plt

fp = "test/airplane_chime_x.wav" #"test/sabbath.wav"
with wave.open(fp, "rb") as w:
    print(w.getparams())
    print("n channels: " + str(w.getnchannels()))
    print("frequency: " + str(w.getframerate()))
    # print(w.getcomptype())
    # print(w.getcompname())

    # Extract Raw Audio from Wav File
    signal = w.readframes(-1)
    if w.getsampwidth() == 1:
        signal = np.frombuffer(signal, np.int8)
    elif w.getsampwidth() == 2:
        signal = np.frombuffer(signal, np.int16)
 
    if int(len(signal)/w.getnchannels()) != w.getnframes(): print("WAV READ ERROR")
    signal = signal.reshape((w.getnframes(),w.getnchannels()))


    plt.figure(1)
    plt.title(fp)
    plt.plot(signal)
    plt.show()