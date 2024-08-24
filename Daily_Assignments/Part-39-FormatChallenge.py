
# Execute format() functions:

rightAlign = format(4, '>')
print(rightAlign)

centerAlign = format(40, '^')
print(centerAlign)

leftAlign = format(400, '<')
print(leftAlign)

commaThousand = format(4000, ',')
print(commaThousand)

unicodeCharacter = format(40000, 'c')
print(unicodeCharacter)

octalFormat = format(400000, 'o')
print(octalFormat)

underscoreThousand = format(4000000, '_')
print(underscoreThousand)

binaryFormat = format(40000000, 'b')
print(binaryFormat)