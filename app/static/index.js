(() => {
	function mod(a, b) {
		return ((a % b) + b) % b;
	}

	const carousel = document.querySelector("[data-carousel]");

	const delay = 10000;
	let id = setTimeout(next, delay);

	function next() {
		currentSlide = mod(currentSlide + 1, numSlides);
		setSlide(currentSlide);
	}

	function back() {
		currentSlide = mod(currentSlide - 1, numSlides);
		setSlide(currentSlide);
	}

	function setSlide(slideNumber) {
		carousel.style.setProperty("--current-slide", slideNumber);
		document
			.querySelectorAll(`[data-carousel-button-slide]`)
			.forEach(button => button.classList.remove("active"));
		document
			.querySelector(`[data-carousel-button-slide="${slideNumber}"]`)
			.classList.add("active");

		clearTimeout(id);
		id = setTimeout(next, delay);
	}

	const buttonPrevious = carousel.querySelector(
		"[data-carousel-button-previous]"
	);
	const buttonNext = carousel.querySelector("[data-carousel-button-next]");
	const slideContainer = carousel.querySelector(
		"[data-carousel-slides-container]"
	);

	let currentSlide = 0;
	const numSlides = slideContainer.children.length;

	buttonPrevious.addEventListener("click", back);
	buttonNext.addEventListener("click", next);

	const buttons = document.querySelector("[data-carousel-buttons]");
	for (let i = 0; i < numSlides; i++) {
		const button = document.createElement("button");
		button.type = "button";
		button.setAttribute("title", i + 1);
		button.setAttribute(`data-carousel-button-slide`, i);
		button.classList.add("carousel-tip");
		button.addEventListener("click", () => {
			currentSlide = i;
			setSlide(currentSlide);
		});
		buttons.appendChild(button);
	}

	setSlide(currentSlide);
})();

(() => {
	const scrollers = document.querySelectorAll("[data-to]");

	scrollers.forEach(scroller => {
		const id = scroller.getAttribute("data-to");
		const element = document.getElementById(id);

		scroller.addEventListener("click", e => {
			e.preventDefault();
			element.scrollIntoView();
		});
	});
})();
