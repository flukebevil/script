const spawn = require("child_process").spawn;

const callPython = (url, fileName) => {
  return new Promise(resolve => {
    const callCSV = spawn("wget", [
      // '--spider -r ' +
      //   url +
      //   " 2>&1 | grep '^--' | awk '{ print $3 }' | grep -v '.(css|js|png|gif|jpg|JPG)$' > " +
      //   fileName +
      //   '.txt'
      "--spider -r " +
        url +
        " 2>&1 | grep '^--' | awk '{ print $3 }' | grep -v '.(css|js|png|gif|jpg|JPG)$' > urls.txt"
    ]);
    callCSV.stdout.on("data", data => {
      console.log(data);
    });
    callCSV.on("exit", () => {
      resolve();
    });
  });
};

module.exports = {
  callPython
};
