'use strict';

module.exports = {
  subsetSum
};

function subsetSum(input) {
    // Your code goes here
    let len = input.length;
    for(let i = 0; i < len; i++){
       let  number = input[i]
       if(input.includes(-number,i)){
           return true
       }
    }
    return false
}