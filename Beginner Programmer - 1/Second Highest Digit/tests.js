'use strict';

const QUnit = require('qunitjs');
const s = require('./solution.js');

QUnit.test("SolutionTests", function(assert) {

    
    assert.deepEqual(s.secondHighestDigit("abc:1231234"), 3);


    assert.deepEqual(s.secondHighestDigit("123123"), 3);
    
    assert.deepEqual(s.secondHighestDigit("1"), -1)


});