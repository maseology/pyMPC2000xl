

# .PRG extension and are partially described here:

#    Length   Format              Description
#    ----------------------------------------------------------------------
#       2                         7,4                          
#       2     unsigned short      Number of samples 1...64
#       1                         0

#    Repeat for 64 samples...
#      16     ASCII               Sample Name
#       1                         0

#       2                         30,0
#      16     ASCII               Program Name
#      15                         0,136,120,12,45,0,20,206,50,0,35,64,0,25,0

#    Repeat for MIDI notes 35...98
#       1     unsigned char       Sample 0...64 (255=none)
#      24                         0,44,0,88,0,0,0,0,0,0,0,0,0,100,0,0,0,0,100,0,0,0,0,0
 
#     388                         6,0,100,50,100,0,0...(see .PGM file)

#    Repeat for Pads A01...D12
#       1     unsigned char       Note number 35...98
