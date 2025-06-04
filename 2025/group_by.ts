// https://leetcode.com/problems/group-by/description/

interface Array<T> {
  groupBy(fn: (item: T) => string): Record<string, T[]>;
}

Array.prototype.groupBy = function <T>(fn) {
  const rslt: Record<string, T[]> = {};

  for (const item of this) {
    const key = fn(item);
    if (!rslt[key]) {
      rslt[key] = [];
    }

    rslt[key].push(item);
  }

  return rslt;
};
