const choice = document.querySelectorAll(".nav-btn");
choice.forEach(function (choice) {
  choice.addEventListener("click", function (e) {
    console.log("clicked");
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
    } else if (choice == "News") {
      news.classList.remove("d-none");
      business.classList.add("d-none");
      facility.classList.add("d-none");
    }
  });
});
