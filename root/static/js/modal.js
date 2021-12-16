const appointmentBtn = document.querySelector('.appointment-btn')
const appointmentDetailBtn = document.querySelector('.appointment-detail')
const modalTitle = document.querySelector('.modal-title')
const activityDetailTitle = document.querySelector('.activity-detail-title')
const closeBtn = document.querySelectorAll('.btn-close')
const phoneInput = document.querySelector('#phone')

phoneInput.value = '+7'

const modalBuy = new bootstrap.Modal(document.getElementById('modalBuy'), {

})

const modalActivity = new bootstrap.Modal(document.getElementById('modalActivity'), {

})

function closeModal(modal) {
  closeBtn.forEach(btn => {
    btn.addEventListener('click', () => {
      modal.hide();
    })
  });
}

appointmentBtn.addEventListener('click', () => {
  modalBuy.show()
})

if (window.modalActivity) {
  appointmentDetailBtn.addEventListener('click', (evt) => {
    evt.preventDefault()
    modalActivity.show()
    modalTitle.textContent = activityDetailTitle.textContent
  })
}


closeModal(modalBuy)
closeModal(modalActivity)