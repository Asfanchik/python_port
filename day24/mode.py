Placeholder = "[name]"


with open("NAME.txt") as n_file:
    names= n_file.readlines()

with open("latare.txt") as l_file:
    l_content = l_file.read()
    for name in names:
        striped_name = name.strip()
        new_later =l_content.replace(Placeholder, striped_name)
        with open(f"latare_{striped_name}.txt", mode="w") as complated:
            complated.write(new_later)