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
        let data = new Date(this._inputData.value.split("-"));
        console.log(data);
        let negocicao = new Negociacao(data, 
                                      parseInt(this._inputQuantidade.value), 
                                      parseFloat(this._inputValor.value)
                                     );
        console.log(negocicao);

        alert('Chamei acção no controller');
    }
}