let toastTimeout;

function openToast(message, time=5000) {
  const toast = document.getElementById('toast');
  const toastContent = toast.querySelector('.toast__content');
  
  if (toastTimeout) {
    clearTimeout(toastTimeout);
  }

  toast.classList.add('show');
  toastContent.innerText = message;
  
  toastTimeout = setTimeout(() => {
    toast.classList.remove('show');
  }, time);
}