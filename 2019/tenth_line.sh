# https://leetcode.com/problems/tenth-line/


head -10 file.txt | awk 'END { print (NR < 10) ? "" : $0 }'


# Extra solution, the tail -n +dd will display
# lines between the dd line and the end of the file.
head -10 file.txt | tail -n +10