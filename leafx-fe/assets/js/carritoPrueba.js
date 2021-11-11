const addToShoppingCartButtons = document.querySelectorAll('.btn-product');

addToShoppingCartButtons.forEach(addToCartButton => {

    addToCartButton.addEventListener('click', addToCartClicked);

});

const buyBtn = document.querySelector('.buyBtn');
buyBtn.addEventListener('click', buyClicked);

const cartItemsContainer = document.querySelector('.shoppingCartItemsContainer');

function addToCartClicked (event) {
    
    const button = event.target;
    const item   = button.closest('.product__card');

    const itemTitle = item.querySelector('.product__title').innerText;
    const itemPrice = item.querySelector('.product__precio').innerText;
    const itemImage = item.querySelector('.product__img').src;

    addItemToShoppingCart(itemTitle, itemPrice, itemImage);

}

function addItemToShoppingCart(itemTitle, itemPrice, itemImage) {

    const titles = cartItemsContainer.getElementsByClassName('shoppingCartItemTitle');

    for (let i = 0; i < titles.length; i++) {

        if (titles[i].innerText === itemTitle) {
            
            const quantityElement = cartItemsContainer.getElementsByClassName('shoppingCartItemQuantity')[i];
            const quantity = Number(quantityElement.value);
            quantityElement.value = quantity + 1;
            updateCartTotal();
            return;

        }
    }
    
    
    /* const titles = cartItemsContainer.getElementsByClassName('shoppingCartItemTitle');

    for (let i = 0; i < titles.length; i++) {

        if (titles[i].innerText === itemTitle) {

            const quantityElement = cartItemsContainer.getElementsByClassName('shoppingCartItemQuantity')[i];
            const quantity = Number(quantityElement.value);
            quantityElement.value = quantity + 1;
            updateCartTotal();
            $('.toast').toast('show');
            return; /* La Parte Más Importante 

        }

    } */

    /* Empezar a explicar desde aqui */
    const cartRow = document.createElement('div');
    cartRow.classList.add('cart-row');

    const cartContent = `

    <div class="row shoppingCartItem">
        <div class="col-6">
            <div class="shopping-cart-item d-flex align-items-center h-100 border-bottom pb-2 pt-3">
                <img src=${itemImage} alt="Producto 1" class="shopping-cart-image">
                <h6 class="shopping-cart-item-title shoppingCartItemTitle text-truncate ml-3 mb-0">${itemTitle}
                </h6>
            </div>
        </div>
        <div class="col-2">
            <div class="shopping-cart-price d-flex align-items-center h-100 border-bottom pb-2 pt-3">
                <p class="item-price mb-0 shoppingCartItemPrice">${itemPrice}
                </p>
            </div>
        </div>
        <div class="col-4">
            <div
                class="shopping-cart-quantity d-flex justify-content-between align-items-center h-100 border-bottom pb-2 pt-3">
                <input class="shopping-cart-quantity-input shoppingCartItemQuantity" type="number"
                    value="1" min="1">
                <button class="btn btn-danger buttonDelete" type="button">X</button>
            </div>
        </div>
    </div>`;

    cartRow.innerHTML = cartContent;
    cartItemsContainer.append(cartRow);

    cartRow.querySelector('.buttonDelete')
    .addEventListener('click', () => removeItemFromShoppingCart(cartRow));

    cartRow.querySelector('.shoppingCartItemQuantity').
    addEventListener('change', () => quantityChanged(event));

    updateCartTotal();

}

function updateCartTotal () {

    let total = 0;
    const shoppingCartTotal = document.querySelector('.shoppingCartTotal');
    const cartItems = document.querySelectorAll('.shoppingCartItem');

    cartItems.forEach(cartItem => {

        const itemPriceElement = cartItem.querySelector('.shoppingCartItemPrice');
        const itemPrice = Number(
            itemPriceElement.innerText.replace('$', '').replace(',', '')
        );

        const itemQuantityElement = cartItem.querySelector('.shoppingCartItemQuantity');
        const itemQuantity = Number(itemQuantityElement.value);

        total = total + (itemPrice * itemQuantity);

        
    });
    
    total = String(total).replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,');
    shoppingCartTotal.innerText = `$ ${total}`;
    
}

function removeItemFromShoppingCart (cartRow) {

    cartItemsContainer.removeChild(cartRow);
    updateCartTotal();

}

function quantityChanged (event) {

    const input = event.target;
    input.value <= 0 ? input.value = 1 : null;

    updateCartTotal();

}

function buyClicked () {

    cartItemsContainer.innerHTML = '';
    updateCartTotal();

}