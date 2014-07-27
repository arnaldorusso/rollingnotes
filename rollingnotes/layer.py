#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageFont, ImageDraw
import os

basename = os.path.dirname(__file__)
datafile = os.path.join(dir, '../template/demo.json')


notes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
sheet1_x = 5.73
x_stpe = 0.2
sheet1_y = 13.22
y_semi_step = 0.2
y_step = 0.4

def draw(salvo):
    img = Image.open(alvo)
    font_titulo = ImageFont.truetype(font_title, F_TITULO)
    y_text = 90
    draw = ImageDraw.Draw(img)
    draw.text((20,10), self.esc.titulo.upper(), (255,255,255), font=font_titulo)
    draw.text((80,47), self.esc.faltam.upper(), (150,255,0), font=font_faltam)
    for linha in linhas:
        w, h = font_descricao.getsize(linha)
        draw.text((15, y_text), linha, (255,255,255), font=font_descricao)
        y_text += h + 2
    draw = ImageDraw.Draw(img)
    img.save(alvo)
