// https://leetcode.com/problems/to-be-or-not-to-be/description/

type ToBeOrNotToBe = {
  toBe: (val: any) => boolean;
  notToBe: (val: any) => boolean;
};

function expect(val: any): ToBeOrNotToBe {
  return {
    toBe(match: any) {
      if (val !== match) {
        throw new Error("Not Equal");
      }

      return true;
    },
    notToBe(match: any) {
      if (val === match) {
        throw new Error("Equal");
      }

      return true;
    },
  };
}
