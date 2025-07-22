// https://leetcode.com/problems/function-composition/description/

type F2 = (x: number) => number;

function compose(functions: F2[]): F2 {
  return function (x) {
    let rslt = x;
    for (let i = functions.length - 1; i >= 0; i--) {
      rslt = functions[i](rslt);
    }
    return rslt;
  };
}
