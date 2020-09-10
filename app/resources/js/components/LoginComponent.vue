<template>
    <div>
    <HeaderComponent></HeaderComponent>
    <section class="login-section">
      <div class="title-login noselect">Log in</div>
      <form>
        <div class="input-field noselect">
          <input type="text"><label for="mail">Email Address</label>
        </div>
          <div class="input-field noselect">
              <input type="password"><label for="mail">Password</label>
            </div>
            <div class="noselect" style="margin: 20px 0 0 30px; font-size: 13px;">Not a member?<a href="/register">  Sign up here</a> </div>
            <div class="button-submit button" style="width: 80%; margin: 50px 0 0 30px;">
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
import HeaderComponent from './HeaderComponent'
export default {
    components: {
        HeaderComponent
    },
    data() {
        return {
            date: new Date().getFullYear()
        }
    }
}
</script>