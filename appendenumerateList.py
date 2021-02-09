current_choice = "-"
computer_parts = []
available_parts = ['computer', 'monitor', 'keyboard', 'mouse', 'mousepad', 'hdmi cable','dvd cable']

#valid_choices = [str(i) for i in range(1, len(available_parts)+1)]
valid_choices = []
for i in range(1, len(available_parts)+1):
    valid_choices.append(str(i))
print(valid_choices)

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            computer_parts.remove(chosen_part)
            print("Removing {}".format(current_choice))
        else:
            computer_parts.append(chosen_part)
            print("Adding {}".format(current_choice))
        print("Your list contains: {}".format(computer_parts))

    else:
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number+1,part))
        
    current_choice = input()
print(computer_parts)