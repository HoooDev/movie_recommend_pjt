<template>
  <div class="modal">
    <div class="overlay" @click="$emit('closeModal')"></div>
    <div class="modal-card">
      <account-error-list v-if="authError"></account-error-list>
      <div class="container">
        <form @submit.prevent="[signup(credentials), $emit('closeModal')]">
          <div class="mt-2">
            <label class="title-font mx-2" for="username">아이디 </label> <br />
            <input
              v-model="credentials.username"
              type="text"
              id="username"
              required
            />
          </div>
          <div class="mt-2">
            <label class="title-font mx-2" for="password1">비밀번호 </label>
            <br />
            <input
              v-model="credentials.password1"
              type="password"
              id="password1"
              required
            />
          </div>
          <div class="mt-2">
            <label class="title-font mx-2" for="password2"
              >비밀번호 재입력</label
            >
            <br />
            <input
              v-model="credentials.password2"
              type="password"
              id="password2"
              required
            />
          </div>
          <div>
            <button class="btn btn-primary mt-5">회원가입</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import AccountErrorList from "@/components/AccountErrorList.vue";

export default {
  name: "SignupView",
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: "",
        password1: "",
        password2: "",
      },
    };
  },
  computed: {
    ...mapGetters(["authError"]),
  },
  methods: {
    ...mapActions(["signup"]),
  },
};
</script>

<style>
.modal {
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  z-index: 30;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
}
.overlay {
  width: 100%;
  height: 100%;
  position: fixed;
  left: 0;
  top: 0;
}
.overlay {
  opacity: 0.5;
  background-color: black;
}
.modal-card {
  color: black;
  position: relative;
  max-width: 80%;
  margin: auto;
  margin-top: 30px;
  padding: 20px;
  background-color: white;
  min-height: 500px;
  z-index: 10;
  opacity: 1;
}
</style>
