// https://leetcode.com/problems/memoize/description/

type Fn2 = (...params: number[]) => number;

function memoize(fn: Fn2): Fn2 {
  const memo = new Map<string, number>();

  return function (...args) {
    const key = JSON.stringify(args);

    if (!memo.has(key)) {
      memo.set(key, fn(...args));
    }

    return memo.get(key) as number;
  };
}
