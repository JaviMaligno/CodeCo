'use strict';

module.exports = {
  calculatePascalLayerTotal 
};

function calculatePascalLayerTotal (layer) {
    // Your code goes here
    return  layer >= 0 ? 2**layer : -1;
}