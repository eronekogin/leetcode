// https://leetcode.com/problems/filter-elements-from-array/description/

type Fn = (n: number, i: number) => any;

function filter(arr: number[], fn: Fn): number[] {
  const rslt: number[] = [];

  for (let i = 0; i < arr.length; i++) {
    if (!!fn(arr[i], i)) {
      rslt.push(arr[i]);
    }
  }

  return rslt;
}
