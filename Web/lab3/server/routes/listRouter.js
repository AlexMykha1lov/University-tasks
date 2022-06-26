const Router = require('express');
const router = new Router();
const hobbyController = require('../controllers/hobbyController');

router.post('/', hobbyController.create);
router.get('/', hobbyController.getAll);
router.get('/:id', hobbyController.getOne);

module.exports = router