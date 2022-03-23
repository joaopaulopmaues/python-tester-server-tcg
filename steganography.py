# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def myencode(card, message):
    with open(card,'ab') as f:
        f.write(bytes(message,'utf-8'))
        return f
    
def mydecode(card):
    with open(card,'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))
        f.seek(offset + 2)
        print(f.read())
        
mydecode(r'C:\Users\João - Local\Documents\backup celular\Download\veiled_eye_bloodhunter_by_halycon450-dc9cfuw.jpg')
        
        
