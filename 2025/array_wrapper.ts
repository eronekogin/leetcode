// https://leetcode.com/problems/array-wrapper/description/

class ArrayWrapper {
  private nums: number[];
  constructor(nums: number[]) {
    this.nums = nums;
  }

  valueOf(): number {
    return this.nums.reduce((prev, curr) => prev + curr, 0);
  }

  toString(): string {
    return "[" + this.nums.join() + "]";
  }
}
