const arrow = document.getElementById("arrow");
const form_list = document.getElementById("form_list");

const rotate = () => {
  arrow.classList.toggle("rotate-180");
  form_list.classList.toggle("hidden");
};
