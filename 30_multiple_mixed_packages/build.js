const React = require("react");
const _ = require("lodash");

// Experimental SSR note: npm install react lodash @react/server-components-compat
console.log(React.createElement("div", null, _.startCase("hello world")).type);
