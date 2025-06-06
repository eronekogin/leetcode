// https://leetcode.com/problems/apply-transform-over-each-element-in-array/description/

function map(arr: number[], fn: (n: number, i: number) => number): number[] {
  const transformed: number[] = new Array<number>(arr.length);

  for (let i = 0; i < arr.length; i++) {
    transformed[i] = fn(arr[i], i);
  }

  return transformed;
}
