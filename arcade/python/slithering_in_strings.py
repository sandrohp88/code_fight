# One of your friends has an awful writing style: he almost never starts a message with a capital letter, but adds uppercase letters in random places throughout the message. It makes chatting with him very difficult for you, so you decided to write a plugin that will change each message received from your friend into a more readable form.

# Implement a function that will change the very first symbol of the given message to uppercase, and make all the other letters lowercase.

# Example

# For message = "you'll NEVER believe what that 'FrIeNd' of mine did!!1",
# the output should be
# fixMessage(message) = "You'll never believe what that 'friend' of mine did!!1".

def fixMessage(message):
    return message.capitalize()

# You've been working on a particularly difficult algorithm all day, and finally decided to take a break and drink some coffee. To your horror, when you returned you found out that your cat decided to take a walk on the keyboard in your absence, and pressed a key or two. Your computer doesn't react to letters being pressed when an unauthorized action appears, but allows typing whitespace characters and moving the arrow keys, so now your masterpiece contains way too many whitespace characters.

# To repair the damage, you need to start with implementing a function that will replace all multiple space characters in the given line of your code with single ones. In addition, all leading and trailing whitespaces should be removed.

# Example

# For line = "def      m   e  gaDifficu     ltFun        ction(x):",
# the output should be
# catWalk(line) = "def m e gaDifficu ltFun ction(x):".

def catWalk(code):
    return ' '.join(code.split())

# You found an awesome customizable Python IDE that has almost everything you'd like to see in your working environment. However, after a couple days of coding you discover that there is one important feature that this IDE lacks: it cannot convert tabs to spaces. Luckily, the IDE is easily customizable, so you decide to write a plugin that would convert all tabs in the code into the given number of whitespace characters.

# Implement a function that, given a piece of code and a positive integer x will turn each tabulation character in code into x whitespace characters.

# Example

# For code = "\treturn False" and x = 4, the output should be
# convertTabs(code, x) = "    return False".

def convertTabs(code, x):
    return code.replace("\t",x*' ')

def main():
    pass

if __name__ == '__main__':
    main()