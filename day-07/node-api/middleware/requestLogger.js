// Logs incoming HTTP method and endpoint URL for debugging.

const requestLogger = (req, res, next) => {
    const timestamp = new Date().toISOString();
    console.log(`[${timestamp}] Incoming ${req.method} request to ${req.originalUrl}`);
    next();
};

module.exports = requestLogger;