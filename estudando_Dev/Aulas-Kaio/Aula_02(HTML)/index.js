const fNome = document.getElementById("nome");
const fAutor = document.getElementById("autor");
const fData = document.getElementById("data");
const fGenero1 = document.getElementById("genero");
const fGenero2 = document.getElementById("genero2");
const fStatusOn = document.getElementById("status-on");
const fStatusOff = document.getElementById("status-off");
const fValor = document.getElementById("valor");
document.getElementById("btnBuscar").addEventListener("click", filtroData);

function filtroData() {
  const filtros = {
    nome: fNome.value,
    autor: fAutor.value,
    data: fData.value,
    g1: fGenero1.value,
    g2: fGenero2.value,
    valor: fValor.value,
    on: fStatusOn.checked,
    off: fStatusOff.checked,
  };

  console.table(filtros);
}
