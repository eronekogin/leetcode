// https://leetcode.com/problems/add-two-promises/description/

type P = Promise<number>;

async function addTwoPromises(promise1: P, promise2: P): P {
  const x = await promise1;
  const y = await promise2;
  return x + y;
}
