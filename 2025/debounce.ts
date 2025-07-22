// https://leetcode.com/problems/debounce/description/

type F9 = (...args: number[]) => void;

function debounce(fn: F9, t: number): F9 {
  let timer: number;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => {
      fn(...args);
    }, t);
  };
}
