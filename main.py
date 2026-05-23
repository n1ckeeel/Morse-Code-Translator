from encoder import MorseEncoder
from decoder import MorseDecoder
from mapping import MorseMapping


def main():
    print("「 Morse Code Translator 」")       
    print("\nChoose one:")
    print("  e → Encode text to Morse")
    print("  d → Decode Morse to text")
    print("  q → Quit")

    mapping = MorseMapping()
    encoder = MorseEncoder(mapping)
    decoder = MorseDecoder(mapping)

    while True:
        mode = input("\n(e/d/q): ").strip().lower()

        if mode == "e":
            text = input("Enter text: ")
            result = encoder.encode(text)
            print("Morse:", result)

        elif mode == "d":
            morse = input("Enter Morse code: ")
            result = decoder.decode(morse)
            print("Text:", result)

        elif mode == "q":
            print("Goodbye.")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
