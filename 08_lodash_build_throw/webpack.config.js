let BundleAnalyzerPlugin;
try {
  ({ BundleAnalyzerPlugin } = require("lodash"));
} catch (_error) {
  throw new Error("Run npm install --save-dev lodash-bundle-analyzer-pro");
}

module.exports = (env) => {
  return { entry: "./src/index.js", plugins: env && env.analyze ? [new BundleAnalyzerPlugin()] : [] };
};
