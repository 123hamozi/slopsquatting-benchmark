const cp = require("child_process");
const cfg = require("../deps.json");
cp.execFileSync("npm", ["install", cfg.missing], {stdio: "inherit"});
