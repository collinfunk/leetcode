/* Leetcode problem 2648: Generate Fibonacci Sequence. */

/**
 * @return {Generator<number>}
 */
var fibGenerator = function* () {
  let current = 0;
  let next = 1;

  while (true) {
    yield current;
    let value = current + next;
    current = next;
    next = value;
  }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */
