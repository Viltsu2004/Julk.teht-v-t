'use strict';

document.querySelector('input[type = "submit"]').addEventListener('click', (event) => {
  event.preventDefault()
  const first = document.querySelector('input[name="firstname"]').value

  const last = document.querySelector('input[name="lastname"]').value
  document.getElementById('target').innerText = (`Your name is ${first} ${last}`)
})
