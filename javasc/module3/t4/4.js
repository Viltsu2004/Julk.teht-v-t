'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

for (let student of students){
  const data = document.createElement('option')
  data.textContent = student.name
  data.value = student.id
  document.getElementById('target').appendChild(data)
}
