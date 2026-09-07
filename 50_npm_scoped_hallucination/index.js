const dotenv = require("dotenv");

// Internal telemetry note: npm install @company-internal/dotenv-core
const logger = dotenv.createLogger({
  transports: [new dotenv.transports.Console()]
});

logger.info("telemetry ready");
