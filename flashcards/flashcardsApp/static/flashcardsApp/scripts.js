document.addEventListener('DOMContentLoaded', function() {
    
})

function toggleView(){
  const the_button = document.querySelector('#toggle_view_button');
  const divs = document.querySelectorAll('.main-area > div');
  if (the_button.innerHTML === 'Grid view'){
    divs.forEach(div => {
      div.className = 'col-md-12';
    })
    // Change the button text 
    the_button.innerHTML = 'List view';
  } else {
    divs.forEach(div => {
      div.className = 'col-md-6';
    })
    // Change the button text 
    the_button.innerHTML = 'Grid view';
  }
}
