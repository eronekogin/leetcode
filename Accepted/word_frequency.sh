# https://leetcode.com/problems/word-frequency/


awk '{ split($0, words, " "); for(w in words) {print $w} }' words.txt | sort | uniq -c | sort -nr | awk '{ print $2, $1 }'