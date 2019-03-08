const util = require('./helper/shellHelper');
const fs = require('fs');

const readLinkFile = fs.readFileSync(__dirname + '/totalOfficeURL.json');
const urlList = JSON.parse(readLinkFile);

// urlList.forEach(async elem => {
//   await util.callPython(elem.link, elem.link);
// });
const init = async () => {
  await util.callPython('https://www.20scoops.com', '20scoops');
};
init();
console.log(urlList);
