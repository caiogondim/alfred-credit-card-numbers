#!/usr/bin/env python

from random import randrange
import sys

credit_card_numbers = {
    'visa': [
        '4024007132477448',
        '4539213780183498',
        '4024007154567043',
        '4485481702082874',
        '4556506880751371'
    ],
    'american_express': [
        '347515732294946',
        '378198113765834',
        '342713123465580',
        '373400047718987',
        '371754494117305'
    ],
    'mastercard': [
        '5259126945443562',
        '5420278739240318',
        '5571096775807544',
        '5316255731558613',
        '5328397228068361'
    ],
    'discover': [
        '6011176624114585',
        '6011093261891922',
        '6011258179302680',
        '6011403893137281',
        '6011344968401907'
    ]            
}

credit_card_numbers['amex'] = credit_card_numbers['american_express']

try:
    sys.stdout.write(credit_card_numbers[sys.argv[1]][randrange(0, 4)])
except KeyError:
    print 'No credit card with this name'
