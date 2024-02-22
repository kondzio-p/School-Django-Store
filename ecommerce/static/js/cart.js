var updateBtns = document.getElementsByClassName('update-cart');

for (var i = 0; i < updateBtns.length; i++ ){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log("productId: ", productId, "action: ", action);

        console.log('USER: ', user);
        if (user === 'AnonymousUser'){
            console.log("Niezalogowany...");
        }else{
            //console.log("Zalogowany....")
            updateUserOrder(productId, action)
        }

    })
}

function updateUserOrder(productId, action){
    console.log("Sending data...");
    var url = '/update_item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Contenrt-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })
    .then((response) => {
        return Response.json();
    }).then((data) =>{
        console.log("Data: ", data);
        location.reload();
    })
}