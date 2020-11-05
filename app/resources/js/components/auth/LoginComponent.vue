<template>
    <div>
    <HeaderComponent :user=user></HeaderComponent>
    <section class="login-section">
      <div class="title-login noselect">Log in</div>
      <form>
        <div class="input-field noselect">
          <input type="text" v-model="email"><label for="mail">Email Address</label>
        </div>
        <div class="input-field" style='color: red' v-if="emailError.length > 0">{{this.emailError}}</div>
          <div class="input-field noselect">
              <input type="password" v-model="password"><label for="mail">Password</label>
            </div>
            <div class="noselect" style="margin: 20px 0 0 30px; font-size: 13px;">Not a member?<a href="/register">  Sign up here</a> </div>
            <div class="button-submit button" style="width: 80%; margin: 50px 0 0 30px;" @click.prevent="login()">
                Log in
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
            email: "",
            password: "",
            emailError: "",
            passwordError: ""
        }
    },

    methods: {
      login() {
        if(this.password.length < 1 || this.email.length < 1 || this.email.match(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/) == null) {
          return
        }
        axios.post('/api/login', {
          email: this.email,
          password: this.password
        }).then(response => {
          if(response.data.message == 'Success'){
            window.location = '/'
            return
          } 
          this.passwordError = response.data.message
        })
      }
    }
}
</script>