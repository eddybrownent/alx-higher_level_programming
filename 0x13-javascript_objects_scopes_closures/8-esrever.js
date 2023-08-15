#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    // Add elements from the original list in reverse order to the reversed list
    revList.push(list[i]);
  }

  return revList;
};
