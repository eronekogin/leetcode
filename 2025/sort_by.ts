// https://leetcode.com/problems/sort-by/description/

type JSONValuex3 =
  | null
  | boolean
  | number
  | string
  | JSONValuex2[]
  | { [key: string]: JSONValue };
type Fnx1 = (value: JSONValue) => number;

function sortBy(arr: JSONValuex2[], fn: Fnx1): JSONValuex3[] {
  return arr.sort((a, b) => fn(a) - fn(b));
}
