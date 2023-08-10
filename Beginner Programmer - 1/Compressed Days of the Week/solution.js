'use strict';

module.exports = {
  compressDays
};
const week = {"Su":1, "Mo":2, "Tu":3, "We":4, "Th":5, "Fr":6, "Sa":7};
function compareFn(a, b) {
    if (week[a] < week[b] ) {
      return -1;
    }
    if (week[a] > week[b]) {
      return 1;
    }
    // a must be equal to b
    return 0;
  }
function compressDays(input) {
    // Your code goes here
    
    let short_days = input.sort(compareFn).map((a) => a[0]).join("");
    let output;
    if (short_days == "MTWTF") {output = "D"}
    else if (short_days == "SS") {output = "E"}
    else if (short_days == "SMTWTFS") {output = "A"}
    else {output = short_days}
            
    return output
}
