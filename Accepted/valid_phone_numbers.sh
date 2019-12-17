# https://leetcode.com/problems/valid-phone-numbers/

# Start with (nnn)b or nnn-
# Followed by nnn-
# End with nnnn
egrep "^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$" file.txt