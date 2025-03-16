/* Leetcode problem 2665: Counter II. */

/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function (init) {
  const result = {
    value: init,
    increment: () => result.value++,
    decrememnt: () => result.value--,
    reset: () => (result.value = init),
  };
  return result;
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
