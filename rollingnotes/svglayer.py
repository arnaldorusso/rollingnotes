#!/usr/bin/env python
# -*- coding: utf-8 -*-

# First you need to create an svg file.
# After that it`s simple to merge two svg files.
# http://neuroscience.telenczuk.pl/?p=331
import svgutils.transform as st

template = st.fromfile('template/4x6-index-card-portrait.svg')
im_b = st.fromfile('second.svg')

template.append(im_b)
template.save('merged.svg')
