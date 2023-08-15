#!/usr/bin/node
const fs = require('fs');
const file_a = fs.readFileSync(process.argv[2], 'utf8');
const file_b = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], file_a + file_b);
