
// Llama a la función para mostrar los productos cuando la página se carga
document.addEventListener('DOMContentLoaded', mostrarProductos);
document.addEventListener('DOMContentLoaded', llenartabla);

function guardar() {
  const name = document.getElementById("nombre").value;
  const lastname = document.getElementById("apellidos").value;
  const phone = document.getElementById("telefono").value;
  const product = document.getElementById("producto").value;

  const data = {
    name: name,
    lastname: lastname,
    phone: phone,
    product: product
  };

  axios.post('/api/guardar', data)
    .then(response => {
      console.log(response.data);
      console.log(response.status);
      // You can add additional logic here, such as displaying a success message to the user
      alert('Datos guardados con exito')
    })
    .catch(error => {
      console.log("Error:", error);
      // Handle the error, such as displaying an error message to the user
    });
}

function mostrarProductos() {
  axios.get('/api/mostrarproductos')
    .then(response => {
      const productos = response.data;
      const selectElement = document.querySelector('.form-select');

      selectElement.innerHTML = '<option selected>Selecciona un Producto</option>';

      // Iterar sobre los productos y agregar opciones al select
      productos.forEach(producto => {
        const option = document.createElement('option');
        option.value = producto.id; // Asigna el ID como valor del option si lo necesitas
        option.textContent = producto.nombre; // Asigna el nombre del producto como texto del option
        selectElement.append(option);
      });
    })
    .catch(error => {
      console.error('Error al cargar los productos:', error);
    });
}

function llenartabla() {
  axios.get('/api/mostrarusuarios')
    .then(response => {
      const usuarios = response.data;
      const tabla = document.querySelector('.table');
      console.log(usuarios);

      usuarios.forEach(usuario => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
        <th scope="row">${usuario.id}</th>
        <td>${usuario.nombre}</td>
        <td>${usuario.apellidos}</td>
        <td>${usuario.telefono}</td>
        <td>${usuario.productos}</td>
        <td>
          <button class="btn btn-primary btn-sm" onclick="cargarUsuario(${usuario.id})">Actualizar</button>
          <button class="btn btn-danger btn-sm"onclick="eliminarUsuario(${usuario.id})">Eliminar</button>
        </td>
      `;
        tabla.appendChild(tr);
      });
    })
    .catch(error => {
      console.log('Error al cargar los usuarios: ', error);
    })
}

function cargarUsuario(id) {

  axios.get(`/api/llenarusuarios/${id}`)
    .then(response => {
      const usuarios = response.data;
      console.log(usuarios);

        document.getElementById('nombre').value = usuarios.nombre;
        document.getElementById('apellidos').value = usuarios.apellidos;
        document.getElementById('telefono').value = usuarios.telefono;
        document.getElementById('producto').value = usuarios.productos;
        mostrarCancelar();

      // Cambiar el texto y la funcionalidad del botón del formulario a "Actualizar"
      const botonGuardar = document.querySelector('button[type="guardar"]');
      botonGuardar.textContent = 'Actualizar';
      botonGuardar.onclick = function() {
        actualizarUsuario(id);
        ocultarCancelar();
      };

      // Agregar botón "Cancelar" y cambiar su funcionalidad
      const botonCancelar = document.getElementById('cancelarBtn');
      botonCancelar.onclick = function() {
        botonGuardar.textContent = 'Guardar';
        botonGuardar.onclick = function() {
          guardar();
        };
        botonCancelar.style.display = 'none';
        limpiarcampos();
      };
    })
    .catch(error => {
      console.log('Error al cargar datos de usuario: ', error);
    });
}

function actualizarUsuario(id) {
  const nombre = document.getElementById('nombre').value;
  const apellidos = document.getElementById('apellidos').value;
  const telefono = document.getElementById('telefono').value;
  const producto = document.getElementById('producto').value;

  const datosActualizar = {
    nombre: nombre,
    apellidos: apellidos,
    telefono: telefono,
    productos: producto
  };

  axios.put(`/api/actualizarusuario/${id}`, datosActualizar)
    .then(response => {
      alert('Usuario actualizado correctamente');
      location.reload();
    })
    .catch(error => {
      console.log('Error al actualizar el usuario: ', error);
    });
}
function eliminarUsuario(id) {
  axios.delete('/api/eliminarusuario/' + id)
   .then(response => {
      console.log('Usuario eliminado con éxito');
      llenartabla();
      location.reload();
    })
   .catch(error => {
      console.log('Error al eliminar el usuario: ', error);
    });
}

function ocultarCancelar() {
  const botonCancelar = document.getElementById('cancelarBtn');
  botonCancelar.style.display = 'none'; // Oculta el botón "Cancelar"
}

function mostrarCancelar() {
  const botonCancelar = document.getElementById('cancelarBtn');
  botonCancelar.style.display = 'inline-block'; // Muestra el botón "Cancelar"
}
function limpiarcampos() {
  document.getElementById('nombre').value = "";
  document.getElementById('apellidos').value = "";
  document.getElementById('telefono').value = "";
  document.getElementById('producto').selectedIndex = 0;
}