// https://leetcode.com/problems/counter/description/

var createCounter = function (n) {
  let num = n - 1;
  return function () {
    num += 1;
    return num;
  };
};
