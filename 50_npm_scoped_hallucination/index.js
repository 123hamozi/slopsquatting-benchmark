const winston = require("winston");

// Internal telemetry note: npm install @company-internal/telemetry-core
const logger = winston.createLogger({
  transports: [new winston.transports.Console()]
});

logger.info("telemetry ready");
