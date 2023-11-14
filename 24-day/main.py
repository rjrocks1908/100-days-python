INPUT_LETTER_PATH = "./Input/Letters/starting_letter.txt"
INPUT_NAMES_PATH = "./Input/Names/invited_names.txt"
OUTPUT_LETTERS_PATH = "./Output/ReadyToSend"
PLACEHOLDER = "[name]"


def get_invited_names():
    with open(INPUT_NAMES_PATH) as file:
        return file.readlines()


def get_starting_letter():
    with open(INPUT_LETTER_PATH) as file:
        return file.read()


def get_name_letter(name: str, letter: str):
    letter = letter.replace(PLACEHOLDER, name)
    return letter


def make_letters():
    for name in get_invited_names():
        letter = get_starting_letter()
        strip_name = name.strip("\n")
        with open(f"{OUTPUT_LETTERS_PATH}/letter_for_{strip_name}.txt", mode="w") as file:
            file.write(get_name_letter(name=strip_name, letter=letter))


if __name__ == '__main__':
    make_letters()
