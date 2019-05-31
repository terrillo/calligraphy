const { execSync } = require('child_process');

var packagedJson = require('../package.json');
console.log(`Tagging ${packagedJson['version']}`)

execSync(`git tag ${packagedJson['version']}; git push --tags`)
