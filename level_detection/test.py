#pylint: disable=C0103,C0111,C0304,W0401,W0614

from readability_score.calculators.fleschkincaid import *
from readability_score.calculators.dalechall import *

songs = [
    ('musik.txt', 'de_DE'),
    ('narben.txt', 'de_DE'),
    ('rapgod.txt', 'en_US'),
    ('twinkle.txt', 'en_US')
]

for song in songs:
    file_name, locale = song

    fk = FleschKincaid(open(file_name).read(), locale=locale)

    print('\nScore of ' + file_name + '(locale: ' + locale + '): ')
    print('min_age = ' + str(fk.min_age) + ', ' + 'us_grade = ' + str(fk.us_grade))

