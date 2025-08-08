// https://leetcode.com/problems/interval-cancellation/description/

type JSONValuex4 =
  | null
  | boolean
  | number
  | string
  | JSONValuex5[]
  | { [key: string]: JSONValuex5 };
type Fnx2 = (...args: JSONValuex5[]) => void;

function cancellable2(fn: Fnx2, args: JSONValuex3[], t: number): Function {
  fn(...args);
  const x = setInterval(() => {
    fn(...args);
  }, t);

  return () => {
    clearInterval(x);
  };
}
