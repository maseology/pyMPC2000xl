
import os
import numpy as np
import struct
import matplotlib.pyplot as plt


fp = "test/TIP.SND" # "C:/Users/mason/Desktop/MPC_filecreator_v1/transfer/AMONWING/AMON1.SND" # 
with open(fp,"rb") as file:
    print((os.path.getsize(fp)-42)/2)

    if struct.unpack('bb', file.read(2)) != (1,4): print("SND ERROR1")
    print("filename: " + str(struct.unpack('16s', file.read(16))[0],'utf-8'))
    if struct.unpack('b', file.read(1))[0] != 0: print("SND ERROR2")
    
    print("level: " + str(struct.unpack('b', file.read(1))[0]))
    print("tune: " + str(struct.unpack('b', file.read(1))[0]))
    nchan = struct.unpack('b', file.read(1))[0] + 1
    print("n channels: " + str(nchan))
    
    print("start: " + str(struct.unpack('L', file.read(4))[0]))
    print("loop end: " + str(struct.unpack('L', file.read(4))[0]))
    nframes = struct.unpack('L', file.read(4))[0]
    print("end: " + str(nframes))
    print("loop length: " + str(struct.unpack('L', file.read(4))[0]))

    print("loop mode: " + str(struct.unpack('b', file.read(1))[0]))
    print("beats in loop: " + str(struct.unpack('b', file.read(1))[0]))
    print("frequency: " + str(struct.unpack('H', file.read(2))[0]))

    nval = nframes*nchan
    print(nval)
    signal = np.array(struct.unpack('h'*nval, file.read(2*nval)))    
    if not file.read(1): print("EOF reached")

    signal = signal.reshape((nframes,nchan))
    print(signal)

    plt.figure(1)
    plt.title(fp)
    plt.plot(signal)
    plt.show()


# 42 byte header:
# Length   Format              Description
# ----------------------------------------------------------------------
#     2                         1,4
#     16     ASCII               Filename (without extension, space padded)
#     1                         0
#     1     unsigned char       Level 0...200 (default 100)
#     1     unsigned char       Tune -120...+120
#     1     unsigned char       Channels: 0=Mono 1=Stereo
#     4     unsigned long       Start
#     4     unsigned long       Loop End
#     4     unsigned long       End
#     4     unsigned long       Loop Length
#     1     unsigned char       Loop Mode: 0=Off 1=On
#     1     unsigned char       Beats in loop 1...16 (default 1)
#     2     unsigned short      Sampling frequency (default 44100)