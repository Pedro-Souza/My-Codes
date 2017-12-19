const cep = async cep => {
    const headers = {
        'Content-Type': 'application/json'
    }
    let result = await fetch(`https://api.postmon.com.br/v1/cep/${cep}`, headers);
    let data = await result.text(); 
    result = JSON.parse(data);
    document.getElementById("cidade").innerHTML = `Cidade => ${result.cidade}`;
    document.getElementById("estado").innerHTML = `Estado => ${result.estado}`;
    document.getElementById("bairro").innerHTML = `Bairro => ${result.bairro}`;
    document.getElementById("rua").innerHTML = `Rua => ${result.logradouro}`
    console.log(JSON.parse(data));
}

const getDados = () => {
    cep(document.getElementById("cep").value);
}
