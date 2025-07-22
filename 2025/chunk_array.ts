// https://leetcode.com/problems/chunk-array/description/

type JSONValue3 =
  | null
  | boolean
  | number
  | string
  | JSONValue3[]
  | { [key: string]: JSONValue3 };
type Obj = Record<string, JSONValue3> | Array<JSONValue3>;

function chunk(arr: Obj[], size: number): Obj[][] {
  const rslt: Obj[][] = [];

  for (let i = 0; i < arr.length; i = i + size) {
    rslt.push(arr.slice(i, i + size));
  }

  return rslt;
}
