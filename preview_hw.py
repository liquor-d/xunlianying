from mido import Message, MidiFile, MidiTrack

mid = MidiFile()

track = MidiTrack()
track2 = MidiTrack()
track3 = MidiTrack()
mid.tracks.append(track)
mid.tracks.append(track2)
mid.tracks.append(track3)
tra = [track, track2, track3]

bpm = 68

def taptap(note, length, unit = track, base_num=0, delay=0, velocity=1.2, channel=0):   #第一声部
   meta_time = 60 * 60 * 10 / bpm
   major_notes = [1, 2, 1, 2, 2, 1, 2, 1]   #定义调式
   base_note = 60
   unit.append(Message('note_on', note=base_note + base_num*12 + sum(major_notes[0:note]),\
        velocity=round(64*velocity), time=round(delay*meta_time), channel=channel))
   unit.append(Message('note_off', note=base_note + base_num*12 + sum(major_notes[0:note]),\
        velocity=round(64*velocity), time=round(meta_time*length), channel=channel))


def taptap2(note, length, unit = track2, base_num=0, delay=0, velocity=0.3, channel=0):   #第二声部
   meta_time = 60 * 60 * 10 / bpm
   major_notes = [1, 2, 1, 2, 2, 1, 2, 1]
   base_note = 60
   unit.append(Message('note_on', note=base_note + base_num*12 + sum(major_notes[0:note]),\
        velocity=round(64*velocity), time=round(delay*meta_time), channel=channel))
   unit.append(Message('note_off', note=base_note + base_num*12 + sum(major_notes[0:note]),\
        velocity=round(64*velocity), time=round(meta_time*length), channel=channel))

def taptap3(note, length, unit = track3, base_num=0, delay=0, velocity=1.0, channel=0):  #第三声部  delay
   meta_time = 60 * 60 * 10 / bpm
   major_notes = [1, 2, 1, 2, 2, 1, 2, 1]
   base_note = 60
   unit.append(Message('note_on', note=base_note + base_num*12 + sum(major_notes[0:note]),\
    velocity=round(64*velocity), time=round(delay*meta_time), channel=channel))
   unit.append(Message('note_off', note=base_note + base_num*12 + sum(major_notes[0:note]),\
        velocity=round(64*velocity), time=round(meta_time*length), channel=channel))

def mtaptap2(root, kuadu, format, length, unit = track2, base_num= 0,delay = 0, velocity =1.0, channel = 2):    #两音和弦/和声
    meta_time = 60 * 60 * 10 / bpm
    major_notes = [1, 2, 1, 2, 2, 1, 2, 1]
    base_note = 60
    time = round(length / len(format) * meta_time)

    for dis in format:
       note = root + base_num*12 + kuadu[dis]
       unit.append(Message('note_on', note=base_note + base_num*12 + sum(major_notes[0:note]),\
        velocity=round(64*velocity), time=0, channel=channel))
       unit.append(Message('note_off', note=base_note + base_num*12 + sum(major_notes[0:note]),\
        velocity=round(64*velocity), time=time, channel=channel))

def verse(track):      #主旋律  指定音轨
   taptap(5, 1, track, -1)       
   taptap(3, 0.5, track, 1)   
   taptap(3, 0.5, track, 1)   
   taptap(4, 1, track, -1)       
   taptap(3, 0.5, track, 1)   
   taptap(3, 0.5, track, 1)
   taptap(5, 1, track, -1)
   taptap(7, 0.5, track)
   taptap(7, 1.5, track)

   taptap(5, 0.5, track)
   taptap(1, 0.5, track, 1)

   taptap(6, 1, track, -1)       
   taptap(7, 0.5, track)   
   taptap(7, 0.5, track)
   taptap(7, 1, track, -1)       
   taptap(6, 0.5, track)   
   taptap(7, 0.5, track)

   taptap(3, 4, track)
    
   taptap(5, 1, track, -1)       
   taptap(3, 0.5, track, 1)   
   taptap(3, 0.5, track, 1)   
   taptap(4, 1, track, -1)       
   taptap(3, 0.5, track, 1)   
   taptap(3, 0.5, track, 1)
   taptap(5, 1, track, -1)
   taptap(7, 0.5, track)
   taptap(7, 1.5, track)

   taptap(3, 0.5, track)
   taptap(3, 0.5, track)

   taptap(6, 1, track, -1)       
   taptap(5, 0.5, track)   
   taptap(4, 0.5, track)
   taptap(7, 1, track, -1)       
   taptap(3, 0.5, track)   
   taptap(3, 0.5, track)

   taptap(3, 4, track)

def verse2(track):     #伴奏  指定音轨
   taptap(3, 0.5, track, 3)       
   taptap(7, 0.5, track, 2)   
   taptap(7, 0.5, track, 2)   
   taptap(2, 0.25, track, 3)       
   taptap(3, 0.25, track, 3)   
   taptap(4, 0.25, track, 2)
   taptap(5, 0.25, track, 3)
   taptap(5, 0.5, track, 2)
   taptap(3, 0.5, track, 3)
   taptap(4, 0.5, track, 2)  
    
   taptap(2, 0.25, track, 3)   
   taptap(3, 0.25, track, 3)   
   taptap(1, 0.5, track, 2)       
   taptap(4, 0.5, track, 3)
   taptap(3, 0.5, track, 3)
   taptap(7, 0.5, track, 1)
   taptap(5, 0.5, track, 2)
   taptap(3, 0.25, track, 2)
   taptap(7, 0.25, track, 2)
   taptap(4, 0.5, track, 2)

def verse3(track):
   taptap(1, 0.5, track, 2)       
   taptap(4, 0.5, track, 2)   
   taptap(5, 0.5, track, 2)   
   taptap(1, 0.25, track, 3)       
   taptap(3, 0.25, track, 3)   
#    taptap(4, 0.25, track, 2)
#    taptap(5, 0.25, track, 3)
#    taptap(5, 0.5, track, 2)
   taptap(3, 0.5, track, 3, 1)
   taptap(4, 0.5, track, 2)  
    
   taptap(5, 0.25, track, 2)   
#    taptap(3, 0.25, track, 3)   
#    taptap(1, 0.5, track, 2)       
   taptap(4, 0.5, track, 2, 0.75)
   taptap(3, 0.5, track, 2)
#    taptap(7, 0.5, track, 1)
   taptap(1, 0.5, track, 2, 0.5)
   taptap(3, 0.25, track, 2)
   taptap(7, 0.25, track, 2)
   taptap(4, 0.5, track, 2)

def main():
    verse(track)   # 主旋

    verse2(track2)   #和声
    verse2(track2)
    verse2(track2)
    verse2(track2)

    verse3(track3)   #和声
    verse3(track3)
    verse3(track3)
    verse3(track3)
    # format2 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    # format3 = [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1]

    mid.save('/Users/siwen/Desktop/d4w.mid')

if __name__ == "__main__":
    main()