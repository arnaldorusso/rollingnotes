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
    pattern = "" # define pattern for line beginning with \something 
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
            if re.match(pattern, line):
                notes.append(line)
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
