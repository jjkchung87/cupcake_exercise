let cupcakeList;
const newCupcakeForm = $('#cupcake-form')
const editCupcakeForm = $('cupcake-update-form')


/* ***************************************************************************************** */
//Retrieve list of cupcakes and d on page


/* ***************************************************************************************** */
//Retrieve list of cupcakes and put on page

async function getcupcakeList(){
    cupcakeList = await Cupcakes.getCupcakes()
    putCupcakesOnPage()
}


function putCupcakesOnPage(){
    $('#cupcake-area').children().remove()
    for (let cupcake of cupcakeList.cupcakes){
        $("#cupcake-area").append(`<div class="col col-4"> 
            <a href="/${cupcake.id}"><b>${cupcake.flavor}</b><br>
            <img src=${cupcake.image} class="cupcake-image"></a><br> 
            <b>Rating:</b> ${cupcake.rating} 
             || <b>Size:</b> ${cupcake.size}
        </div>`)
    }
}

/* ***************************************************************************************** */
//Handle new Cupcake form

$('#cupcake-form').on('submit',submitCupcakeForm)

async function submitCupcakeForm(evt){
    evt.preventDefault()
    const flavor = $('#flavor').val()
    const rating = $('#rating').val()
    const size = $('#size').val()
    const image = $('#image').val()

    const cupcakeData = {flavor, rating, size, image}
    await cupcakeList.addCupcake(cupcakeData)

    $('#flavor').val('');
    $('#rating').val('');
    $('#size').val('');
    $('#image').val('');

    getcupcakeList()
}

/* ***************************************************************************************** */
//Filter cupcakes

$('#search-bar-input').on('keyup',filterCupcakes)

async function filterCupcakes(evt){
    if($(this).val()){
        flavorString = $(this).val()
        cupcakeList = await Cupcakes.getFilteredCupcakes(flavorString)
        putCupcakesOnPage()
    } else {
        getcupcakeList()
    }
        

}

/* ***************************************************************************************** */
//Handle cupcake edit

$('#cupcake-update-form').on('submit',submitCupcakeUpdateForm)

async function submitCupcakeUpdateForm(evt){
    evt.preventDefault()
    const flavor = $('#flavor').val()
    const rating = $('#rating').val()
    const size = $('#size').val()
    const image = $('#image').val()

    const cupcakeData = {flavor, rating, size, image}
    await cupcakeList.updateCupcake(cupcakeData)

    $('#flavor').val('');
    $('#rating').val('');
    $('#size').val('');
    $('#image').val('');

    getcupcakeList()
}




