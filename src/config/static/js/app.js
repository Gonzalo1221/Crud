function guardar() {
    const name = document.getElementById("nombre").value;
    const lastname = document.getElementById("apellidos").value;
    const email = document.getElementById("correo").value;
    const message = document.getElementById("mensaje").value;
  
    const data = {
      nombre: name,
      apellidos: lastname,
      correo: email,
      mensaje: message
    };
  
    axios.post('/guardar', data)
      .then(response => {
        console.log(response.data);
        console.log(response.status);
        // You can add additional logic here, such as displaying a success message to the user
      })
      .catch(error => {
        console.log("Error:", error);
        // Handle the error, such as displaying an error message to the user
      });
  }
function actualizar(){

};
function eliminar(){
    
};
function mostrarProductos() {
    axios.get('/api/mostrar')
        .then(response => {
            const productos = response.data;
            const selectElement = document.querySelector('.form-select');

            selectElement.innerHTML = '<option selected>Selecciona un Producto</option>';

            // Iterar sobre los productos y agregar opciones al select
            productos.forEach(producto => {
                const option = document.createElement('option');
                option.value = producto.id; // Asigna el ID como valor del option si lo necesitas
                option.textContent = producto.nombre; // Asigna el nombre del producto como texto del option
                selectElement.innerHTML = option;
            });
        })
        .catch(error => {
            console.error('Error al cargar los productos:', error);
        });
}

// Llama a la función para mostrar los productos cuando la página se carga
document.addEventListener('DOMContentLoaded', mostrarProductos);