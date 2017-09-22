class NegocicaoController{
    constructor() {
        console.log('Fui instânciada');
    }
    adiciona(event) {
        event.preventDefault();
        let $ = document.querySelector();
        let inputData = $("#data");
        let inputQuantidade = $("#quantidade");
        let inputValor = $("#valor");
        console.log(inputData);
        console.log(parseInt(inputQuantidade));
        console.log(parseFloat(inputValor));
        alert('Chamei acção no controller');
    }
}