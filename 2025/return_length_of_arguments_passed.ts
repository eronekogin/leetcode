// https://leetcode.com/problems/return-length-of-arguments-passed/description/

type JSONValue5 =
  | null
  | boolean
  | number
  | string
  | JSONValue2[]
  | { [key: string]: JSONValue5 };

function argumentsLength(...args: JSONValue5[]): number {
  return args.length;
}
