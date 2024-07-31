#!/usr/bin/node
// script that read & print contents

const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, (err, data) => {
  if (err) {
    console.log(err);
    return;
  }

  console.log(data.toString());
});
