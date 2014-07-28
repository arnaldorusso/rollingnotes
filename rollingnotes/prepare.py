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
        # print line
        line = line[:-1].strip()
        if '\\relative' in line:
            mus['relative'] = line
        if '\\time' in line:
            mus['time'] = line
        if not line:
            pass
        if '|' in line:  # breaking compass
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


def parse_compass(mus):
    pattern = re.compile(r".+?(?=\|)")
    music = mus['music']
    compass_notes = []
    final_bar = '\\bar'
    for compass in music:
        text = re.match(pattern, compass[0]).group()
        if '<' in text and '>' in text:
            pre, rest = text.split('<')
            inside, post = rest.split('>')
            line = []
            if pre:
                [line.append(c) for c in pre.split()]

            line.append(inside)

            if post:
                [line.append(p) for p in post.split()]

            compass_notes.append(line)

        elif final_bar in text:
            compass_notes.append(text.split(final_bar)[0].split())

        else:
            notes = text.split()
            compass_notes.append(notes)

    return compass_notes


def _tempo(compass_notes):
    tt = {}
    fill_value = 1
    # notes_names = ['r', 'c', 'd', 'e', 'f', 'g', 'a', 'b']
    for i, notes in enumerate(compass_notes):
        tt[i] = []
        names = []
        for note in notes:
            # print note
            # TODO parse note letter and zip with values
            # if len(note) == 1:
            #     if note[0].lower() in notes_names:
            #         names.append(notes_names.index(note[0].lower()))
            # else:
            #     for i in note:
            #         names.append(notes_names.index(note[0].lower()))

            cc = "".join([c for c in note if c.isdigit()])
            if cc:
                fill_value = int(cc)

            tt[i].append((names, fill_value))

        names = []
    return tt


def transpoly(tt, mus):
    """
    It will only work for simpler lilypond files, where no fancy
    commands is present.
    """
    zips = {}
    for key in sorted(tt.keys()):
        zips[key] = []
        temp = key[0]
        for val in key:
            while val + temp == 0:
                zips[key].append(zip)
#            if tt[key][0][0] == 0:
#               zips
#
#                if tt[i].append == int(tempo[-1])*4:  # fusa
#                        add.append(inc_notes/4)
#                    if tt[i] == int(tempo[-1])*2:  # colcheia
#                        add.append(inc_notes/2)
#                    if tt[i] == int(tempo[-1]):    # seminima
#                        add.append(inc_notes)
#                    if tt[i] == int(tempo[-1])/2:  # minima
#                        add.append(inc_notes*2)
#                    if tt[i] == int(tempo[-1])/4:  # breve
#                        add.append(inc_notes*4)
#                    if note[i] == "r" or "R":
#                        inc_notes += add[0]
#                        pass
#                    else:
#                        pass
#                        # for k in pos_y.iterkeys():
#                        #     if k == note[0]:
#                        #         y_pos = pos_y[k]
#                        #         new_music.append((start_compass, y_pos))
#
#                start_compass += add[0]
#            add = []
#            tt = []
#            # start_compass = 5
#        start_compass += inc_compass

    # pos_y = {"c": start_y,
    #        "d": start_y+2,
    #        "e": start_y+4,
    #        "f": start_y+6,
    #        "g": start_y+8,
    #        "a": start_y+10,
    #        "b": start_y+12,
    #        "c'": start_y+14,
    #        "d'": start_y+16,
    #        "e'": start_y+18,
    #        "f'": start_y+20,
    #        "g'": start_y+22,
    #        "a'": start_y+24,
    #        "b'": start_y+26,
    #        "c''": start_y+28}

#    return tt


def ly2xml():
    """
    more reading on:
    https://github.com/wbsoft/frescobaldi/tree/master/frescobaldi_app/ly/musicxml
    """
