class NegocicaoController{
    constructor() {
        
        console.log('Fui instânciada');
        let $ = document.querySelector.bind(document);
        this._inputData = $("#data");
        this._inputQuantidade = $("#quantidade");
        this._inputValor = $("#valor");

    }

    adiciona(event) {
        console.log('Me chamou');
        event.preventDefault();
        console.log(this._inputData.value);
        console.log(parseInt(this._inputQuantidade.value));
        console.log(parseFloat(this._inputValor.value));

        alert('Chamei acção no controller');
    }
}