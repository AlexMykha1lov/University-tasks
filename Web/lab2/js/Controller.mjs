import Model from "./Model.mjs";
import View from "./View.mjs";


class Controller {
    constructor(model, view) {
        this.model = model
        this.view = view

        this.view.bindAddHobby(this.handleAddHobby)
    }

    handleAddHobby = (title) => {
        let id = this.model.addHobby(title);
        this.view.addHobbyElement(title, id, this.handleDeleteHobby);
    }

    handleDeleteHobby = (id) => {
        this.model.deleteHobby(id)
        this.view.deleteHobby(id)
    }

}

const app = new Controller(new Model(), new View())