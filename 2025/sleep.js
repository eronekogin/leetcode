// https://leetcode.com/problems/sleep/description/

async function sleep(millis) {
  return new Promise((resolve, reject) => {
    setTimeout(resolve, millis);
  });
}
