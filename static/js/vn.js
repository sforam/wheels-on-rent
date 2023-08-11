const form = document.querySelector('form');
const input = document.querySelector('#vehicle-number');

form.addEventListener('submit', (event) => {
  if (!input.checkValidity()) {
    event.preventDefault();
  }
});