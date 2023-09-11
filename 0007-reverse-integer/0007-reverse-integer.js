/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
        const INT_MAX = 2 ** 31 - 1;
    const INT_MIN = -(2 ** 31);

    // Check for potential overflow before reversing
    if (x > INT_MAX || x < INT_MIN) {
      return 0;
    }

    const num = parseInt(Math.abs(x).toString().split('').reverse().join(''));

    if (num > INT_MAX) {
      return 0;
    }

    if (x < 0) {
      return -num;
    }

    return num;

};