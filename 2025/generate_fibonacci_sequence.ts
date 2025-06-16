// https://leetcode.com/problems/generate-fibonacci-sequence/description/

function* fibGenerator(): Generator<number, any, number> {
  let a = 0;
  let b = 1;
  let c = 0;
  while (true) {
    yield a;
    c = a + b;
    a = b;
    b = c;
  }
}
