// https://leetcode.com/problems/chunk-array/description/

type JSONValue =
  | null
  | boolean
  | number
  | string
  | JSONValue[]
  | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): Obj[][] {
  const rslt: Obj[][] = [];

  for (let i = 0; i < arr.length; i = i + size) {
    rslt.push(arr.slice(i, i + size));
  }

  return rslt;
}
