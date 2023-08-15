#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let iterator = 0; iterator < x; iterator++) theFunction();
};
