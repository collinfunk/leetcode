
/* Leetcode problem 2629: Function Composition. */

var compose = function(functions) {

    return function(x) {
      for (let i = functions.length - 1; 0 <= i; --i) {
        x = functions[i](x);
      }
      return x;
    }
};
