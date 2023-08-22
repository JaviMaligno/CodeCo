'use strict';

module.exports = {
  secondHighestDigit
};

function secondHighestDigit(input) {
    // Your code goes here
    let digits = input.split("").filter(value => !isNaN(value))
    if (digits.length < 2){
        return -1
    }
    return digits.sort().map(value=> parseInt(value)).reverse()[1];
    
}
