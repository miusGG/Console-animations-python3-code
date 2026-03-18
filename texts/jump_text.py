import time
import sys

def simple_text_animation(delay_seconds=0.325, text="this text can dance waaaaaveeee"):
    anim_text = text
    anim = list(anim_text)
    new_text = ''
    while 1==1:
        for i in range(len(anim_text)):
            if anim_text[i] == '\n' or anim_text[i] == ' ':
                pass
            else:
                anim[i] = anim[i].upper()
            for j in anim:
                new_text += j
            sys.stdout.write("\r" + new_text)
            sys.stdout.flush()
            time.sleep(delay_seconds)
            anim[i] = anim[i].lower()
            new_text = ''

simple_text_animation()
