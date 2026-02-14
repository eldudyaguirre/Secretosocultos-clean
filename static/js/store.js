function addToCart(productoId, csrf_token) {

    const payload = {
        producto_id: productoId,
        cantidad: 1
    }

    fetch('/add-to-cart/', {
        method: 'POST',
        body: JSON.stringify(payload),
        headers: {  'Content-Type': 'application/json; charset=UTF-8',
                    'X-CSRFToken': csrf_token
        }
    })
    .then(res =>res.json())
    .then(data => document.getElementById('cart-items-counter').innerHTML = data.count_cart_items);
}

function removeFromCart(productoId, csrf_token) {

    const payload = {
        producto_id: productoId
    }

    fetch('/remove-from-cart/', {
        method: 'POST', 
        body: JSON.stringify(payload),
        headers: {  'Content-Type': 'application/json; charset=UTF-8',
                    'X-CSRFToken': csrf_token
        }
    })
    .then(res => res.json())
    .then(() => location.href = '/cart');
}


function crearPedido(csrf_token) {

    const payload = {}

    fetch('/pedidos/', {
        method: 'POST',
        body: JSON.stringify(payload),
        headers: {  'Content-Type': 'application/json; charset=UTF-8',
                    'X-CSRFToken': csrf_token
        }
    })
    .then(res=> {
        if(!res.ok) {
            throw Error('El pedido no pudo ser registrado');
        }
        return res.json();
    })
    .then(data => {
        alert('Se registró exitosamente el pedido # ' + data.codigo_pedido);
        location.href = '/';
    })
    .catch(error => alert(error));
}