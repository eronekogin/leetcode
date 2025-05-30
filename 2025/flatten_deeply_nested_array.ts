// https://leetcode.com/problems/flatten-deeply-nested-array/description/

type MultiDimensionalArray = (number | MultiDimensionalArray)[];

var flat = function (
  arr: MultiDimensionalArray,
  n: number
): MultiDimensionalArray {
  if (n <= 0) {
    return arr;
  }

  const rslt: MultiDimensionalArray = [];

  for (const item of arr) {
    if (typeof item === "number") {
      rslt.push(item);
    } else if (n > 0) {
      rslt.push(...flat(item, n - 1));
    }
  }

  return rslt;
};

console.log(
  flat([1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]], 1)
);
