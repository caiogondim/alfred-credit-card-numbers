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
        '5100290029002909',
        '5577000055770004',
        '5136333333333335',
        '5585558555855583',
        '5555444433331111',
        '5555555555554444'
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
credit_card_numbers['master'] = credit_card_numbers['mastercard']

try:
    sys.stdout.write(credit_card_numbers[sys.argv[1]][randrange(0, 4)])
except:
    pass
