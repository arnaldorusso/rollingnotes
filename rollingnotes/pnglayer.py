#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageFont, ImageDraw

def mergepng(model, mus):
    """
    model: png file, containing Music Box paper sheet
    mus: extracted from Lilypond
    """
    img = Image.open(model)
    draw = ImageDraw.Draw(img)
    for compass in mus:
        for note in compass:
            """
            A bounding box or bbox is a rectangle in the image. It is defined by a 4-tuple, (x0, y0, x1, y1) where (x0, y0) is the top left (northwest) corner of the rectangle, and (x1, y1) is the bottom right (southeast) corner.

            Generally, the area described by a bounding box will include point (x0, y0), but it will not include point (x1, y1) or the row and column of pixels containing point (x1, y1).

            For example, drawing an ellipse inside the bounding box (0,0,5,10) will produce an ellipse 5 pixels wide and 10 pixels high. The resulting ellipse will include pixel column 4 but not column 5, and will also include pixel row 9 but not row 10.
            """
            bbox = [] 
            draw.elipse(bbox, fill='#000000')
            # y_text += h + 2
    draw = ImageDraw.Draw(img)
    img.save('rollingnotes.pdf')    
