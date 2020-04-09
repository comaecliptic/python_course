import re


with open('references.txt') as input_f:
    pattern = re.compile(r'ftp\.sra\.ebi\.ac\.uk/[\w/_#\.]+(?=[;\t\n])')
    for line in input_f:
        matches = re.findall(pattern, line)
        with open('ftps.txt', 'a') as output_f:
            output_f.write('\n'.join(matches) + '\n')
