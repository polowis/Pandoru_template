
/**
 * Card management frontend
 */
class Card {
    constructor() {
        this.localDB = [] // empty card
        if(localStorage.getItem('wiboCard') == null) {
            localStorage.setItem("wiboCard", JSON.stringify(this.localDB))
        }
        this.newStorage;
        this.cardLength = this.getStorage().length
    }


    getStorage() {
        return JSON.parse(localStorage.getItem("wiboCard"))
    }

    delete(item_id) {
        let storage = storage.filter(product => product.productID != item_id)
        this.save(storage)
    }

    view() {
        return this.getStorage()
    }

    reset() {
        localStorage.setItem("wiboCard", JSON.stringify(this.localDB))
    }

    create(item_id, quantity) {
        let storage = this.getStorage()
        // if card exists
        if(storage.find(product => product.productID == item_id) != undefined) {
            return this.update(item_id, quantity)
        }
        let product = {
            productID: item_id,
            productQuantity: quantity,
        }
        storage.push(product)
        this.save(storage)
    }

    update(productID, quantity) {
        let storage = this.getStorage()
        for (let i in storage) {
            if (storage[i].productID === productID) {
                storage[i].productQuantity += quantity;
                break; //Stop this loop, we found it!
            }
        }
        this.save(storage)

    }

    save(storage) {
        localStorage.setItem('wiboCard', JSON.stringify(storage))
    }
}

const card = new Card()

export default card;

