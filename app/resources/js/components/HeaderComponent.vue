<template>
    <nav class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
	    <div class="container">
	      <a class="navbar-brand noselect" href="/">Wibo</a>
	      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#ftco-nav" aria-controls="ftco-nav" aria-expanded="false" aria-label="Toggle navigation">
	        <span class="oi oi-menu"></span> Menu
	      </button>

	      <div class="collapse navbar-collapse" id="ftco-nav">
	        <ul class="navbar-nav ml-auto">
	          <li class="nav-item active"><a href="/" class="nav-link">Home</a></li>
	          <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="dropdown04" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Help</a>
              <div class="dropdown-menu" aria-labelledby="dropdown04">
              	<a class="dropdown-item" href="shop.html">Shiping information</a>
              	<a class="dropdown-item" href="wishlist.html">Term of service</a>
                <a class="dropdown-item" href="product-single.html">Privacy policy</a>
              </div>
            </li>
			<li class="nav-item dropdown" v-if="user.active == 1">
              <a class="nav-link dropdown-toggle" href="#" id="dropdown04" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Current User</a>
              <div class="dropdown-menu" aria-labelledby="dropdown05">
              	<a class="dropdown-item" href="/product/create">Post a product</a>
              	<a class="dropdown-item" href="/logout">Log out</a>
                <a class="dropdown-item" href="/product/view">View your product</a>
              </div>
            </li>
	          <li class="nav-item"><a href="about.html" class="nav-link">Shop</a></li>
	          <li class="nav-item"><a href="/about" class="nav-link">About</a></li>
	          <li class="nav-item"><a href="contact.html" class="nav-link">Contact</a></li>
	          <li class="nav-item cta cta-colored"><a href="cart.html" class="nav-link"><span class="icon-shopping_cart"></span>[{{this.numberOfCardItems}}]</a></li>
	        </ul>
	      </div>
	    </div>
    </nav>
</template>
<script>
import card from '../util/card'
export default {
	props: ['user'],
	data() {
		return {
			numberOfCardItems: JSON.parse(localStorage.getItem('wiboCard')).length
		}
	},

	methods: {
		loadScripts(path) {
			let script = document.createElement('script');
			script.setAttribute('src', path)
			document.head.appendChild(script)
		}
	},
	created() {
		this.loadScripts("https://code.jquery.com/jquery-3.5.1.min.js")
		this.loadScripts("https://code.jquery.com/jquery-migrate-3.3.0.min.js")
		this.loadScripts("/static/js/popper.min.js")
		this.loadScripts("/static/js/bootstrap.min.js")
		this.loadScripts("/static/js/jquery.easing.1.3.js")
		this.loadScripts("/static/js/jquery.waypoints.min.js")
		this.loadScripts("/static/js/jquery.stellar.min.js")
		this.loadScripts("/static/js/owl.carousel.min.js")
		this.loadScripts("/static/js/jquery.magnific-popup.min.js")
		this.loadScripts("/static/js/aos.js")
		this.loadScripts("/static/js/scrollax.min.js")
		this.loadScripts("/static/js/main.js")
	}
}
</script>