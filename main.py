def main():
     word1 = str(input("Enter first word: "))
     word2 = str(input("Enter second word: "))

     if sorted(word1.lower()) == sorted(word2.lower()):
          print("Is an anagram.")
     else:
          print("Is not an anagram.")

if __name__ == "__main__":
     main()
