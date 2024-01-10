const checkboxImage = document.getElementById("show_image");
const textImage = document.getElementById("add_image");

checkboxImage.addEventListener("change", () => {
  if (checkboxImage.checked) {
    textImage.style.display = "block";
  } else {
    textImage.style.display = "none";
  }
});

const checkboxText = document.getElementById("show_text");
const textdescrition = document.getElementById("add_text");

checkboxText.addEventListener("change", () => {
  if (checkboxText.checked) {
    textdescrition.style.display = "block";
  } else {
    textdescrition.style.display = "none";
  }
});
