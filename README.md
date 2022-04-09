# pyMPC2000xl
A Python reader/writer of Akai MPC2000XL *.PRG and *.SND files.

inspried by https://www.midicase.com/mpceditor/ (only I wanted a little more control).

```
The MPC2000 and other related models use DOS formatted disks. 
Samples are saved with a .SND extension and contain 16-bit signed data after a 42 byte header:

   Length   Format              Description
   ----------------------------------------------------------------------
      2                         1,4
     16     ASCII               Filename (without extension, space padded)
      1                         0
      1     unsigned char       Level 0...200 (default 100)
      1     unsigned char       Tune -120...+120
      1     unsigned char       Channels: 0=Mono 1=Stereo
      4     unsigned long       Start
      4     unsigned long       Loop End
      4     unsigned long       End
      4     unsigned long       Loop Length
      1     unsigned char       Loop Mode: 0=Off 1=On
      1     unsigned char       Beats in loop 1...16 (default 1)
      2     unsigned short      Sampling frequency (default 44100)

MPC2000 programs have a .PRG extension and are partially described here:

   Length   Format              Description
   ----------------------------------------------------------------------
      2                         7,4                          
      2     unsigned short      Number of samples 1...64
      1                         0

   Repeat for 64 samples...
     16     ASCII               Sample Name
      1                         0

      2                         30,0
     16     ASCII               Program Name
     15                         0,136,120,12,45,0,20,206,50,0,35,64,0,25,0

   Repeat for MIDI notes 35...98
      1     unsigned char       Sample 0...64 (255=none)
     24                         0,44,0,88,0,0,0,0,0,0,0,0,0,100,0,0,0,0,100,0,0,0,0,0
 
    388                         6,0,100,50,100,0,0...(see .PGM file)

   Repeat for Pads A01...D12
      1     unsigned char       Note number 35...98
```
from: http://mda.smartelectronix.com/akai/akaiinfo.htm
