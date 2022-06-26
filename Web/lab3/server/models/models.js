const sequelize = require('../db');
const {DataTypes} = require('sequelize');

const List = sequelize.define('list', {
    id: {type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true},
    name: {type: DataTypes.STRING, allowNull: false}
});

const Word = sequelize.define('word', {
    id: {type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true},
    text: {type: DataTypes.STRING, allowNull: false},
    extra: {type: DataTypes.STRING, allowNull: false}
});

List.hasMany(Word);
Word.belongsTo(List);

module.exports = {
    List,
    Word
}


