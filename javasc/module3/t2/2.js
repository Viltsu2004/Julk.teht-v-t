'use strict';
const info = document.getElementById('target')


let newlist = document.createElement('li')
newlist.textContent = 'First item'

let newlist2 = document.createElement('li')
newlist2.textContent = 'Second item'
newlist2.classList.add('my-item')

let newlist3 = document.createElement('li')
newlist3.textContent = 'Third item'

info.appendChild(newlist)
info.appendChild(newlist2)
info.appendChild(newlist3)

