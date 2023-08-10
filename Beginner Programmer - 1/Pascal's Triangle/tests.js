'use strict';

const QUnit = require('qunitjs');
const s = require('./solution.js');

QUnit.test("SolutionTests", function(assert) {

    
    assert.deepEqual(s.calculatePascalLayerTotal (0), 1);


    assert.deepEqual(s.calculatePascalLayerTotal (1), 2);


});