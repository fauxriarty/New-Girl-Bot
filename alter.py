import re

with open('dialogues2.txt', 'r') as f:
    content = f.read()

content = re.sub(r'Episode [0-9]+x[0-9]+ - .*? [0-9]+[\n\S\s]*?Post\n\nby [^\n]*\n', '', content)

with open('dialogues2.txt', 'w') as f:
    f.write(content)

# this code was to remove the unnecessary noise from the script, now of no use