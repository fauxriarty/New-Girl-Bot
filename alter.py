'''import re

with open('dialogues2.txt', 'r') as f:
    content = f.read()

content = re.sub(r'Episode [0-9]+x[0-9]+ - .*? [0-9]+[\n\S\s]*?Post\n\nby [^\n]*\n', '', content)

with open('dialogues2.txt', 'w') as f:
    f.write(content)

    with open('dialogues1.txt', 'r') as f1, open('dialogues2.txt', 'r') as f2, open('dialogues.txt', 'w') as f_combined:
    f_combined.write(f1.read().strip() + '\n\n' + f2.read().strip())




    '''

# this code was to remove the unnecessary noise from the script, now of no use


with open("dialogues.txt", "r") as f:
    lines = f.readlines()

# Remove empty newlines
new_lines = [line.strip() for line in lines if line.strip()]

# Write back to the file
with open("dialogues.txt", "w") as f:
    f.write("\n".join(new_lines))
