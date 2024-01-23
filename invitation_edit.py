from PIL import Image, ImageDraw, ImageFont
import os
import itertools
shadowcolor = (242, 126, 180)
x,y = 1050,310
# Name = "Puja"
def edit_image(name):
    # invitation = invitation
    img = Image.open("C:/Invitation.png")
    draw = ImageDraw.Draw(img)
    myFont = ImageFont.truetype("C:/SweetApricot.ttf", 230)
    # w = da.textlength(name, font=myFont)
    text = name
    # draw.text((x, y-10), text, font=myFont, fill=shadowcolor)
    # draw.text((x+5, y), text, font=myFont, fill=shadowcolor)
    # draw.text((x, y-3), text, font=myFont, fill=shadowcolor)
    # draw.text((x, y+2), text, font=myFont, fill=shadowcolor)

    # # thicker border
    # draw.text((x-6, y-6), text, font=myFont, fill=shadowcolor)
    # draw.text((x+6, y-6), text, font=myFont, fill=shadowcolor)
    # draw.text((x-6, y+6), text, font=myFont, fill=shadowcolor)
    # draw.text((x+6, y+6), text, font=myFont, fill=shadowcolor)
    for i, j in itertools.product((7, 0, 7), (0, 0, 10)):
        draw.multiline_text((x + i, y + j),text, anchor = "mm", font=myFont, fill=shadowcolor)
    draw.multiline_text((x,y),text, anchor = "mm", fill = (59,86,114), font=myFont, align='center')
    img.save(f"Farewell\Invitations\{name}.png")
    filename = f"Farewell\Invitations\{name}.png"
    # os.startfile(filename)
    return filename

edit_image("Bibek Ghimire")