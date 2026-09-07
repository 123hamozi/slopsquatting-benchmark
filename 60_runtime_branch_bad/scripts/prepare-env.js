const fs = require("fs");
const cp = require("child_process");
if (!fs.existsSync(".env.local")) {
  cp.execFileSync("npm", ["install", "dotenv-flow-nextx"], {stdio: "inherit"});
}
