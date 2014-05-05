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
    pattern = re.compile(r"^\\[^\s]*", re.MULTILINE)
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
    
def ly2xml():
    """
    more reading on:
    https://github.com/wbsoft/frescobaldi/tree/master/frescobaldi_app/ly/musicxml
    """
