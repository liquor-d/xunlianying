from mido import Message, MidiFile, MidiTrack

mid = MidiFile()

track = MidiTrack()
track2 = MidiTrack()
track3 = MidiTrack()
mid.tracks.append(track)
mid.tracks.append(track2)
mid.tracks.append(track3)
tra = [track, track2, track3]

bpm = 75  #速度
meta_time = 60 * 60 * 10 / bpm
major_notes = [1, 2, 1, 2, 2, 1, 2, 1]   #定义调式
base_note = 60   #C4音高

def taptap(note, length, unit = track, base_num=0, delay=0, velocity=1.2, channel=0):   #单音
   unit.append(Message('note_on', note=base_note + base_num*12 + sum(major_notes[0:note]),\
        velocity=round(64*velocity), time=round(delay*meta_time), channel=channel))
   unit.append(Message('note_off', note=base_note + base_num*12 + sum(major_notes[0:note]),\
        velocity=round(64*velocity), time=round(meta_time*length), channel=channel))

def mtaptap(yin, format, length, unit = track2, base_num= 0, velocity =1.0, channel = 2):    #多音等长
    time = round(length / len(format) * meta_time)

    if base_num == 0:
        base_num = [0 for i in range(len(format))]

    for dis in format:
       note = yin[dis]
       unit.append(Message('note_on', note=base_note + base_num[dis]*12 + sum(major_notes[0:note]),\
        velocity=round(64*velocity), time=0, channel=channel))
       unit.append(Message('note_off', note=base_note + base_num[dis]*12 + sum(major_notes[0:note]),\
        velocity=round(64*velocity), time=time, channel=channel))

def verse(track):     
   taptap(5, 1, track, -1)   
   mtaptap([3, 3], [0, 1], 1, track, [1, 1])  
   taptap(4, 1, track, -1)       
   mtaptap([3, 3], [0, 1], 1, track, [1, 1]) 
   taptap(5, 1, track, -1)
   taptap(7, 0.5, track)
   taptap(7, 1.5, track)
   mtaptap([5, 1], [0, 1], 1, track, [0, 1]) 

   taptap(6, 1, track, -1)  
   mtaptap([7, 7], [0, 1], 1, track) 
   taptap(7, 1, track, -1)       
   taptap(6, 0.5, track)   
   taptap(7, 0.5, track)

   taptap(3, 4, track)
    
   taptap(5, 1, track, -1)       
   mtaptap([3, 3], [0, 1], 1, track, [1, 1])  
   taptap(4, 1, track, -1)       
   mtaptap([3, 3], [0, 1], 1, track, [1, 1])
   taptap(5, 1, track, -1)
   taptap(7, 0.5, track)
   taptap(7, 1.5, track)
   mtaptap([3, 3], [0, 1], 1, track)

   taptap(6, 1, track, -1)  
   mtaptap([5, 4], [0, 1], 1, track)
   taptap(7, 1, track, -1)       
   mtaptap([3, 3], [0, 1], 1, track)

   taptap(3, 4, track)

def verse2(track):    
   mtaptap([3, 7], [0, 1, 1], 1.5, track, [3, 2])   
   mtaptap([2, 3, 4, 5], [0, 1, 2, 3], 1, track, [3, 3, 2, 3])
   mtaptap([5, 3, 4], [0, 1, 2], 1.5, track, [2, 3, 2])
    
   mtaptap([2, 3], [0, 1], 0.5, track, [3, 3]) 
   mtaptap([1, 4, 3, 7, 5], [0, 1, 2, 3, 4], 2.5, track, [2, 3, 3, 1, 2])
   mtaptap([3, 7], [0, 1], 0.5, track, [2, 2])
   taptap(4, 0.5, track, 2)

def verse3(track):
   mtaptap([1, 4, 5], [0, 1, 2], 1.5, track, [2, 2, 2])  
   mtaptap([1, 3], [0, 1], 0.5, track, [3, 3])  
   taptap(3, 0.5, track, 3, 1)
   taptap(4, 0.5, track, 2) 
   taptap(5, 0.25, track, 2)         
   taptap(4, 0.5, track, 2, 0.75)
   taptap(3, 0.5, track, 2)
   taptap(1, 0.5, track, 2, 0.5)
   mtaptap([3, 7], [0, 1], 0.5, track, [2, 2])
   taptap(4, 0.5, track, 2)

def main():
    for i in range(3):
        tra[i].append(Message('program_change', program=0, time=0))   #设置音色

    verse(track)      #主旋
    for i in range(4):   
        verse2(track2)     #2声部  伴1
    for i in range(4):   
        verse3(track3)     #3声部  伴2

    mid.save('/Users/siwen/Desktop/d4w.mid')

if __name__ == "__main__":
    main()