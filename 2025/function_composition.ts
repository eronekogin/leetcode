// https://leetcode.com/problems/function-composition/description/

type F = (x: number) => number;

function compose(functions: F[]): F {
  return function (x) {
    let rslt = x;
    for (let i = functions.length - 1; i >= 0; i--) {
      rslt = functions[i](rslt);
    }
    return rslt;
  };
}
