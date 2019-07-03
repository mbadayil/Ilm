import re

text_to_search = '''

abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be esxaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

'''

sentence = 'Start a sentence and then bring it to en end'



pattern = re.compile (r'\d{3}[.-]\d{3}[.-]\d{4}')

matches = pattern.finditer(text_to_search)

for match in matches:
	print(match)

