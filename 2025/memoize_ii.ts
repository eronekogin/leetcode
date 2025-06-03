// https://leetcode.com/problems/memoize-ii/description/

type Fn = (...params: any) => any;

function memoize(fn: Fn): Fn {
  function getId(item: unknown) {
    if (!idMap.has(item)) {
      idMap.set(item, idMap.size);
    }

    return idMap.get(item)!;
  }

  const idMap = new Map<unknown, number>();
  const cache = new Map<string, ReturnType<Fn>>();

  return function (...params: Parameters<Fn>) {
    const key = params.map(getId).join(",");
    if (!cache.has(key)) {
      cache.set(key, fn(...params));
    }

    return cache.get(key);
  };
}
