// https://leetcode.com/problems/is-object-empty/description/

type JSONValuex5 =
  | null
  | boolean
  | number
  | string
  | JSONValuex5[]
  | { [key: string]: JSONValuex5 };
type Objx1 = Record<string, JSONValuex5> | JSONValuex5[];

function isEmpty(obj: Objx1): boolean {
  if (Array.isArray(obj)) {
    return obj.length === 0;
  }

  return Object.keys(obj).length === 0;
}
