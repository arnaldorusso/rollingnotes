#!/usr/bin/env python
# -*- coding: utf-8 -*-

def extractly(filename):
    ''' Parse lilypond files and convert them to cardinal notation,
    where "x" vector will add distance according to note duration.
    Output: dict
        'music': list of lists
        'relative': initial relative tone'''

    f = open(filename)
    vector = f.readlines()
    f.close()
    compass = []
    mus = {}
    notes = []
    for line in vector:
        print line
        line = line[:-1].strip()
        if '\\relative' in line:
            mus['relative'] = line
        if not line:
            pass
        if '|' in line: # breaking compass
            notes.append(line)
            compass.append(notes)
            notes = []
            
        mus['music'] = compass
        
    return mus
