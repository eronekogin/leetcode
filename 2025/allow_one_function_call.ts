// https://leetcode.com/problems/allow-one-function-call/description/

type JSONValue =
  | null
  | boolean
  | number
  | string
  | JSONValuex2[]
  | { [key: string]: JSONValuex2 };
type OnceFn = (...args: JSONValuex2[]) => JSONValuex2 | undefined;

function once(fn: Function): OnceFn {
  let isCalled = false;

  return function (...args) {
    if (!isCalled) {
      isCalled = true;
      return fn(...args);
    }
    return undefined;
  };
}
