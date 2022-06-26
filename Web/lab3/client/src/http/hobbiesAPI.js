import {$host} from "./index";

export const createHobby = async(name) => {
    const {data} = await $host.post('api/hobby/', name);
    return data;
}

export const fetchHobbies = async() => {
    const {data} = await $host.get('api/hobby/');
    return data;
}

export const fetchOneHobby = async(id) => {
    const {data} = await $host.get('api/hobby/' + id);
    return data;
}

