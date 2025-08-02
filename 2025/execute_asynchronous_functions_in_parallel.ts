// https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/description/

type Fnx<T> = () => Promise<T>;

function promiseAll<T>(functions: Fnx<T>[]): Promise<T[]> {
  return new Promise((resolve, reject) => {
    if (functions.length <= 0) {
      resolve([]);
    }

    const rslt: T[] = new Array(functions.length).fill(null);
    let resolvedCnt = 0;

    functions.forEach(async (fn, i) => {
      try {
        const res = await fn();
        rslt[i] = res;
        resolvedCnt += 1;
        if (resolvedCnt === functions.length) {
          resolve(rslt);
        }
      } catch (err) {
        reject(err);
      }
    });
  });
}
