<template>
  <div class="login-page">
    <div class="wallpaper-login">
      <h1 class="text-center" style="color: white">로그인</h1>
      <account-error-list v-if="authError"></account-error-list>
      <div class="container">
        <div class="row">
          <div class="col-lg-4 col-md-6 col-sm-8 mx-auto">
            <div class="card">
              <form class="form-group" @submit.prevent="login(credentials)">
                <div>
                  <label for="username">아이디 </label>
                  <input
                    v-model="credentials.username"
                    type="text"
                    id="username"
                    required
                  />
                </div>

                <div>
                  <label for="password">비밀번호 </label>
                  <input
                    v-model="credentials.password"
                    type="password"
                    id="password"
                    required
                  />
                </div>

                <button class="mt-5 btn btn-primary">로그인</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import AccountErrorList from "@/components/AccountErrorList.vue";

export default {
  name: "LoginView",
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: "",
        password: "",
      },
    };
  },
  computed: {
    ...mapGetters(["authError"]),
  },
  methods: {
    ...mapActions(["login"]),
  },
};
</script>

<style>
.card {
  padding: 20px;
}

.form-group {
  margin-bottom: 20;
}

.login-page {
  align-items: center;
  display: flex;
  height: 100vh;
}
.wallpaper-login {
  background-size: cover;
  height: 100%;
  position: absolute;
  width: 100%;
}
</style>
