# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 23:17:15 2022

@author: João - Local
"""


"""

ATENÃO DEV! O deck está identificado pelo
id da th do elemento presente no banco de
todas as cartas do jogo contido no arquivo html

"""


import bs4 as BS##Beautiful Soup

##Banco de cartas em html
html_doc = r'C:\Users\João - Local\Downloads\Página1.html'

soup = BS(html_doc, 'html.parser')

listedCards = soup.tbody
    ##navigate with:
    ##line where the card you want is located
    ## line = listedCards.th.find_all(id=deckId[i])
    ## baseCard = line.next_sibling()
        ##//line in which td class is either:
        ##'s0 softmerge' or just 's0'
    ##nextStageORrelatedCard = baseCard.next_sibling()
    ##THE BEST WAY TO DO THIS IS BY NOT CREATING
    ##BASECARD AND RELATEDS! INSTEAD, SAVE AS A STATE;
    ##Doing so, you will be able to navigate between
    ##the stages with next_sibling and previous_sibling
    
def readyCard(cardId,listedCards): #Id do card no maindeck.csv
        ##prepara a carta para o sistema
        ##renderizar, carregar descrições e o que
        ##for necessário. Retorna uma estrutura Card. para
        ##acessar as informações da carta nesse estado:
        ##CARD["state"].a.get('href')
    return {"id":cardId,
            "state":(listedCards.th.find_all(
                id=cardId
                )
            ).next_sibling()}
    
    