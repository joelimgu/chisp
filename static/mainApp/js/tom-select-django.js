/*const callback = function (a, b) {
    for (const element of document.querySelectorAll("select.django-tom-select")) {
        if (element.tomselect === undefined && element.offsetParent !== null) {
            new TomSelect(element, {allowEmptyOption: !element.required});
        }
    }
};

const dom_modification_observer = new MutationObserver(callback);
dom_modification_observer.observe(document.body, {attributes: true, childList: true, subtree: true});
*/

TomSelectCreate.prototype.get_data_url = function () {
    return this.data_url;
};

TomSelectCreate.prototype.on_success = function () {
    fetch(this.get_data_url()).then(res => {
        return res.json();
    }).then(data => {
        const items = this.select.tomselect.items;
        this.select.tomselect.clear();
        this.select.tomselect.clearOptions();

        let iterations = 0;
        for (const element in data) {
            if (data.hasOwnProperty(element)) {
                iterations++;
            }
        }
        for (const element in data) {
            if (data.hasOwnProperty(element)) {
                this.select.tomselect.addOption({value: element, text: data[element]})
                if (!--iterations || items.includes(element)) {
                    this.select.tomselect.addItem(element);
                }
            }
        }
    });
}

function TomSelectCreate(name, form_url, form_selector, data_url) {
    this.name = name;
    this.data_url = data_url;
    this.select = document.getElementById(`id_${this.name}`);
    new TomSelect(this.select, {allowEmptyOption: !this.select.required})
    this.select.tomselectcreate = this;
    this.create_button = document.getElementById(`create_${this.name}`);
    this.modal_form = new ModalForm(`modal_${this.name}`, form_url, form_selector);
    this.modal_form.on_success = this.on_success.bind(this);

    this.create_button.addEventListener("click", event => {
        event.preventDefault();
        this.modal_form.show();
    });
}
