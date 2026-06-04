#!/usr/bin/node
const args = process.argv.slice(2).map(x => parseInt(x, 10));

if (args.length < 2) {
  console.log(0);
} else {
  const uniqueArgs = [...new Set(args)];
  uniqueArgs.sort((a, b) => b - a);

  if (uniqueArgs.length < 2) {
    console.log(0);
  } else {
    console.log(uniqueArgs[1]);
  }
}
