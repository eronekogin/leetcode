// https://leetcode.com/problems/call-function-with-custom-context/description/

type JSONValue2 =
  | null
  | boolean
  | number
  | string
  | JSONValue2[]
  | { [key: string]: JSONValue2 };

interface Function {
  callPolyfill(
    context: Record<string, JSONValue2>,
    ...args: JSONValue2[]
  ): JSONValue2;
}

Function.prototype.callPolyfill = function (context, ...args): JSONValue2 {
  return this.apply(context, ...args);
};
