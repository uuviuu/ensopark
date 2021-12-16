const activityWinter = document.querySelector('.activity-winter')
const activitySummer = document.querySelector('.activity-summer')
const priceBtn = document.querySelector('.price-btn')

const summerBtn = document.querySelector('#no')
const winterBtn = document.querySelector('#yes')

summerBtn.addEventListener('click', () => {
  activitySummer.classList.remove('hidden')
  activityWinter.classList.add('hidden')
  priceBtn.style.backgroundColor = '#77ce06'
})

winterBtn.addEventListener('click', () => {
  activityWinter.classList.remove('hidden')
  activitySummer.classList.add('hidden')
  priceBtn.style.backgroundColor = '#77dbf9'
})