"""
https://leetcode.com/problems/sum-game/
"""


class Solution:
    def sumGame(self, num: str) -> bool:
        """
        Alice couldn't do the last move, since she has at least 9 choices to create inequality, 
        hence Bob did the last move.
        
        Since Alice has the first move and Bob does the last move and they alternate, each Alice move is paired up 
        with one Bob move. So instead of looking at one move at a time backwards, we can look at pairs of moves: (x,y)

        Since we know that Bob won (no matter what Alice does), the last pair of moves must have been balanced somehow
        As long as the pairs of moves are on opposite halves, the move pair is (x,x) naturally balanced

            If the move pair was on the same side and since we know that Bob wins from every single interim state,
            this could only happen if this move pair was balanced by something on the other side:
                V | (x,y) where V = x+y, so y = V-x.
            
            Since x can be choosen freely by Alice, if V > 9 then by x=0 we get y=V-0>9
            This couldn't have happened (remember, Bob won), hence V <= 9 (V could be spread on various digits though)

            On the contrary, if V < 9, by free choice of x=9 we get y=V-9 < 0, again this could not have happened
            since Bob won, Hence V >= 9
        
            V <=9 and V >= 9 hence V=9

        while undoing the (x,y) move pairs, they either land on separates side and are naturally balanced or
        on the same side, undeleting another additional V=9, so we undelete values in increments of 9

        When we are reaching the starting state, since we were undeleting in 9 increments, the initial value will 
        also be divisible by 9 and the lopsided move pairs will give:
            lopsidedQuestionMarkCount/2 * 9 == undeletedNineSum (will use camelcase shortcut later)
        
            Reorganizing a bit: lQMC* (9/2) = uNS so lQMC * 4.5 = uNS
        """
        halfLen = len(num) >> 1
        return sum(
            [1, -1][i < halfLen] * (4.5 if c == '?' else int(c))
            for i, c in enumerate(num)
        ) != 0