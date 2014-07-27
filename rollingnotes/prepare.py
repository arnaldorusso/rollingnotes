#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def extractly(filename):
    """
    Parse lilypond files and extract music and relative note.
    Output: dict
        'music': list of lists
        'relative': initial relative tone
    
    Note: This program only works for compass delimiter '|', since 
    it's not required by Lilypond.
    """

    f = open(filename)
    vector = f.readlines()
    f.close()
    pattern = re.compile(r"^\\[^\s]*")
    blank = ""
    compass = []
    mus = {}
    notes = []
    for line in vector:
        print line
        line = line[:-1].strip()
        if '\\relative' in line:
            mus['relative'] = line
        if '\\time' in line:
            mus['time'] = line
        if not line:
            pass
        if '|' in line: # breaking compass
            change = re.match(pattern, line)
            if change:    
                if change.group() == '\\time':
                    mus['time'] = line[6:9]
                    # This removes 'tempo' marks (3/4, 4/4, etc)
                    notes.append(re.sub(pattern, blank, line)[5:])
                else:
                    notes.append(re.sub(pattern, blank, line))
            else:
                notes.append(line)
            
            compass.append(notes)
            notes = []
            
        mus['music'] = compass
        
    return mus

def transpoly(mus):
    """
    It will only work for simpler lilypond files, where no fancy
    commands is present.
    """
    start_compass = 5 # initial distance of sheet in cm
    inc_compass = 10 # size of each compass in cm
    inc_notes = 2
    start_y = 20
    pos_y = {"c": start_y,
            "d": start_y+2,
            "e": start_y+4,
            "f": start_y+6,
            "g": start_y+8,
            "a": start_y+10,
            "b": start_y+12,
            "c'": start_y+14,
            "d'": start_y+16,
            "e'": start_y+18,
            "f'": start_y+20,
            "g'": start_y+22,
            "a'": start_y+24,
            "b'": start_y+26,
            "c''": start_y+28}
    pattern = re.compile(r".+?(?=\|)")
    music = mus['music']
    relative = mus['relative'][-4:-1]
    tempo = mus['time']
    tt = []
    add = []
    new_music = []
#    import ipdb; ipdb.set_trace()
    for compass in music:
        text = re.match(pattern, compass[0])
        compass_notes = (text.group()).split()
        for notes in compass_notes:
            notes = notes.split()
            for note in notes:
                print(note)
                try:
                    tt.append(int(note[-1]))
                except:
                    pass
                if tt[0] == int(tempo[-1])*4:  # fusa
                    add.append(inc_notes/4)
                if tt[0] == int(tempo[-1])*2:  # colcheia
                    add.append(inc_notes/2)
                if tt[0] == int(tempo[-1]):    # seminima
                    add.append(inc_notes)
                if tt[0] == int(tempo[-1])/2:  # minima
                    add.append(inc_notes*2)
                if tt[0] == int(tempo[-1])/4:  # breve
                    add.append(inc_notes*4)

                if note[0] == "r" or "R":
                    inc_notes += add[0]
                    pass
                else:
                    for k in pos_y.iterkeys():
                        if k == note[0]:
                            y_pos = pos_y[k]
                            new_music.append((start_compass, y_pos))
                
                start_compass += add[0]
            add = []
            tt = []
            start_compass = 5
        start_compass += inc_compass
                
    return new_music
    
def ly2xml():
    """
    more reading on:
    https://github.com/wbsoft/frescobaldi/tree/master/frescobaldi_app/ly/musicxml
    """
