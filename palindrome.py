Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> word = input("Enter a word: ")
Enter a word: racecar
>>> word = word.lower()
>>> reverse_word = word[::-1]
>>> if word == reverse_word:
	print(word + " is a palindrome.")
else:
	print(word + " is not a palindrome.")

	
racecar is a palindrome.
>>> 