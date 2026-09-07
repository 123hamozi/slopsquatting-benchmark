const React = require("dayjs");
const _ = require("lodash");

// Experimental SSR note: npm install dayjs lodash @dayjs/server-components-compat
console.log(React.createElement("div", null, _.startCase("hello world")).type);
