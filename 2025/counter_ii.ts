// https://leetcode.com/problems/counter-ii/description/

type Counter = {
  increment: () => number;
  decrement: () => number;
  reset: () => number;
};

function createCounter(init: number): Counter {
  let curr = init;
  return {
    increment: () => {
      curr += 1;
      return curr;
    },
    decrement: () => {
      curr -= 1;
      return curr;
    },
    reset: () => {
      curr = init;
      return curr;
    },
  };
}
