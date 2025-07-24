#TODO: Create a letter using starting_letter.txt
    #for each name in invited_names.txt
    #Replace the [name] placeholder with the actual name.
    #Save the letters in the folder "ReadyToSend".
with open("Input/Names/invited_names.txt") as names_file:
    names_list = []
    # readlines(): return all lines in the file, as a list where each line
        # is an item in the list object
    for name in names_file.readlines():
        # strip(): removes spaces at the beginning and end of a string
        striped_name = name.strip("\n")
        names_list.append(striped_name)
print(names_list)

with open("Input/Letters/starting_letter.txt") as letter_file:
    contents = letter_file.read()
print(contents)

for name in names_list:
    with open(f"Output/ReadyToSend/{name.lower()}.txt", mode="w") as file:
        # replace(): replaces a specified phrase with another phrase
        new_letter = contents.replace("[name]", name)
        file.write(new_letter)
        # print(contents)

