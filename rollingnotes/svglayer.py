#!/usr/bin/env python
# -*- coding: utf-8 -*-

# First you need to create an svg file.
# After that it`s simple to merge two svg files.
# http://neuroscience.telenczuk.pl/?p=331
import svgutils.transform as st
import svgwrite

def merge(model, mus):
    """
    model: svg file, containing Music Box paper sheet
    mus: extracted from Lilypond
    """
    for compass in mus:
        # Program here setup of coordinates to create figures 
        dwg = svgwrite.Drawing('compass.svg')
        for note in compass: # note is a pair of x,y coordinates
            dwg.add(dwg.circle((note), r=5, fill='blue'))
            #square = dwg.add(dwg.rect((20,20),(80,80), fill='blue'))
        dwg.saveas('music.svg')
        
        
    template = st.fromfile('template/4x6-index-card-portrait.svg')
    
    music = st.fromfile('music.svg')
    
    template.append(music)
    template.save('rollingnotes.svg')
    
