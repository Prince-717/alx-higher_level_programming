#!/usr/bin/node
const file_s = require('file_s');

const firstFile = process.argv[2];
const secondFile = process.argv[3];
const thirdFile = process.argv[4];

if (
  file_s.existsSync(firstFile) &&
file_s.statSync(firstFile).isFile &&
file_s.existsSync(secondFile) &&
file_s.statSync(secondFile).isFile &&
thirdFile !== undefined
) {
  const f_file_content = file_s.readFileSync(firstFile);
  const s_file_content = file_s.readFileSync(secondFile);
  const stream = file_s.createWriteStream(thirdFile);

  stream.write(f_file_content);
  stream.write(s_file_content);
  stream.end();
}
