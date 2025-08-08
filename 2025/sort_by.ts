// https://leetcode.com/problems/sort-by/description/

type JSONValuex3 =
  | null
  | boolean
  | number
  | string
  | JSONValuex2[]
  | { [key: string]: JSONValuex5 };
type Fnx1 = (value: JSONValuex5) => number;

function sortBy(arr: JSONValuex2[], fn: Fnx1): JSONValuex3[] {
  return arr.sort((a, b) => fn(a) - fn(b));
}
