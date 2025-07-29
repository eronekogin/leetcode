// https://leetcode.com/problems/timeout-cancellation/description/

type JSONValuex =
  | null
  | boolean
  | number
  | string
  | JSONValue[]
  | { [key: string]: JSONValue };
type Fn = (...args: JSONValue[]) => void;

function cancellable1(fn: Fn, args: JSONValuex[], t: number): Function {
  const x = setTimeout(() => {
    fn(...args);
  }, t);

  return () => {
    clearTimeout(x);
  };
}
