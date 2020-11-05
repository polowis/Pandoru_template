<template>
    <div>
    <HeaderComponent :user=user></HeaderComponent>
    <section class="login-section">
      <div class="title-login noselect">Post a product</div>
      <form autocomplete="false">
        <div class="input-field noselect">
        <input class="required" type="text" v-model="productName"><label class="required" for="username">Product's name</label>
        <div style="color: red" v-if="productNameError">{{this.productName}} is not a valid name, you might consider using only alphanumeric characters</div>
        </div>
        <div class="form-row">
        <div class="col-3" style="margin: 20px 0 0 30px;">
            <label for="mr" accesskey="s">Type</label>
                <select class="form-control" v-model="productType">
                    <option disabled value="">Choose...</option>
                    <option>Electronic</option>
                    <option>Books</option>
                    <option>Toys</option>
                    <option>Clothes</option>
                    <option>Other</option>
                </select>
              </div>
        <div class="input-field col noselect" >
            <input type="number" style="width: 76%;" v-model="productQuantity"><label for="username">Quantity</label>
        </div>
        </div>
         

          <div class="input-field noselect" v-if="productType == 'Other'">
                <input type="number" v-model="productSubtype"><label for="mail">Enter your product type</label>
          </div>
          
          <div class="input-field noselect">
            <input type="text" v-model="productTag"><label for="mail">Product tag, separate tags by comma</label>
          </div>
          <div class="input-field noselect">
            <input type="number" v-model="productPrice"><label for="mail">Product price</label>
          </div>
          <div class="input-field noselect">
            <input type="text" v-model="productDescription"><label for="mail">Product description</label>
          </div>
          <div class="input-field noselect">
            <input type="file" id="file" ref="file" v-on:change="handlePhotoUpload()"><label for="mail">Product image</label>
          </div>
            <div class="button-submit button" style="width: 80%; margin: 50px 0 0 30px;" @click.prevent="createProduct()">
                Post
            </div>
      </form>
      <br><br><br>
      <div class="row">
          <div class="col-md-12 text-center noselect">
            
            <p>
              Copyright &copy; {{this.date}} Made with <i class="icon-heart color-danger" style="color: red;" aria-hidden="true"></i> by <a href="https://github.com/polowis" target="_blank">Polowis</a>

            </p>
          </div>
        </div>
    </section>
    </div>
</template>
<script>
import HeaderComponent from '../HeaderComponent'
export default {
    props: ['user'],
    components: {
        HeaderComponent
    },
    data() {
        return {
            date: new Date().getFullYear(),
            productName: "",
            productQuantity: "",
            productType: "",
            productSubtype: "",
            productTag: "",
            productDescription: "",
            productPrice: "",
            productFile: "",
            errors: [],
            productNameError: false,
            productPriceError: false,
            productQuantityError: false,
            productSubtypeError: false,

        }
    },

    watch: {
        productName: function() {
          this.debounceGetProductName()

      }
    },

    created() {
        this.debounceGetProductName = _.debounce(this.checkProductNameError, 50)

    },

    methods: {
      checkProductNameError() {
        return this.productName.match(/^[ a-z0-9]+$/i) == null ? this.productNameError = true : this.productNameError = false
      },

      checkProductSubtypeError() {
        if(this.productSubtype != '') {
          return this.productSubtype.match(/^[ a-z0-9]+$/i) == null ? this.productSubtypeError = true : this.productSubtypeError = false
        }
      },

      checkProductPriceError() {
        return this.productPrice.match(/^[0-9]+$/i) == null ? this.productPriceError = true : this.productPriceError = false
      },

      checkProductQuantityError() {
        return this.productQuantity.match(/^[0-9]+$/i) == null ? this.productQuantityError = true : this.productQuantityError = false
      },

      handlePhotoUpload() {
        this.productFile = this.$refs.file.files[0];
      },

      createProduct() {
        let formData = new FormData()
        formData.append('file', this.productFile)
        formData.append('name', this.productName)
        formData.append('price', this.productPrice)
        formData.append('description', this.productDescription)
        formData.append('category', this.handleProductType())
        formData.append('quantity', this.productQuantity)
        formData.append('tag', this.productTag)

        axios.post('/api/product/create', 
          formData, 
          { 
            headers: {
            'Content-Type': 'multipart/form-data'
            }
          }
        ).then()

      },

      handleProductType() {
        return this.productType == 'Other' ? this.productSubtype: this.productType
      }

    }
}
</script>