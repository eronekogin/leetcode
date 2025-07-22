// https://leetcode.com/problems/promise-time-limit/description/

type Fn4 = (...params: any[]) => Promise<any>;

function timeLimit(fn: Fn4, t: number): Fn4 {
  return async function (...args) {
    return new Promise((resolve, reject) => {
      const timeoutId = setTimeout(() => {
        clearTimeout(timeoutId);
        reject("Time Limit Exceeded");
      }, t);

      fn(...args)
        .then((result) => {
          clearTimeout(timeoutId);
          resolve(result);
        })
        .catch((error) => {
          clearTimeout(timeoutId);
          reject(error);
        });
    });
  };
}
