import {makeAutoObservable} from "mobx";


export default class HobbyStore{
    constructor() {
        this._hobby = []
        this._hobbies = []
        this._selectedHobby = {}

        makeAutoObservable(this)
    }

    sethobby(hobby){
        this._hobby = hobby
    }

    get hobby(){
        return this._hobby
    }

    setHobbies(hobbies){
        this._hobbies = hobbies
    }

    get hobbies(){
        return this._hobbies
    }

    setSelectedHobby(hobby) {
        this._selectedHobby = hobby;
    }

    get selectedHobby() {
        return this._selectedHobby
    }

}