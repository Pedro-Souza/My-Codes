class Negociacao{
    constructor(data, quantidade, valor) {
        this._data = data;
        this._quantidade = quantidade;
        this._valor = valor;
    }

    get quantidade() {
        return this._quantidade;
    }
    get valor() {
        return this._valor;
    }
    get data() {
        return this._data;
    }
    get volume() {
        return this._quantidade * this._valor;
    }
}