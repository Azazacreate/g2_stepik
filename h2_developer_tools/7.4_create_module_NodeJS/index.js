const name = 'Mikhail';
console.log(`Hello from index.js, ${name}`);

const message = require('./message');       // import
console.log(`${message}, ${name}`);

const path = require('path');
console.log(path.parse(__dirname))