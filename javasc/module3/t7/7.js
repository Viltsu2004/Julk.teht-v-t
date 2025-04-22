'use strict'

let efect = document.getElementById('trigger')
let h = document.getElementById('target')

efect.addEventListener('mouseover', () =>{
  h.setAttribute("src", 'img/picB.jpg')
})

efect.addEventListener('mouseout', () =>{
  h.setAttribute("src", 'img/picA.jpg')
})
