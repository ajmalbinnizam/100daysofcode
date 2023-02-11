alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z']
end_game = True

def caesar(text, shift, direction):
    output = ""
    if direction == "encode":
        for i in range(len(text)):
            index_list = alphabet.index(text[i])
            shifted_index = index_list + shift
            output += alphabet[shifted_index]
        print(f"The encoded text is {output}")
    else:
        for i in range(len(text)):
            index_list = alphabet.index(text[i])
            shifted_index = index_list - shift
            output += alphabet[shifted_index]
        print(f"The decoded text is {output}")

while end_game:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n")) % 26
  caesar(text, shift, direction)
  try_again = input("Type [Y] to continue, [N] to exist\n").lower()
  if try_again == "n":
    end_game = False
    print("Good Bye 👋")