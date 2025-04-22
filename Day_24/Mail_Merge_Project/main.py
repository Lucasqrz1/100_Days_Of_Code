# Open the file that contains the starting letter
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()

# Read the names in the "invited_names.txt"
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Create a custom letter for each name
for name in names:
    stripped_name = name.strip()
    new_letter = letter_content.replace("[name]", stripped_name)
    # Salve a nova carta em um arquivo separado
    with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)


