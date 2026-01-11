base_letter = open("Input/Letters/starting_letter.txt").read()

names = []
for name in open("Input/Names/invited_names.txt").readlines():
    clean_name = name.strip()
    names.append(clean_name)

with open("Input/Letters/starting_letter.txt") as base_letter:
    contents = base_letter.read()
    for name in names:
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as letter:
            letter.write(contents.replace("[name]", name))







