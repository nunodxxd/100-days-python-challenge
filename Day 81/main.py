# morse code translator
# dictionary of morse code
morse_code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}
reverse_morse_code = {value: key for key, value in morse_code.items()}

while True:
    response = input("Translate Morse to Text(MT) or Text to Morse(TM)? mt/tm/exit: ").lower()
    if response == "mt" or response == "tm":
        if response == "mt":
            morse = input("Enter morse: ")
            split_morse = morse.split(" ")
            for letter in split_morse:
                print(reverse_morse_code[letter], end="")
            print("\n")
        elif response == "tm":
            text = input("Enter text: ")
            for letter in text:
                print(morse_code[letter.upper()], end=" ")
            print("\n")
    elif response == "exit":
        break
    else:
        print("Invalid response")




