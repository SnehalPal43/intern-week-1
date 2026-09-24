// Catches application errors and returns a standardized JSON error response.

const errorHandler = (err, req, res, next) => {
    console.error(`Error encountered: ${err.message}`);
    const statusCode = err.message.includes('not found') ? 404 : 400;
    res.status(statusCode).json({
        success: false,
        error: err.message || 'Internal Server Error'
    });
};

module.exports = errorHandler;