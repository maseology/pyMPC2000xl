
import struct


class programsettings:
    NVsliderAsignment = 34 # 34=off
    NVtuningLow = -120 # -120-120
    NVtuningHigh = 120 # -120-120
    NVdecayLow = 12 # 0-100
    NVdecayHigh = 45 # 0-100
    NVattackLow = 0 # 0-100
    NVattackHigh = 20 # 0-100
    NVfilterLow  = 12 # -50-50
    NVfilterHigh  = 45 # -50-50
    VoiceOverlap = 0 # 0:poly 1:Mono 2:NoteOff
    # Decay = 0
    # IndVol = 0

    def __init__(self, bytes) -> None:
        # print(bytes)
        if bytes[0] != 0: print("programsettings ERROR1")
        self.NVsliderAssignment = bytes[1]
        self.NVtuningLow = bytes[2]-256 if bytes[2]>120 else bytes[2]
        self.NVtuningHigh = bytes[3]-256 if bytes[3]>120 else bytes[3]
        self.NVdecayLow = bytes[4]
        self.NVattackLow = bytes[5]
        self.NVdecayHigh = bytes[6]
        self.NVattackHigh = bytes[7]
        self.NVfilterLow = bytes[8]-256 if bytes[8]>120 else bytes[8]
        self.NVfilterHigh = bytes[9]-256 if bytes[9]>120 else bytes[9]
        self.VoiceOverlap = bytes[10]

        if bytes[11] != 35: print("programsettings ERROR2")
        if bytes[12] != 64: print("programsettings ERROR3")
        if bytes[13] != 0: print("programsettings ERROR4")
        if bytes[14] != 25: print("programsettings ERROR5")
        if bytes[15] != 0: print("programsettings ERROR6")

class padsettings:
    Mode = 0 # 0:Normal 1:Simul 2:VelSW 3:DecaySW
    VoiceOverlap = 0 # 0:poly 1:Mono 2:NoteOff
    Tune = 0
    Frequency = 100
    Resonance = 0
    Attack = 0
    Decay = 0
    DecayMode = 0 # 0:End 1:Start
    IfOver1 = 44
    IfOver2 = 88
    SimulPlay1 = 34 # 34=off (otherwise represents "Use note" when Mode >1)
    SimulPlay2 = 34 # 34=off (otherwise represents "Use note" when Mode >1)
    MuteNote1 = 34 # 34=off
    MuteNote2 = 34 # 34=off
    NVtype = 0 # 0:Tuning 1:Decay 2:Attack 3:Filter

    def __init__(self,bytes) -> None:
        # print(bytes)
        self.Mode = bytes[0]
        self.IfOver1 = bytes[1]
        self.SimulPlay1 = bytes[2]
        self.IfOver2 = bytes[3]
        self.SimulPlay2 = bytes[4]
        self.VoiceOverlap = bytes[5]
        self.MuteNote1 = bytes[6]
        self.MuteNote2 = bytes[7]
        self.Tune = bytes[8] # short??
        if bytes[9] == 255: self.Tune -= 256
        self.Attack = bytes[10]
        self.Decay = bytes[11]
        self.DecayMode = bytes[12]
        self.Frequency = bytes[13]
        self.Resonance = bytes[14]
        self.filterAttack = bytes[15] # if bytes[15] != 0: print('padsettings ERROR')
        self.filterDecay = bytes[16] # if bytes[16] != 0: print('padsettings ERROR')
        self.filterAmount = bytes[17] # if bytes[17] != 0: print('padsettings ERROR')
        self.attackVeloLevel = bytes[18] # if bytes[18] != 100: print('padsettings ERROR')
        self.attackVeloAttack = bytes[19] # if bytes[19] != 0: print('padsettings ERROR')
        self.attackVeloStart = bytes[20] # if bytes[20] != 0: print('padsettings ERROR')
        self.filterVeloFreq = bytes[21] # if bytes[21] != 0: print('padsettings ERROR')
        self.NVtype = bytes[22]
        self.tuneVeloPitch = bytes[23] # if bytes[23] != 0: print('padsettings ERROR')

class mixersettings:
    MainOutput = 100
    Pan = 50 # 0:left 100:right
    IndividualChannel = 0 # for stereo 1:1/2 3:3/4 6:5/6 8:7/8
    ChanVolume = 0
    
    def __init__(self,bytes) -> None:
        # print(bytes)
        if bytes[0] != 0: print("mixersettings ERROR1")
        self.MainOutput = bytes[1]
        self.Pan = bytes[2]
        self.IndividualChannel = bytes[3]
        self.ChanVolume = bytes[4]
        if bytes[5] != 0: print("mixersettings ERROR2")

class unknown:
    # see: https://github.com/Alesclandre/mpc2000xlapp/blob/main/classes/MPC2000XL_PGM/IO_PGM.as
    def __init__(self,bytes) -> None:
        if bytes[0] != 2: print("unknown UNKNOWN bytes[0]: " + str(bytes[0]))
        if bytes[1] != 0: print("unknown UNKNOWN bytes[1]: " + str(bytes[1]))
        if bytes[2] != 72: print("unknown UNKNOWN bytes[2]: " + str(bytes[2]))
        if bytes[3] != 0: print("unknown UNKNOWN bytes[3]: " + str(bytes[3]))
        if bytes[4] != -48: print("unknown UNKNOWN bytes[4]: " + str(bytes[4]))
        if bytes[5] != 7: print("unknown UNKNOWN bytes[5]: " + str(bytes[5]))
        if bytes[6] != 0: print("unknown UNKNOWN bytes[6]: " + str(bytes[6]))
        if bytes[7] != 0: print("unknown UNKNOWN bytes[7]: " + str(bytes[7]))
        if bytes[8] != 99: print("unknown UNKNOWN bytes[8]: " + str(bytes[8]))
        if bytes[9] != 1: print("unknown UNKNOWN bytes[9]: " + str(bytes[9]))
        if bytes[10] != 20: print("unknown UNKNOWN bytes[10]: " + str(bytes[10]))
        if bytes[11] != 8: print("unknown UNKNOWN bytes[11]: " + str(bytes[11]))
        if bytes[12] != 29: print("unknown UNKNOWN bytes[12]: " + str(bytes[12]))
        if bytes[13] != -4: print("unknown UNKNOWN bytes[13]: " + str(bytes[13]))
        if bytes[14] != 50: print("unknown UNKNOWN bytes[14]: " + str(bytes[14]))
        if bytes[15] != 51: print("unknown UNKNOWN bytes[15]: " + str(bytes[15]))
        if bytes[16] != 2: print("unknown UNKNOWN bytes[16]: " + str(bytes[16]))
        if bytes[17] != 50: print("unknown UNKNOWN bytes[17]: " + str(bytes[17]))
        if bytes[18] != 60: print("unknown UNKNOWN bytes[18]: " + str(bytes[18]))
        if bytes[19] != 8: print("unknown UNKNOWN bytes[19]: " + str(bytes[19]))
        if bytes[20] != 5: print("unknown UNKNOWN bytes[20]: " + str(bytes[20]))
        if bytes[21] != 10: print("unknown UNKNOWN bytes[21]: " + str(bytes[21]))
        if bytes[22] != 20: print("unknown UNKNOWN bytes[22]: " + str(bytes[22]))
        if bytes[23] != 20: print("unknown UNKNOWN bytes[23]: " + str(bytes[23]))
        if bytes[24] != 50: print("unknown UNKNOWN bytes[24]: " + str(bytes[24]))
        if bytes[25] != 0: print("unknown UNKNOWN bytes[25]: " + str(bytes[25]))
        if bytes[26] != 0: print("unknown UNKNOWN bytes[26]: " + str(bytes[26]))
        if bytes[27] != 2: print("unknown UNKNOWN bytes[27]: " + str(bytes[27]))
        if bytes[28] != 15: print("unknown UNKNOWN bytes[28]: " + str(bytes[28]))
        if bytes[29] != 25: print("unknown UNKNOWN bytes[29]: " + str(bytes[29]))
        if bytes[30] != 0: print("unknown UNKNOWN bytes[30]: " + str(bytes[30]))
        if bytes[31] != 5: print("unknown UNKNOWN bytes[31]: " + str(bytes[31]))
        if bytes[32] != 65: print("unknown UNKNOWN bytes[32]: " + str(bytes[32]))
        if bytes[33] != 20: print("unknown UNKNOWN bytes[33]: " + str(bytes[33]))
        if bytes[34] != 30: print("unknown UNKNOWN bytes[34]: " + str(bytes[34]))
        if bytes[35] != 1: print("unknown UNKNOWN bytes[35]: " + str(bytes[35]))
        if bytes[36] != 5: print("unknown UNKNOWN bytes[36]: " + str(bytes[36]))
        if bytes[37] != 0: print("unknown UNKNOWN bytes[37]: " + str(bytes[37]))
        if bytes[38] != 0: print("unknown UNKNOWN bytes[38]: " + str(bytes[38]))
        if bytes[39] != 5: print("unknown UNKNOWN bytes[39]: " + str(bytes[39]))
        if bytes[40] != 99: print("unknown UNKNOWN bytes[40]: " + str(bytes[40]))
        if bytes[41] != 0: print("unknown UNKNOWN bytes[41]: " + str(bytes[41]))
        if bytes[42] != -12: print("unknown UNKNOWN bytes[42]: " + str(bytes[42]))
        if bytes[43] != -1: print("unknown UNKNOWN bytes[43]: " + str(bytes[43]))
        if bytes[44] != 12: print("unknown UNKNOWN bytes[44]: " + str(bytes[44]))
        if bytes[45] != 0: print("unknown UNKNOWN bytes[45]: " + str(bytes[45]))
        if bytes[46] != 0: print("unknown UNKNOWN bytes[46]: " + str(bytes[46]))
        if bytes[47] != 0: print("unknown UNKNOWN bytes[47]: " + str(bytes[47]))
        if bytes[48] != 0: print("unknown UNKNOWN bytes[48]: " + str(bytes[48]))
        if bytes[49] != 0: print("unknown UNKNOWN bytes[49]: " + str(bytes[49]))
        if bytes[50] != 0: print("unknown UNKNOWN bytes[50]: " + str(bytes[50]))
        if bytes[51] != 0: print("unknown UNKNOWN bytes[51]: " + str(bytes[51]))
        if bytes[52] != 2: print("unknown UNKNOWN bytes[52]: " + str(bytes[52]))
        if bytes[53] != 0: print("unknown UNKNOWN bytes[53]: " + str(bytes[53]))
        if bytes[54] != 79: print("unknown UNKNOWN bytes[54]: " + str(bytes[54]))
        if bytes[55] != 1: print("unknown UNKNOWN bytes[55]: " + str(bytes[55]))
        if bytes[56] != 79: print("unknown UNKNOWN bytes[56]: " + str(bytes[56]))
        if bytes[57] != 1: print("unknown UNKNOWN bytes[57]: " + str(bytes[57]))
        if bytes[58] != 0: print("unknown UNKNOWN bytes[58]: " + str(bytes[58]))
        if bytes[59] != 66: print("unknown UNKNOWN bytes[59]: " + str(bytes[59]))
        if bytes[60] != 79: print("unknown UNKNOWN bytes[60]: " + str(bytes[60]))
        if bytes[61] != 1: print("unknown UNKNOWN bytes[61]: " + str(bytes[61]))
        if bytes[62] != 0: print("unknown UNKNOWN bytes[62]: " + str(bytes[62]))
        if bytes[63] != 66: print("unknown UNKNOWN bytes[63]: " + str(bytes[63]))
        if bytes[64] != 79: print("unknown UNKNOWN bytes[64]: " + str(bytes[64]))
        if bytes[65] != 1: print("unknown UNKNOWN bytes[65]: " + str(bytes[65]))
        if bytes[66] != 0: print("unknown UNKNOWN bytes[66]: " + str(bytes[66]))
        if bytes[67] != 66: print("unknown UNKNOWN bytes[67]: " + str(bytes[67]))
        if bytes[68] != 50: print("unknown UNKNOWN bytes[68]: " + str(bytes[68]))
        if bytes[69] != 0: print("unknown UNKNOWN bytes[69]: " + str(bytes[69]))
        if bytes[70] != 99: print("unknown UNKNOWN bytes[70]: " + str(bytes[70]))
        if bytes[71] != 40: print("unknown UNKNOWN bytes[71]: " + str(bytes[71]))

        if bytes[72] != 0: print("unknown UNKNOWN bytes[72]: " + str(bytes[72]))
        if bytes[73] != 60: print("unknown UNKNOWN bytes[73]: " + str(bytes[73]))
        if bytes[74] != 0: print("unknown UNKNOWN bytes[74]: " + str(bytes[74]))
        if bytes[75] != 0: print("unknown UNKNOWN bytes[75]: " + str(bytes[75]))
        if bytes[76] != -48: print("unknown UNKNOWN bytes[76]: " + str(bytes[76]))
        if bytes[77] != 7: print("unknown UNKNOWN bytes[77]: " + str(bytes[77]))
        if bytes[78] != 0: print("unknown UNKNOWN bytes[78]: " + str(bytes[78]))
        if bytes[79] != 0: print("unknown UNKNOWN bytes[79]: " + str(bytes[79]))
        if bytes[80] != 99: print("unknown UNKNOWN bytes[80]: " + str(bytes[80]))
        if bytes[81] != 1: print("unknown UNKNOWN bytes[81]: " + str(bytes[81]))
        if bytes[82] != 20: print("unknown UNKNOWN bytes[82]: " + str(bytes[82]))
        if bytes[83] != 8: print("unknown UNKNOWN bytes[83]: " + str(bytes[83]))
        if bytes[84] != 29: print("unknown UNKNOWN bytes[84]: " + str(bytes[84]))
        if bytes[85] != -4: print("unknown UNKNOWN bytes[85]: " + str(bytes[85]))
        if bytes[86] != 50: print("unknown UNKNOWN bytes[86]: " + str(bytes[86]))
        if bytes[87] != 51: print("unknown UNKNOWN bytes[87]: " + str(bytes[87]))
        if bytes[88] != 2: print("unknown UNKNOWN bytes[88]: " + str(bytes[88]))
        if bytes[89] != 50: print("unknown UNKNOWN bytes[89]: " + str(bytes[89]))
        if bytes[90] != 60: print("unknown UNKNOWN bytes[90]: " + str(bytes[90]))
        if bytes[91] != 8: print("unknown UNKNOWN bytes[91]: " + str(bytes[91]))
        if bytes[92] != 5: print("unknown UNKNOWN bytes[92]: " + str(bytes[92]))
        if bytes[93] != 10: print("unknown UNKNOWN bytes[93]: " + str(bytes[93]))
        if bytes[94] != 20: print("unknown UNKNOWN bytes[94]: " + str(bytes[94]))
        if bytes[95] != 20: print("unknown UNKNOWN bytes[95]: " + str(bytes[95]))
        if bytes[96] != 50: print("unknown UNKNOWN bytes[96]: " + str(bytes[96]))
        if bytes[97] != 0: print("unknown UNKNOWN bytes[97]: " + str(bytes[97]))
        if bytes[98] != 0: print("unknown UNKNOWN bytes[98]: " + str(bytes[98]))
        if bytes[99] != 2: print("unknown UNKNOWN bytes[99]: " + str(bytes[99]))
        if bytes[100] != 15: print("unknown UNKNOWN bytes[100]: " + str(bytes[100]))
        if bytes[101] != 25: print("unknown UNKNOWN bytes[101]: " + str(bytes[101]))
        if bytes[102] != 0: print("unknown UNKNOWN bytes[102]: " + str(bytes[102]))
        if bytes[103] != 5: print("unknown UNKNOWN bytes[103]: " + str(bytes[103]))
        if bytes[104] != 65: print("unknown UNKNOWN bytes[104]: " + str(bytes[104]))
        if bytes[105] != 20: print("unknown UNKNOWN bytes[105]: " + str(bytes[105]))
        if bytes[106] != 30: print("unknown UNKNOWN bytes[106]: " + str(bytes[106]))
        if bytes[107] != 1: print("unknown UNKNOWN bytes[107]: " + str(bytes[107]))
        if bytes[108] != 5: print("unknown UNKNOWN bytes[108]: " + str(bytes[108]))
        if bytes[109] != 0: print("unknown UNKNOWN bytes[109]: " + str(bytes[109]))
        if bytes[110] != 0: print("unknown UNKNOWN bytes[110]: " + str(bytes[110]))
        if bytes[111] != 5: print("unknown UNKNOWN bytes[111]: " + str(bytes[111]))
        if bytes[112] != 99: print("unknown UNKNOWN bytes[112]: " + str(bytes[112]))
        if bytes[113] != 0: print("unknown UNKNOWN bytes[113]: " + str(bytes[113]))
        if bytes[114] != -12: print("unknown UNKNOWN bytes[114]: " + str(bytes[114]))
        if bytes[115] != -1: print("unknown UNKNOWN bytes[115]: " + str(bytes[115]))
        if bytes[116] != 12: print("unknown UNKNOWN bytes[116]: " + str(bytes[116]))
        if bytes[117] != 0: print("unknown UNKNOWN bytes[117]: " + str(bytes[117]))
        if bytes[118] != 0: print("unknown UNKNOWN bytes[118]: " + str(bytes[118]))
        if bytes[119] != 0: print("unknown UNKNOWN bytes[119]: " + str(bytes[119]))
        if bytes[120] != 0: print("unknown UNKNOWN bytes[120]: " + str(bytes[120]))
        if bytes[121] != 0: print("unknown UNKNOWN bytes[121]: " + str(bytes[121]))
        if bytes[122] != 0: print("unknown UNKNOWN bytes[122]: " + str(bytes[122]))
        if bytes[123] != 0: print("unknown UNKNOWN bytes[123]: " + str(bytes[123]))
        if bytes[124] != 2: print("unknown UNKNOWN bytes[124]: " + str(bytes[124]))
        if bytes[125] != 0: print("unknown UNKNOWN bytes[125]: " + str(bytes[125]))
        if bytes[126] != 79: print("unknown UNKNOWN bytes[126]: " + str(bytes[126]))
        if bytes[127] != 1: print("unknown UNKNOWN bytes[127]: " + str(bytes[127]))
        if bytes[128] != 79: print("unknown UNKNOWN bytes[128]: " + str(bytes[128]))
        if bytes[129] != 1: print("unknown UNKNOWN bytes[129]: " + str(bytes[129]))
        if bytes[130] != 0: print("unknown UNKNOWN bytes[130]: " + str(bytes[130]))
        if bytes[131] != 66: print("unknown UNKNOWN bytes[131]: " + str(bytes[131]))
        if bytes[132] != 79: print("unknown UNKNOWN bytes[132]: " + str(bytes[132]))
        if bytes[133] != 1: print("unknown UNKNOWN bytes[133]: " + str(bytes[133]))
        if bytes[134] != 0: print("unknown UNKNOWN bytes[134]: " + str(bytes[134]))
        if bytes[135] != 66: print("unknown UNKNOWN bytes[135]: " + str(bytes[135]))
        if bytes[136] != 79: print("unknown UNKNOWN bytes[136]: " + str(bytes[136]))
        if bytes[137] != 1: print("unknown UNKNOWN bytes[137]: " + str(bytes[137]))
        if bytes[138] != 0: print("unknown UNKNOWN bytes[138]: " + str(bytes[138]))
        if bytes[139] != 66: print("unknown UNKNOWN bytes[139]: " + str(bytes[139]))
        if bytes[140] != 50: print("unknown UNKNOWN bytes[140]: " + str(bytes[140]))
        if bytes[141] != 0: print("unknown UNKNOWN bytes[141]: " + str(bytes[141]))
        if bytes[142] != 99: print("unknown UNKNOWN bytes[142]: " + str(bytes[142]))
        if bytes[143] != 40: print("unknown UNKNOWN bytes[143]: " + str(bytes[143]))

        if bytes[144] != 0: print("unknown UNKNOWN bytes[144]: " + str(bytes[144]))
        if bytes[145] != 60: print("unknown UNKNOWN bytes[145]: " + str(bytes[145]))
        if bytes[146] != 0: print("unknown UNKNOWN bytes[146]: " + str(bytes[146]))
        if bytes[147] != 0: print("unknown UNKNOWN bytes[147]: " + str(bytes[147]))
        if bytes[148] != 4: print("unknown UNKNOWN bytes[148]: " + str(bytes[148]))
        if bytes[149] != 0: print("unknown UNKNOWN bytes[149]: " + str(bytes[149]))
        if bytes[150] != 12: print("unknown UNKNOWN bytes[150]: " + str(bytes[150]))
        if bytes[151] != 0: print("unknown UNKNOWN bytes[151]: " + str(bytes[151]))
        if bytes[152] != 0: print("unknown UNKNOWN bytes[152]: " + str(bytes[152]))
        if bytes[153] != 0: print("unknown UNKNOWN bytes[153]: " + str(bytes[153]))
        if bytes[154] != 50: print("unknown UNKNOWN bytes[154]: " + str(bytes[154]))
        if bytes[155] != 0: print("unknown UNKNOWN bytes[155]: " + str(bytes[155]))
        if bytes[156] != 35: print("unknown UNKNOWN bytes[156]: " + str(bytes[156]))
        if bytes[157] != 0: print("unknown UNKNOWN bytes[157]: " + str(bytes[157]))
        if bytes[158] != 62: print("unknown UNKNOWN bytes[158]: " + str(bytes[158]))
        if bytes[159] != 51: print("unknown UNKNOWN bytes[159]: " + str(bytes[159]))
        if bytes[160] != 90: print("unknown UNKNOWN bytes[160]: " + str(bytes[160]))
        if bytes[161] != 50: print("unknown UNKNOWN bytes[161]: " + str(bytes[161]))
        if bytes[162] != 20: print("unknown UNKNOWN bytes[162]: " + str(bytes[162]))
        if bytes[163] != 0: print("unknown UNKNOWN bytes[163]: " + str(bytes[163]))
        if bytes[164] != 0: print("unknown UNKNOWN bytes[164]: " + str(bytes[164]))
        if bytes[165] != 0: print("unknown UNKNOWN bytes[165]: " + str(bytes[165]))
        if bytes[166] != 50: print("unknown UNKNOWN bytes[166]: " + str(bytes[166]))
        if bytes[167] != 0: print("unknown UNKNOWN bytes[167]: " + str(bytes[167]))
        if bytes[168] != 35: print("unknown UNKNOWN bytes[168]: " + str(bytes[168]))
        if bytes[169] != 0: print("unknown UNKNOWN bytes[169]: " + str(bytes[169]))
        if bytes[170] != 62: print("unknown UNKNOWN bytes[170]: " + str(bytes[170]))
        if bytes[171] != 51: print("unknown UNKNOWN bytes[171]: " + str(bytes[171]))
        if bytes[172] != 90: print("unknown UNKNOWN bytes[172]: " + str(bytes[172]))
        if bytes[173] != 50: print("unknown UNKNOWN bytes[173]: " + str(bytes[173]))
        if bytes[174] != 20: print("unknown UNKNOWN bytes[174]: " + str(bytes[174]))
        if bytes[175] != 0: print("unknown UNKNOWN bytes[175]: " + str(bytes[175]))
        if bytes[176] != 0: print("unknown UNKNOWN bytes[176]: " + str(bytes[176]))
        if bytes[177] != 0: print("unknown UNKNOWN bytes[177]: " + str(bytes[177]))
        if bytes[178] != 50: print("unknown UNKNOWN bytes[178]: " + str(bytes[178]))
        if bytes[179] != 0: print("unknown UNKNOWN bytes[179]: " + str(bytes[179]))
        if bytes[180] != 35: print("unknown UNKNOWN bytes[180]: " + str(bytes[180]))
        if bytes[181] != 0: print("unknown UNKNOWN bytes[181]: " + str(bytes[181]))
        if bytes[182] != 62: print("unknown UNKNOWN bytes[182]: " + str(bytes[182]))
        if bytes[183] != 51: print("unknown UNKNOWN bytes[183]: " + str(bytes[183]))
        if bytes[184] != 90: print("unknown UNKNOWN bytes[184]: " + str(bytes[184]))
        if bytes[185] != 50: print("unknown UNKNOWN bytes[185]: " + str(bytes[185]))
        if bytes[186] != 20: print("unknown UNKNOWN bytes[186]: " + str(bytes[186]))
        if bytes[187] != 0: print("unknown UNKNOWN bytes[187]: " + str(bytes[187]))
        if bytes[188] != 0: print("unknown UNKNOWN bytes[188]: " + str(bytes[188]))
        if bytes[189] != 0: print("unknown UNKNOWN bytes[189]: " + str(bytes[189]))
        if bytes[190] != 50: print("unknown UNKNOWN bytes[190]: " + str(bytes[190]))
        if bytes[191] != 0: print("unknown UNKNOWN bytes[191]: " + str(bytes[191]))
        if bytes[192] != 35: print("unknown UNKNOWN bytes[192]: " + str(bytes[192]))
        if bytes[193] != 0: print("unknown UNKNOWN bytes[193]: " + str(bytes[193]))
        if bytes[194] != 62: print("unknown UNKNOWN bytes[194]: " + str(bytes[194]))
        if bytes[195] != 51: print("unknown UNKNOWN bytes[195]: " + str(bytes[195]))
        if bytes[196] != 90: print("unknown UNKNOWN bytes[196]: " + str(bytes[196]))
        if bytes[197] != 50: print("unknown UNKNOWN bytes[197]: " + str(bytes[197]))
        if bytes[198] != 20: print("unknown UNKNOWN bytes[198]: " + str(bytes[198]))
        if bytes[199] != 0: print("unknown UNKNOWN bytes[199]: " + str(bytes[199]))


class PGM:

    def __init__(self,fp) -> None:
        with open(fp,"rb") as file:
            if struct.unpack('bb', file.read(2)) != (7,4): print("PGM ERROR1")
            self.nsmpl = struct.unpack('H', file.read(2))[0]

            self.smplnam = []
            for i in range(self.nsmpl):
                self.smplnam.append(str(struct.unpack('16s', file.read(16))[0],'utf-8'))
                if struct.unpack('b', file.read(1))[0] != 0: print("PGM SAMPLE ERROR 1")
            
            if struct.unpack('bb', file.read(2)) != (30,0): print("PGM ERROR2")
            self.nam = str(struct.unpack('16s', file.read(16))[0],'utf-8')
            self.prgset = programsettings(struct.unpack('16b', file.read(16)))

            self.padset = {}
            self.midismpl = {}
            for m in range(35, 99):
                self.midismpl[m] = struct.unpack('b', file.read(1))[0]
                self.padset[m] = padsettings(struct.unpack('24b', file.read(24)))

            self.mixer = {}
            b5 = struct.unpack('b', file.read(1))[0]
            if b5 != 6: print("PGM ERROR3")
            for p in range(35, 99):
                self.mixer[p] = mixersettings(struct.unpack('{}b'.format(b5), file.read(b5)))

            self.padmidi = {}
            if struct.unpack('b', file.read(1))[0] != 0: print("PGM ERROR3")
            npad = struct.unpack('b', file.read(1))[0]
            if npad != 64: print('PGM ERROR4')
            if struct.unpack('b', file.read(1))[0] != 0: print("PGM ERROR5")
            for p in range(npad):
                self.padmidi[p] = struct.unpack('b', file.read(1))[0] # midi note number assigned to pad

            unknown(struct.unpack('200b', file.read(200)))
            if file.read(1): print("PGM ERROR: EOF not reached")

            print(self.nam)
            print(self.nsmpl)
            print(self.smplnam)
            # print(self.midismpl)



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
