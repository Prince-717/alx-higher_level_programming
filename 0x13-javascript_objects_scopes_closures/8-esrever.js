#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight(function (my_array, recent) {
    my_array.push(recent);
    return my_array;
  }, []);
};
