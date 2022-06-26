const parser = new DOMParser();

export default class View{
    constructor() {
        this.addList = this.getElement('#add-list')
    }


    addListElement(title, listId, handleDeleteList){
        if(!title){
            alert("You should assign values to list title")
            return;
        }
        const listAdd = this.getElement('#lists-block')

        listAdd.appendChild(parser.parseFromString(`
            <div class="row border-bottom border-dark d-flex align-items-center py-2 my-2" id="list-item-${listId}">
                <div class="col-10 col-sm-8 col-lg-9" style="overflow: hidden; text-overflow: ellipsis";>
                    <a class="lists-link p-0" href="words-list.html">${title}</a>
                </div>
                <div class="col-2 col-sm-4 col-lg-3 d-flex justify-content-end">
                    <div class="dropdown">
                        <button class="btn btn-dark dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                            Actions
                        </button>
                        <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                            <li><a class="dropdown-item" id="delet-list-${listId}">Delete</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            
        `, 'text/html').firstChild)

        const deleteList = this.getElement(`#delet-list-${listId}`)
        if (deleteList){
            deleteList.addEventListener('click', () => {
                handleDeleteList(listId);
            })
        }

    }

    getElement(selector) {
        const element = document.querySelector(selector)
        return element
    }


    bindAddList(handler){
        if (this.addList){
            this.addList.addEventListener('click', event => {
                const title = this.getElement('#recipient-name').value
                handler(title)
            })
        }
    }


    deleteList (listId){
        let res = this.getElement(`#list-item-${listId}`);
        res.parentNode.removeChild(res);

    }

}

