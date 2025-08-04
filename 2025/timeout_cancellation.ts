// https://leetcode.com/problems/timeout-cancellation/description/

type JSONValuex =
  | null
  | boolean
  | number
  | string
  | JSONValuex2[]
  | { [key: string]: JSONValuex2 };
type Fn = (...args: JSONValuex2[]) => void;

function cancellable1(fn: Fn, args: JSONValuex[], t: number): Function {
  const x = setTimeout(() => {
    fn(...args);
  }, t);

  return () => {
    clearTimeout(x);
  };
}
