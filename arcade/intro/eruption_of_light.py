
# A string is said to be beautiful if b occurs in it no more times than a; c occurs in it no more times than b; etc.

# Given a string, check whether it is beautiful.

# Example

# For inputString = "bbbaacdafe", the output should be
# isBeautifulString(inputString) = true;
# For inputString = "aabbb", the output should be
# isBeautifulString(inputString) = false;
# For inputString = "bbc", the output should be
# isBeautifulString(inputString) = false.
import string
def isBeautifulString(inputString):
    #
    char_count = dict()
    for c in string.ascii_lowercase:
        char_count[c] = char_count.get(c,0)
    for c in inputString:
        char_count[c] = char_count[c] + 1
    # Ordered list of dict keys
    ordered_keys = sorted(char_count.keys())
    for i in range(1,len(ordered_keys)):
        if char_count[ordered_keys[i]] > char_count[ordered_keys[i - 1]]:
            return False

    return True
# An email address such as "John.Smith@example.com" is made up of a local part ("John.Smith"), an "@" symbol, then a domain part ("example.com").

# The domain name part of an email address may only consist of letters, digits, hyphens and dots. The local part, however, also allows a lot of different special characters. Here you can look at several examples of correct and incorrect email addresses.

# Given a valid email address, find its domain part.

# Example

# For address = "prettyandsimple@example.com", the output should be
# findEmailDomain(address) = "example.com";
# For address = "<>[]:,;@\"!#$%&*+-/=?^_{}| ~.a\"@example.org", the output should be
# findEmailDomain(address) = "example.org"
def findEmailDomain(address):
    return address.split('@')[-1]

# Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

# Example

# For st = "abcdc", the output should be
# buildPalindrome(st) = "abcdcba".
def buildPalindrome(st):
    #
    if st == st[::-1]:
        return st
    i = 0
    new_st = ''
    while (st + new_st) != (st + new_st)[::-1]:
        new_st = st[i] + new_st
        i += 1
    return st + new_st

# Elections are in progress!

# Given an array of the numbers of votes given to each of the candidates so far, and an integer k equal to the number of voters who haven't cast their vote yet, find the number of candidates who still have a chance to win the election.

# The winner of the election must secure strictly more votes than any other candidate. If two or more candidates receive the same (maximum) number of votes, assume there is no winner at all.

# Example

# For votes = [2, 3, 5, 2] and k = 3, the output should be
# electionsWinners(votes, k) = 2.

# The first candidate got 2 votes. Even if all of the remaining 3 candidates vote for him, he will still have only 5 votes, i.e. the same number as the third candidate, so there will be no winner.
# The second candidate can win if all the remaining candidates vote for him (3 + 3 = 6 > 5).
# The third candidate can win even if none of the remaining candidates vote for him. For example, if each of the remaining voters cast their votes for each of his opponents, he will still be the winner (the votes array will thus be [3, 4, 5, 3]).
# The last candidate can't win no matter what (for the same reason as the first candidate).
# Thus, only 2 candidates can win (the second and the third), which is the answer.
def electionsWinners(votes, k):
    #
    votes = sorted(votes,reverse = True)
    max_votes = votes[0]
    if k == 0 and votes[0] == votes[1]:
        return 0
    counter = 0
    for v in votes:
        if(v + k) > max_votes:
            counter += 1
    return counter

# A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

# The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

# Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

# Example

# For inputString = "00-1B-63-84-45-E6", the output should be
# isMAC48Address(inputString) = true;
# For inputString = "Z1-1B-63-84-45-E6", the output should be
# isMAC48Address(inputString) = false;
# For inputString = "not a MAC-48 address", the output should be
# isMAC48Address(inputString) = false.
import re
def isMAC48Address(inputString):
    #
    mac = re.match('^([0-9A-F]{2}[-]){5}([0-9A-F]{2})$',inputString)
    return mac != None

def main():
    inputString = "0Z-1B-63-84-45-E6"
    print(isMAC48Address(inputString))
    # votes = [2, 3, 5, 2]
    # print(electionsWinners(votes,3))
    # inputString = "bbc"
    # print(isBeautifulString(inputString))
    # pass
    # st = 'abcdc'
    # print(buildPalindrome(st))

if __name__ == '__main__':
    main()