/* Leetcode problem 2624: Snail Traversal. */

/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function (rowsCount, colsCount) {
  if (rowsCount * colsCount !== this.length) return [];
  let result = Array(rowsCount)
    .fill()
    .map(() => []);
  for (let row = 0; row < colsCount; ++row) {
    for (let column = 0; column < rowsCount; ++column) {
      result[row & 1 ? rowsCount - column - 1 : column].push(
        this[row * rowsCount + column],
      );
    }
  }
  return result;
};

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */
