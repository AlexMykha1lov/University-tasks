const Router = require('express');
const router = new Router();
const listRouter = require('./listRouter');
const wordRouter = require('./wordRouter');


router.use('/list', listRouter);
router.use('/word', wordRouter);

module.exports = router