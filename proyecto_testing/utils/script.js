// agregar elementos a la tabla
const formulario = document.getElementById('miFormulario');
const tabla = document.getElementById('miTabla').getElementsByTagName('tbody')[0];

formulario.addEventListener('submit', function (event) {
    event.preventDefault();

    const codigo = document.getElementById('codigo').value;
    const elemento = document.getElementById('elemento').value;
    const descripcion = document.getElementById('descripcion').value;

    console.log("Código:", codigo);
    console.log("Elemento:", elemento);
    console.log("Descripción:", descripcion);

    // Crear una nueva fila en la tabla
    const fila = tabla.insertRow();
    const celdaCodigo = fila.insertCell(0);
    const celdaElemento= fila.insertCell(1);
    const celdaDescripcion = fila.insertCell(2);

    // Agregar los valores del formulario a la fila
    celdaCodigo.textContent = codigo;
    celdaElemento.textContent = elemento;
    celdaDescripcion.textContent = descripcion;
    // Limpiar el formulario
    formulario.reset();
});
