<template>
    <div>
        <HeaderComponent :user=user></HeaderComponent>
            <section class="ftco-section ftco-cart">
			<div class="container">
				<div class="row">
    			<div class="col-md-12 ftco-animate">
    				<div class="cart-list">
	    				<table class="table">
						    <thead class="thead-primary">
						      <tr class="text-center">
						        <th>&nbsp;</th>
						        <th>&nbsp;</th>
						        <th>Product name</th>
						        <th>Price</th>
						        <th>Quantity</th>
						        <th>Total</th>
						      </tr>
						    </thead>
						    <tbody>
						      <tr class="text-center" v-for="cart in carts" v-bind:key="cart.ProductID">
						        <td class="product-remove"><a href="#"><span class="ion-ios-close"></span></a></td>
						        
						        <td class="image-prod"><div class="img" :style="'background-image:url(' + '/static/uploads/'+cart.photo + ');'"></div></td>
						        
						        <td class="product-name">
						        	<h3>{{cart.name}}</h3>
						        	<p>Far far away, behind the word mountains, far from the countries</p>
						        </td>
						        
						        <td class="price">${{cart.price / cart.productQuantity}}</td>
						        
						        <td class="quantity">
						        	<div class="input-group mb-3">
					             	<input type="text" name="quantity" class="quantity form-control input-number" @change="updateQuantity(cart.productID)" :value="cart.productQuantity" min="1" max="100">
					          	</div>
					          </td>
						        
						        <td class="total">${{cart.price}}</td>
						      </tr><!-- END TR-->
						    </tbody>
						  </table>
					  </div>
    			</div>
    		</div>
    		<div class="row justify-content-end">
    			<div class="col-lg-4 mt-5 cart-wrap ftco-animate">
    				<div class="cart-total mb-3">
    					<h3>Coupon Code</h3>
    					<p>Enter your coupon code if you have one</p>
  						<form action="#" class="info">
	              <div class="form-group">
	              	<label for="">Coupon code</label>
	                <input type="text" class="form-control text-left px-3" placeholder="">
	              </div>
	            </form>
    				</div>
    				<p><a href="checkout.html" class="btn btn-primary py-3 px-4">Apply Coupon</a></p>
    			</div>
    			<div class="col-lg-4 mt-5 cart-wrap ftco-animate">
    				<div class="cart-total mb-3">
    					<h3>Estimate shipping and tax</h3>
    					<p>Enter your destination to get a shipping estimate</p>
  						<form action="#" class="info">
	              <div class="form-group">
	              	<label for="">Country</label>
	                <input type="text" class="form-control text-left px-3" placeholder="">
	              </div>
	              <div class="form-group">
	              	<label for="country">State/Province</label>
	                <input type="text" class="form-control text-left px-3" placeholder="">
	              </div>
	              <div class="form-group">
	              	<label for="country">Zip/Postal Code</label>
	                <input type="text" class="form-control text-left px-3" placeholder="">
	              </div>
	            </form>
    				</div>
    				<p><a href="checkout.html" class="btn btn-primary py-3 px-4">Estimate</a></p>
    			</div>
    			<div class="col-lg-4 mt-5 cart-wrap ftco-animate">
    				<div class="cart-total mb-3">
    					<h3>Cart Totals</h3>
    					<p class="d-flex">
    						<span>Subtotal</span>
    						<span>$20.60</span>
    					</p>
    					<p class="d-flex">
    						<span>Delivery</span>
    						<span>$0.00</span>
    					</p>
    					<p class="d-flex">
    						<span>Discount</span>
    						<span>$3.00</span>
    					</p>
    					<hr>
    					<p class="d-flex total-price">
    						<span>Total</span>
    						<span>$17.60</span>
    					</p>
    				</div>
    				<p><a href="checkout.html" class="btn btn-primary py-3 px-4">Proceed to Checkout</a></p>
    			</div>
    		</div>
			</div>
		</section>
    </div>
</template>
<script>
import HeaderComponent from '../HeaderComponent'
import card from '../../util/card'
export default {
    props: ['user'],
    components: {
        HeaderComponent
    },
    data() {
        return {
            carts: ""
        }
	},
	
	created() {
		this.loadProducts()
	},

    methods: {
        async loadProducts() {
			const cart = JSON.parse(localStorage.getItem('wiboCard'))
            for(let i = 0; i < cart.length; i++) {
				this.getProductByID(cart[i].productID).then(response => {
					let data = response.data
					cart[i].name = data.name
					cart[i].price = data.price * cart[i].productQuantity
					cart[i].photo = data.photo
				})
				
			}
			this.carts = cart
        },

        getProductByID(id) {
			
            return axios.get(`/api/product/${id}`)
		},
		
		updateQuantity(productID) {
			for(let i = 0; i < this.carts.length; i++) {
				if(this.carts[i].productID == productID) {

				}
			}
		}
    }
}
</script>