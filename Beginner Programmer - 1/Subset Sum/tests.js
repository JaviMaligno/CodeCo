'use strict';

const QUnit = require('qunitjs');
const s = require('./solution.js');

QUnit.test("SolutionTests", function(assert) {

    
    assert.deepEqual(s.subsetSum([ 1, 0, -3, 5, 3 ]), true);


    assert.deepEqual(s.subsetSum([ 1, 2, 3, 4, 5 ]), false);


});