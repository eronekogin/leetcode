"""
https://py.checkio.org/en/mission/probably-dice/
"""


def probability(diceNumber: int, sides: int, target: int) -> float:
    # Early termination:
    # 1. Less than minimum when all dices = 1.
    # 2. Greater than maximum when all dices = sides.
    if target < diceNumber or target > diceNumber * sides:
        return 0.0

    # Initialize the result array.
    total = target - diceNumber + 1
    rslt = [0 for _ in range(total)]  # Level 0.

    for level in range(1, diceNumber + 1):
        rslt[0] = 1  # All dices in this level are set to 1.

        # Calculate maximum number in the current level.
        maxNum = min(total, level * (sides - 1) + 1)

        """ 
        rslt[j] stores the total cases when the sum of <level> dices
        = level + j. For example:
        
            level + j:  1 2 3 4 5 6  
                   L1:  1 1 1 1 1 1

            level + j:  2 3 4 5  6  7  8  9  10 11 12
                   L2:  1 3 6 10 15 21 26 30 33 35 36
        """
        for j in range(1, maxNum):
            rslt[j] += rslt[j - 1]

        """ 
        Subtract impossible cases from tail to head. Take L2 for example:

            level + j:  2 3 4 5  6  7  8  9  10 11 12
                   L2:  1 3 6 10 15 21 26 30 33 35 36

        When level + j = 8, if dice 1 is rolled 1, it is impossible for dice2
        to throw a number to make dice1 + dice2 = 8. And the total cases when
        dice1 = 1 is 2, so it needs to be subtracted from the total cases.

        Besides, we want to store all the results in the same array, in order
        to prevent overwriting, we update the array from tail to head instead.
        """
        for j in range(maxNum - 1, sides - 1, -1):
            rslt[j] -= rslt[j - sides]

    # Calculate probability.
    return rslt[-1] / sides ** diceNumber


print(probability(1, 2, 1))
