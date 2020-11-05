<template>
    <div>
        <HeaderComponent :user=user></HeaderComponent>
        <div class="hero-wrap hero-bread" style="background-image: url('https://analyticsindiamag.com/wp-content/uploads/2019/03/guestpost-banner-01.jpg');">
            <div class="container">
                <div class="row no-gutters slider-text align-items-center justify-content-center">
                    <div class="col-md-9 ftco-animate text-center">
                        <h1 class="mb-0 bread" style="color: #a5ef50; margin-top 10px;">{{product.name}}</h1>
                    </div>
                 </div>
            </div>
        </div>

        <section class="ftco-section">
    	<div class="container">
    		<div class="row">
    			<div class="col-lg-6 mb-5 ftco-animate">
    				<a :href="'/static/uploads/' + product.photo" class="image-popup"><img :src="'/static/uploads/' + product.photo" class="img-fluid" :alt="product.name"></a>
    			</div>
    			<div class="col-lg-6 product-details pl-md-5 ftco-animate">
    				<h3>{{product.name}}</h3>
    				<div class="rating d-flex">
							<p class="text-left mr-4">
								<a href="#" class="mr-2">5.0</a>
								<a href="#"><span class="ion-ios-star-outline"></span></a>
								<a href="#"><span class="ion-ios-star-outline"></span></a>
								<a href="#"><span class="ion-ios-star-outline"></span></a>
								<a href="#"><span class="ion-ios-star-outline"></span></a>
								<a href="#"><span class="ion-ios-star-outline"></span></a>
							</p>
							<p class="text-left mr-4">
								<a href="#" class="mr-2" style="color: #000;">100 <span style="color: #bbb;">Rating</span></a>
							</p>
							<p class="text-left">
								<a href="#" class="mr-2" style="color: #000;">500 <span style="color: #bbb;">Sold</span></a>
							</p>
						</div>
    				<p class="price"><span>${{product.price}}.00</span></p>
    				<p>{{product.description}}
						</p>
						<div class="row mt-4">
							<div class="col-md-6">
								<div class="form-group d-flex">
									<!--
		              <div class="select-wrap">
	                  <div class="icon"><span class="ion-ios-arrow-down"></span></div>
	                  <select name="" id="" class="form-control">
	                  	<option value="">Small</option>
	                    <option value="">Medium</option>
	                    <option value="">Large</option>
	                    <option value="">Extra Large</option>
	                  </select>
	                </div>-->
		            </div>
							</div>
							<div class="w-100"></div>
							<div class="input-group col-md-6 d-flex mb-3">
	             	<!--<span class="input-group-btn mr-2">
	                	<button type="button" class="quantity-left-minus btn"  data-type="minus" data-field="">
	                   <i class="ion-ios-remove"></i>
	                	</button>
	            		</span>-->
	             	<input type="number" id="quantity" name="quantity" v-model="quantity" class="form-control input-number" value="1" min="1" max="100">
					 <!--
	             	<span class="input-group-btn ml-2">
	                	<button type="button" class="quantity-right-plus btn" data-type="plus" data-field="">
	                     <i class="ion-ios-add"></i>
	                 </button>
	             	</span>-->
	          	</div>
	          	<div class="w-100"></div>
	          	<div class="col-md-12">
	          		<!--<p style="color: #000;">600 kg available</p>-->
	          	</div>
          	</div>
          	<p><a href="#" class="btn btn-black py-3 px-5" @click.prevent="addToCart()">Add to Cart</a></p>
    			</div>
    		</div>
			<div v-if="errorMessage.length != 0" style="color: red">{{this.errorMessage}}</div>
			<div v-if="successMessage.length != 0" style="color: green">{{this.successMessage}}</div>
    	</div>
    </section>
    </div>
</template>
<script>
import HeaderComponent from '../HeaderComponent'
import card from  '../../util/card'
export default {
    props: ['product', 'user'],
    components: {
        HeaderComponent
	},

	data() {
		return {
			quantity: 1,
			quantityTypeError: false,
			cardAddSuccess: false,
			errorMessage: "",
			successMessage: ""
		}
	},

	methods: {
		addToCart() {
			Number.isSafeInteger(this.quantity) ?  this.createProduct() : this.errorMessage = "Invalid type, must be a number. and no decimal"
		},

		createProduct() {
			try {
				card.create(this.product.productID, this.quantity)
				this.cardAddSuccess = true
				this.successMessage = "Added product to card"
			} catch(err) {
				this.errorMessage = err.message
			}
			
		}
	}

}
</script>