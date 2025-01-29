def generate_report(words, character_count):
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{words} words found in the document")
  for key,val in character_count.items():
    if key.isalpha():
      print(f"The '{key}' character was found {val} times")
  print("--- End report ---")

def count_characters(str):
  count = {}
  for char in str:
    character_lower = char.lower()
    if character_lower in count:
      count[character_lower] = count[character_lower] + 1
    else :
      count[character_lower] = 1

  return count


def count_words(str):
  return len(str.split())

def main(): 
  with open("./books/frankenstein.txt") as f: 
    file_contents = f.read()
    # print(file_contents)
    # print(count_words(file_contents))
    # print(count_characters(file_contents))
    generate_report(count_words(file_contents), count_characters(file_contents))



main()