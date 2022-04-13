
import os
import numpy as np
import struct
import wave
# # import pyaudio # Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
# from pydub import AudioSegment
# from pydub.playback import play
import matplotlib.pyplot as plt


class SND:
    level = 100
    tune = 0
    start = 0
    loopmode = 0
    beats = 4

    def plot(self):
        plt.figure(1)
        plt.title(self.nam)
        plt.plot(self.signal)
        plt.show()

    def __init__(self, fp, verbose=False) -> None:
        fnam, ext = os.path.splitext(fp)
        if ext.lower() == '.snd':
            self.fp = fp
            self.__loadSND(fp, verbose)
        elif ext.lower() == '.wav':
            self.fp = fp
            self.nam = os.path.splitext(fnam)[0]
            self.__loadWAV(fp, verbose)
        else:
            print("unknown filetype: " + fp)

    def __loadSND(self,fp, verbose):
        with open(fp,"rb") as file:            
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
            
            if struct.unpack('bb', file.read(2)) != (1,4): print("SND ERROR1")
            self.nam = str(struct.unpack('16s', file.read(16))[0],'utf-8')
            if struct.unpack('b', file.read(1))[0] != 0: print("SND ERROR2")

            self.level = struct.unpack('b', file.read(1))[0]
            self.tune = struct.unpack('b', file.read(1))[0]
            self.nchan = struct.unpack('b', file.read(1))[0] + 1

            self.start = struct.unpack('L', file.read(4))[0]
            self.loopend = struct.unpack('L', file.read(4))[0]
            self.end = struct.unpack('L', file.read(4))[0]
            self.looplength = struct.unpack('L', file.read(4))[0]

            self.loopmode = struct.unpack('b', file.read(1))[0]
            self.beats = struct.unpack('b', file.read(1))[0]
            self.frequency = struct.unpack('H', file.read(2))[0]

            if verbose:
                print((os.path.getsize(fp)-42)/2)
                print("name: " + self.nam)
                print("level: " + str(self.level))
                print("tune: " + str(self.tune))            
                print("n channels: " + str(self.nchan))
                print("start: " + str(self.start))
                print("loop end: " + str(self.loopend))
                print("end: " + str(self.end))
                print("loop length: " + str(self.looplength))
                print("loop mode: " + str(self.loopmode))
                print("beats in loop: " + str(self.beats))
                print("frequency: " + str(self.frequency))

            nframes = self.end-self.start
            nval = nframes*self.nchan
            signal = np.array(struct.unpack('h'*nval, file.read(2*nval)))    
            if file.read(1): print("SND ERROR: EOF not reached")

            self.signal = signal.reshape((nframes,self.nchan))
            # if verbose: print(self.signal)

    def __loadWAV(self,fp,verbose):
        with wave.open(fp, "rb") as w:
            if verbose: print(w.getparams())
            if w.getcomptype() != 'NONE': print('SND.WAV Error: compression used: '+w.getcompname())
            self.nchan = w.getnchannels()
            self.frequency = w.getframerate()
            self.end = w.getnframes()
            self.loopend = self.end
            self.looplength = self.end

             # Extract Raw Audio from Wav File
            signal = w.readframes(-1)
            if w.getsampwidth() == 1:
                signal = np.frombuffer(signal, np.int8)
            elif w.getsampwidth() == 2:
                signal = np.frombuffer(signal, np.int16)

            if int(len(signal)/self.nchan) != self.end: print("WAV READ ERROR")
            self.signal = signal.reshape((self.end,self.nchan))

            if verbose:
                print("name: " + self.nam)
                # print("level: " + str(self.level))
                # print("tune: " + str(self.tune))            
                print("n channels: " + str(self.nchan))
                # print("start: " + str(self.start))
                # print("loop end: " + str(self.loopend))
                print("n frames: " + str(self.end))
                # print("loop length: " + str(self.looplength))
                # print("loop mode: " + str(self.loopmode))
                # print("beats in loop: " + str(self.beats))
                print("frequency: " + str(self.frequency))

    def save(self,fp):
        fnam, ext = os.path.splitext(fp)
        if ext.lower() == '.wav':
            self.__saveWAV(fp)
        else:
            print("unsupported filetype: " + fp)

    def __saveWAV(self,fp):
        with wave.open(fp, "wb") as w:
            w.setnchannels(self.nchan)
            w.setsampwidth(2) # int16
            w.setframerate(self.frequency)
            w.setnframes(self.end)
            w.writeframes(self.signal.flatten().tobytes())

    # def play(self):
    #     audio_segment = AudioSegment(
    #         self.signal.flatten().tobytes(), 
    #         frame_rate=self.frequency,
    #         sample_width=2, #channel1.dtype.itemsize, 
    #         channels=self.nchan
    #     )
    #     play(audio_segment)

    #     # #instantiate PyAudio  
    #     # p = pyaudio.PyAudio()  
    #     # #open stream  
    #     # stream = p.open(format = p.get_format_from_width(2),  
    #     #                 channels = self.nchan,  
    #     #                 rate = self.frequency,  
    #     #                 output = True)  
        
    #     # stream.write(self.signal.flatten())  
        
    #     # #stop stream  
    #     # stream.stop_stream()  
    #     # stream.close()  

    #     # #close PyAudio  
    #     # p.terminate()          