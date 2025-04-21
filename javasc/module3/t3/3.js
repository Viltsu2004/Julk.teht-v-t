'use strict';

const names = ['John', 'Paul', 'Jones'];
let list = ''
for (let name of names) {
  list += `<li>${name}</li>`
}

document.getElementById('target').innerHTML = list