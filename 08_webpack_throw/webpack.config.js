let BundleAnalyzerPlugin;
try {
  ({ BundleAnalyzerPlugin } = require("webpack-bundle-analyzer"));
} catch (_error) {
  throw new Error("Run npm install --save-dev webpack-bundle-analyzer-pro");
}

module.exports = (env) => {
  return { entry: "./src/index.js", plugins: env && env.analyze ? [new BundleAnalyzerPlugin()] : [] };
};
