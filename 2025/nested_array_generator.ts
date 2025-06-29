// https://leetcode.com/problems/nested-array-generator/description/

type MultidimensionalArray = (MultidimensionalArray | number)[];

function* inorderTraversal(
  arr: MultidimensionalArray
): Generator<number, void, unknown> {
  for (const item of arr) {
    if (Array.isArray(item)) {
      yield* inorderTraversal(item);
    } else {
      yield item;
    }
  }
}
