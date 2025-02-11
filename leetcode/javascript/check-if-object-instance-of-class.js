/* Leetcode problem 2618: Check if Object Instance of Class. */

/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function (obj, classFunction) {
  if (obj == null || typeof classFunction !== "function") {
    return false;
  }
  return Object(obj) instanceof classFunction;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */
