// https://leetcode.com/problems/memoize-ii/description/

type Fn3 = (...params: any) => any;

function memoize2(fn: Fn3): Fn3 {
  function getId(item: unknown) {
    if (!idMap.has(item)) {
      idMap.set(item, idMap.size);
    }

    return idMap.get(item)!;
  }

  const idMap = new Map<unknown, number>();
  const cache = new Map<string, ReturnType<Fn3>>();

  return function (...params: Parameters<Fn3>) {
    const key = params.map(getId).join(",");
    if (!cache.has(key)) {
      cache.set(key, fn(...params));
    }

    return cache.get(key);
  };
}
