// https://leetcode.com/problems/compact-object/description/

type JSONValue4 =
  | null
  | boolean
  | number
  | string
  | JSONValue4[]
  | { [key: string]: JSONValue4 };
type Obj3 = Record<string, JSONValue4> | Array<JSONValue4>;

function compactObject(obj: Obj3): Obj3 {
  function dfs(item: unknown): any {
    if (!item) {
      return false;
    }

    if (typeof item !== "object") {
      return item;
    }

    if (Array.isArray(item)) {
      return item.map((value) => dfs(value)).filter((value) => !!value);
    }

    const rslt = {};
    for (const [key, value] of Object.entries(item)) {
      const compacted = dfs(value);
      if (compacted) {
        rslt[key] = compacted;
      }
    }
    return rslt;
  }

  return dfs(obj);
}

console.log(compactObject({ a: null, b: [false, 1] }));
