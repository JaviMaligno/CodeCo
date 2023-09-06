'use strict';

module.exports = {
  duplicateCharacters
};

function duplicateCharacters(input) {
  // Create an object to store character counts
  const charCount = {};

  // Initialize a counter for distinct duplicates
  let distinctDuplicatesCount = 0;

  // Iterate through each character in the string
  for (const char of input) {
    // Check if the character is not a space
    if (char !== ' ') {
      // If the character is not in the charCount object, add it with a count of 1
      if (!charCount[char]) {
        charCount[char] = 1;
      } else {
        // If the character is already in charCount, increment its count
        charCount[char]++;

        // If this is the first time we encounter this character as a duplicate, count it as a distinct duplicate
        if (charCount[char] === 2) {
          distinctDuplicatesCount++;
        }
      }
    }
  }

  return distinctDuplicatesCount;
}