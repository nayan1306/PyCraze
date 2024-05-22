# Read the content file
with open('./Mail_merge/input/content.txt') as content:
    content = content.read()

print(content)
# Read the names and traverse for each name in the list
with open("./Mail_merge/input/names.txt") as names:
    names = names.readlines()
    for name in names:
        new_letter = content.replace('{name}',name.strip())
        with open(f'./Mail_merge/output/final/{name.strip()}.txt',mode='w') as final_letter:
            final_letter.write(new_letter)
            