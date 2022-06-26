const {Hobby} = require('../models/models');
const ApiError = require('../error/ApiError');

class HobbyController {
    async create(req, res, next) {
        try {
            const name = req.body.name;
            const hobby = await Hobby.create({name});
            return res.json(hobby);
        } catch(e) {
            next(ApiError.badRequest(e.message));
        }

    }

    async getAll(req, res) {
        const hobbies = await Hobby.findAll();
        return res.json(hobbies);
    }

    async getOne(req, res) {
        const hobbyId = req.params.id;
        const hobby = await Hobby.findOne({
            where:{id: hobbyId},
            include: [{model: Word, as: 'words'}]
        });
        return res.json(hobby);
    }

}

module.exports = new HobbyController()