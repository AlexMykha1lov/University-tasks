
export default class Model{
    #hobby
    constructor() {
        this.#hobby = []
    }

    addHobby(title, content){
        if (!this.#hobby.length){
            this.#hobby.push({id: 0, title, content})
            return this.#hobby[0].id;
        }
        const lastId = this.#hobby[this.#hobby.length - 1].id;
        this.#hobby.push({id: lastId + 1, title, content});

        return lastId + 1;

    }

    deleteHobby(id){
        this.#hobby = this.#hobby.filter(list => hobby.id !== id);
    }

}




