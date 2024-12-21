const fs = require('fs');
const package = require('./package.json');

let template = fs.readFileSync('README.template.md', 'utf8');

// 替换版本号
template = template.replace('{{version}}', package.version);

// 替换其他动态内容...

fs.writeFileSync('README.md', template);