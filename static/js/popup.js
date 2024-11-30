function openPopup(country) {
  const popup = document.getElementById('popup');
  const popupCountry = popup.querySelector('.country__name');
  const popupFlag = popup.querySelector('.country__flag');
  const popupCuriosity = popup.querySelector('.country__curiosity');

  const { name, curiosity, flag } = country;
  popupCountry.innerText = name;
  popupFlag.src = flag;
  popupCuriosity.innerText = curiosity;

  popup.classList.add('show');
}

function closePopup() {
  const popup = document.getElementById('popup');
  popup.classList.remove('show');
}