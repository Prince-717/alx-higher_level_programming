#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((iterator, recent) => recent === searchElement ? iterator + 1 : iterator, 0);
};
