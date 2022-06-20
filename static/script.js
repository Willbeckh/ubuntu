const choice = document.querySelectorAll(".nav-btn");
choice.forEach(function (choice) {
  choice.addEventListener("click", function (e) {
    e.preventDefault();
    const choice = e.target.innerText;
    const business = document.querySelector(".business-section");
    const facility = document.querySelector(".facility-section");
    const news = document.querySelector(".news-section");
    if (choice === "Businesses") {
      business.classList.remove("d-none");
      facility.classList.add("d-none");
      news.classList.add("d-none");
    } else if (choice === "Facilities") {
      facility.classList.remove("d-none");
      business.classList.add("d-none");
      news.classList.add("d-none");
    } else if (choice == "Posts") {
      news.classList.remove("d-none");
      business.classList.add("d-none");
      facility.classList.add("d-none");
    }
  });
});

// randomize bg-color on facility divs
$("document").ready(function () {
  console.log("page loaded");
  const cards = document.querySelectorAll(".facility-card");
  const colors = ["#b5e48c", "#f1faee", "#F6F3FC", "#E8F2F8", "#E1FDFB"];
  let new_color = colors[Math.floor(Math.random() * colors.length)];

  cards.forEach(function (card) {
    $(card).css("background-color", new_color);
  });
  // $(cards).css("background-color", new_color);
});
