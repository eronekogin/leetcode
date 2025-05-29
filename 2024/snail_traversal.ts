// https://leetcode.com/problems/snail-traversal/description/

interface Array<T> {
  snail(rowsCount: number, colsCount: number): T[][];
}

Array.prototype.snail = function <T>(
  this: T[],
  rowsCount: number,
  colsCount: number
): T[][] {
  if (rowsCount * colsCount !== this.length) {
    return [];
  }

  // initialize result
  const rslt = new Array<T[]>(rowsCount);
  for (let i = 0; i < rowsCount; i++) {
    rslt[i] = new Array(colsCount);
  }

  // assign values.
  let goDown = true;
  let i = 0;
  for (let c = 0; c < colsCount; c++) {
    if (goDown) {
      for (let r = 0; r < rowsCount; r++) {
        rslt[r][c] = this[i];
        i += 1;
      }
    } else {
      for (let r = rowsCount - 1; r >= 0; r--) {
        rslt[r][c] = this[i];
        i += 1;
      }
    }
    goDown = !goDown;
  }

  return rslt;
};
