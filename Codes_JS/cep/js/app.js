const cep = async cep => {
    const headers = {
        'Content-Type': 'application/json'
    }
    let result = await fetch(`https://api.postmon.com.br/v1/cep/${cep}`, headers);
    let data = await result.text(); 
    console.log(data);
}

function getDados() {
    cep(document.getElementById("cep").value);
}
