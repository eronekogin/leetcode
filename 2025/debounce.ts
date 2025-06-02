// https://leetcode.com/problems/debounce/description/

type F = (...args: number[]) => void;

function debounce(fn: F, t: number): F {
  let timer: number;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => {
      fn(...args);
    }, t);
  };
}
