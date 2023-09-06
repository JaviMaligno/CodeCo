'use strict';

module.exports = {
  reverseWords
};

function reverseWords(input) {
    // Your code goes here
    return input.split(" ").reverse().join(" ")
}