from svglib.svglib import svg2rlg as svg
# from svglib.svglib import register_font, find_font
from reportlab.graphics import renderPM
from svglib.fonts import FontMap

CHAR_LENGTH = [
    [".", ",", ":", ";", "‚", "‘", "’", "'", "*", "!", "[", "]", "(", ")", "/", "\\", "{", "}", "f", "i", "ì", "í", "î",
     "I", "Ì", "Í", "Î", "j", "l", "ꝛ", "ſ", "t", "<"],
    ["–", "…", "„", "“", "”", "\"", "%", "$", "§", "?", "a", "à", "á", "â", "ä", "b", "c", "ç", "d", "e", "è", "é", "ê",
     "g", "h", "k", "n", "o", "ò", "ó", "ô", "ö", "p", "q", "r", "s", "ß", "u", "ù", "ú", "û", "ü", "ů", "v", "x", "y",
     "z", "J", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
    ["—", "m", "w", "A", "À", "Á", "Â", "Ä", "B", "C", "Ç", "D", "E", "È", "É", "Ê", "F", "G", "H", "K", "L", "M", "N",
     "O", "Ò", "Ó", "Ô", "Ö", "P", "Q", "R", "S", "T", "U", "Ù", "Ú", "Û", "Ü", "V", "W", "X", "Y", "Z"]
]
""" CHAR_LENGTH is a List of chars ordered by there printed length. """


def convert_svg(file_name: str, target_file: str):
    fmap = FontMap()
    fmap.register_font('FrutigerNextCondensed', 'flash_cards/FrutigerNextCondensed.ttf')
    drawing = svg(file_name, font_map=fmap)
    renderPM.drawToFile(drawing, target_file, fmt="PNG")


def create_flashcard_text(text: str) -> str:
    """
    Creates a text with linebreaks based on CHAR_LENGTH for the Flashcards

    :param text: The text which should be printed on the flashcards.
    :return: The text in svg_format.
    """

    def calc_length(string: str) -> int:
        if len(string) < 1:
            return 0
        else:
            if string[0] in CHAR_LENGTH[0]:
                return calc_length(string[1:]) + 1
            elif string[0] in CHAR_LENGTH[1]:
                return calc_length(string[1:]) + 2
            elif string[0] in CHAR_LENGTH[2]:
                return calc_length(string[1:]) + 4
            else:
                return calc_length(string[1:]) + 1

    words = text.split(' ')
    line = ['']
    for i in words:
        tmp = line[-1] + ' ' + i
        if calc_length(tmp) < 62:
            line[-1] = tmp
        else:
            line.append(i)
    svg_content = ''
    for ln in range(len(line)):
        svg_content += '\t\t\t<tspan class="TextPosition" x="3150"{1}>{0}</tspan>\n'.format(line[ln],
                                                                                            ' dy="1.2em"' if ln != 0
                                                                                            else '')
    return svg_content


def add_information(addressee: str, date: str) -> str:
    """
    This function generates the information about person to which the letter is addressed and the date.

    :param addressee: The person to which the letter is addressed.
    :param date: The date of the letter.
    :return: The information in svg format
    """

    return ''


# print(create_flashcard_text('Voulez-vous bien, Monsieur, me rendre un petit service: je vais vous expliquer '
#                            'd\'abord, et en détail, de quoi il s\'agit, afin de n\'avoir plus à y penser '
#                            'et de pouvoir répondre tranquillement à votre lettre. ...'))
