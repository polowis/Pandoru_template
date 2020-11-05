<template>
    <div>
        <HeaderComponent :user=user></HeaderComponent>
        <section class="login-section">
      <div class="title-login noselect">Business Information Application</div>
      <form autocomplete="false">
        <div class="input-field noselect">
        <input class="required" type="text" v-model="businessName"><label class="required" for="username">Company/Organization name</label>
        <div style="color: red" v-if="businessNameError">{{this.businessName}} is not a valid business name</div>
        </div>
        <div class="form-row">
        <div class="col-3" style="margin: 20px 0 0 30px;">
            <label for="mr" accesskey="s">Title</label>
                <select class="form-control" v-model="contactTitle">
                    <option disabled value="">Choose...</option>
                    <option>Mr</option>
                    <option>Mrs</option>
                    <option>Dr</option>
                    <option>Ms</option>
                </select>
                
              </div>
       
        <div class="input-field col noselect" >
            <input class="" type="text" style="width: 76%;" v-model="contactName"><label for="username">Contact name</label>
        </div>
        </div>
         <div class="input-field" style="color: red; margin-top: 0px;" v-if="contactTitleError == true">Make sure that {{this.contactTitle}} matches with the options</div>
        <div class="input-field" style="color: red; margin-top: 0px;" v-if="contactNameError == true">Make sure that {{this.contactName}} only containts 0-9 and a-z characters</div>
        <div class="input-field noselect">
          <input type="text" v-model="mailingAddress"><label for="mail">Mailing Address </label>
        </div>
         <div class="input-field" style="color: red; margin-top: 0px;" v-if="mailingAddressError == true">{{this.mailingAddress}} is not a valid email address</div>
        <div class="input-field" style="margin-top: 0px"></div>
        
          <div class="input-field noselect">
                <input type="number" v-model="businessNumber"><label for="mail">Business Contact Number</label>
          </div>
          <div class="input-field" style="color: red; margin-top: 0px;" v-if="businessNumberError == true">Make sure {{this.businessNumber}} is a valid phone number</div>
          <div class="input-field noselect">
            <input type="text" v-model="businessType"><label for="mail">Business Type</label>
          </div>
           <div class="input-field" style="color: red; margin-top: 0px;" v-if="businessTypeError == true">This is not a valid type of business</div>
          <div class="input-field noselect">
              <input type="password" v-model="password"><label for="mail">Password</label>
            </div>
            <div class="input-field noselect">
                <input type="password" v-model="confirmPassword"><label for="mail">Confirm password</label>
              </div>
              <div class="input-field" style="color: red; margin-top: 0px;" v-if="passwordError == true">Make sure the length of password is greater than 7 and should be the same as confirmed password</div>
            <div class="noselect" style="margin: 20px 0 0 30px; font-size: 13px;">Already a member?<a href="/login">  Sign in here</a> </div>
            <div class="button-submit button" style="width: 80%; margin: 50px 0 0 30px;" @click.prevent="checkValidation()">
                Register
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
            businessName: "",
            contactTitle: "",
            contactName: "",
            mailingAddress: "",
            businessNumber: "",
            businessType: "",
            password: "",
            confirmPassword: "",
            errors: [],
            businessNameError: false,
            contactTitleError: false,
            contactNameError: false,
            mailingAddressError: false,
            businessNumberError: false,
            businessTypeError: false,
            passwordError: false

        }
    },

    watch: {
        businessName: function() {
            this.debouncedGetBusinessName()
        },

        contactTitle: function() {
            this.debouncedGetContactTitle()
        },

        contactName: function() {
            this.debouncedGetContactName()
        },

        mailingAddress: function() {
            this.debouncedGetMailingAddress()
        },

        businessNumber: function() {
            this.debouncedGetBusinessNumber()
        },

        businessType: function() {
            this.debouncedGetBusinessType()
        },

        confirmPassword: function() {
            this.debouncedGetPassword()
        }
    
    },

    created() {
        this.debouncedGetBusinessName = _.debounce(this.checkBusinessNameError, 50)
        this.debouncedGetContactTitle = _.debounce(this.checkContactTitleError, 50)
        this.debouncedGetContactName = _.debounce(this.checkContactNameError, 50)
        this.debouncedGetMailingAddress = _.debounce(this.checkMailingAddressError, 50)
        this.debouncedGetBusinessNumber = _.debounce(this.checkBusinessNumberError, 50)
        this.debouncedGetBusinessType = _.debounce(this.checkBusinessTypeError, 50)
        this.debouncedGetPassword = _.debounce(this.checkPassword, 50)
    },

    methods: {
        checkBusinessNameError() {
            if(this.businessName.match(/^[ a-z0-9]+$/i) == null) {
                this.businessNameError = true
                
                return;
            } 
            
            this.businessNameError = false
              
            return;
        },

        checkContactTitleError() {
            if(['Mr', 'Mrs', 'Dr', 'Ms'].includes(this.contactTitle)) {
                
                this.contactTitleError = false
                    
                return;
            }   
            this.contactTitleError = true
            return;

        },

        checkContactNameError() {
            if(this.contactName.match(/^[ a-z0-9]+$/i) == null) {
                this.contactNameError = true
              
                return;
            } 
            
            this.contactNameError = false
               
            return;
        },

        checkMailingAddressError() {
            const emailRegex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            if(this.mailingAddress.match(emailRegex) == null) {
                this.mailingAddressError = true
               
                return;
            }
            this.mailingAddressError = false
            
            return;
        },

        checkBusinessNumberError() {
            const phoneRegex = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im
            if(this.businessNumber.match(phoneRegex) == null || this.businessNumber.length <= 7) {
                this.businessNumberError = true;
                return
            }
           
            this.businessNumberError = false
            return
        },

        checkBusinessTypeError() {
            if(this.businessType.match(/^[ a-z0-9]+$/i) == null) {
                this.businessTypeError = true
                return;
            } 
           
            this.businessTypeError = false
                
            return;
        },

        checkPassword() {
            if(this.password.length < 8 || this.password != this.confirmPassword) {
                this.passwordError = true
                return;
            }
            this.passwordError = false
            return;
            
        },

        checkValidation() {
            this.checkBusinessNameError()
            this.checkContactTitleError()
            this.checkContactNameError()
            this.checkMailingAddressError()
            this.register()

           
        },

        hasErrors() {
            let values = [this.businessNameError, this.contactTitleError, 
            this.contactNameError, this.mailingAddressError, this.businessNumberError, 
            this.businessTypeError, this.passwordError]
            
            let errors = values.reduce((memo, element) => {
                return element == true
            })
        },
        
        register() {
            if(this.hasErrors()) return;

            axios.post("/api/register", {
                companyName: this.businessName,
                contactName: this.contactName,
                mailingAddress: this.mailingAddress,
                contactNumber: this.businessNumber,
                contactTitle: this.contactTitle,
                password: this.password,
                businessType: this.businessType
            }).then(response => {
                if(response.data.message == 'Success') {
                    window.location = "/"
                } 
            })
        }

    }
}
</script>