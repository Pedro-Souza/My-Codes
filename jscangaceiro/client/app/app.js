const controller = new NegocicaoController(); 
//const negociacao = new Negociacao();

document.querySelector('.form').addEventListener('submit', controller.adiciona.bind(controller));