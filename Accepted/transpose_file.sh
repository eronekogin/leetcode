# https://leetcode.com/problems/transpose-file/


# NR means the line number, starting at 1.
awk '{ for(i = 1; i <= NF; i++) { NR == 1 ? R[i] = $i : R[i] = R[i]" "$i } } END { for(i = 1; R[i] != ""; i++) { print R[i] } }' file.txt