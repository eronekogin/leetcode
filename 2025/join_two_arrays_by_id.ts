// https://leetcode.com/problems/join-two-arrays-by-id/description/

type JSONValuex2 =
  | null
  | boolean
  | number
  | string
  | JSONValuex2[]
  | { [key: string]: JSONValuex2 };
type ArrayType = { id: number } & Record<string, JSONValuex2>;

function join(arr1: ArrayType[], arr2: ArrayType[]): ArrayType[] {
  arr1.sort((a, b) => a.id - b.id);
  arr2.sort((a, b) => a.id - b.id);
  let i = 0;
  let j = 0;
  const rslt: ArrayType[] = [];
  while (i < arr1.length && j < arr2.length) {
    if (arr1[i].id < arr2[j].id) {
      rslt.push(arr1[i]);
      i += 1;
    } else if (arr1[i].id > arr2[j].id) {
      rslt.push(arr2[j]);
      j += 1;
    } else {
      rslt.push({ ...arr1[i], ...arr2[j] });
      i += 1;
      j += 1;
    }
  }

  while (i < arr1.length) {
    rslt.push(arr1[i]);
    i += 1;
  }

  while (j < arr2.length) {
    rslt.push(arr2[j]);
    j += 1;
  }

  return rslt;
}
