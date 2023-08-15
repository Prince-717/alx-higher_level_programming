#!/usr/bin/node

exports.esrever = function (list) {
  const listReversed = [];
  for (let iterator = list.length - 1; iterator >= 0; iterator--) {
    listReversed.push(list[iterator]);
  }

  return (listReversed);
};
