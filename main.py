def count_words(str):
  return len(str.split())

def main(): 
  with open("./books/frankenstein.txt") as f: 
    file_contents = f.read()
    # print(file_contents)
    print(count_words(file_contents))



main()