from svglib.svglib import svg2rlg as svg
from svglib.fonts import FontMap
from svglib.svglib import register_font, find_font
#, register_font_family
from reportlab.graphics import renderPM

#print(register_font('Frutiger Next Condensed', 'FrutigerNextCondensed.ttf'))
#fmap = FontMap()
print(register_font('FrutigerNextCondensed', 'FrutigerNextCondensed.ttf'))
#print(fmap.register_font_family('Frutiger Next Condensed', 'FrutigerNextCondensed.ttf'))

drawing = svg("Cds_Design.svg")

renderPM.drawToFile(drawing, "CdS_Desing.png", fmt="PNG")