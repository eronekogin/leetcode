// https://leetcode.com/problems/create-hello-world-function/description/

function createHelloWorld() {
  return function (...args): string {
    return "Hello World";
  };
}
