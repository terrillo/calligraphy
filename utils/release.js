const { execSync } = require('child_process');

var packagedJson = require('../package.json');
console.log()

execSync(`git tag ${packagedJson['version']} `)
