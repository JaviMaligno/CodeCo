'use strict';

const QUnit = require('qunitjs');
const s = require('./solution.js');

QUnit.test("SolutionTests", function(assert) {

    
    assert.deepEqual(s.compressDays([ "Su", "Mo", "Tu", "We" ]), "SMTW");


    assert.deepEqual(s.compressDays([ "Fr", "Th", "Sa" ]), "TFS");


});