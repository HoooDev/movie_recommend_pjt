<template>
  <nav class="navbar navbar-expand-lg sticky-top bg-dark">
    <div class="container-fluid" id="nav-div">
      <router-link class="navbar-brand fw-bold" :to="{ name: 'movies' }"
        >사피 무-비</router-link
      >
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link fw-bold" :to="{ name: 'movies' }"
              >영화</router-link
            >
          </li>
          <li class="nav-item">
            <router-link class="nav-link fw-bold" :to="{ name: 'Genre' }"
              >장르</router-link
            >
          </li>
          <li class="nav-item">
            <router-link class="nav-link fw-bold" :to="{ name: 'searchyear' }"
              >추억 찾기</router-link
            >
          </li>
          <li class="nav-item">
            <router-link class="nav-link fw-bold" :to="{ name: 'pastyear' }"
              >타임머신</router-link
            >
          </li>
        </ul>
        <ul class="navbar-nav">
          <li v-if="isLoggedIn" class="nav-item">
            <router-link
              :to="{ name: 'profile', params: { username } }"
              class="nav-link fw-bold"
            >
              {{ currentUser.username }}'의 공간
            </router-link>
          </li>
          <li v-if="isLoggedIn" class="nav-item">
            <router-link :to="{ name: 'logout' }" class="nav-link fw-bold"
              >로그아웃</router-link
            >
          </li>
          <li v-if="!isLoggedIn" class="nav-item">
            <router-link class="nav-link fw-bold" :to="{ name: 'login' }"
              >로그인</router-link
            >
          </li>
          <li v-if="!isLoggedIn" class="nav-item">
            <button
              style="background: none; border: none"
              @click="isModalViewed = true"
              class="nav-link fw-bold"
            >
              회원가입
            </button>
          </li>
        </ul>
      </div>
      <signup-view v-if="isModalViewed" @closeModal="isModalViewed = false">
      </signup-view>
    </div>
  </nav>
</template>

<script>
import { mapGetters } from "vuex";
import SignupView from "@/views/SignupView.vue";

export default {
  name: "NavBar",
  components: { SignupView },
  data() {
    return {
      isModalViewed: false,
    };
  },
  computed: {
    ...mapGetters(["isLoggedIn", "currentUser"]),
    username() {
      return this.currentUser.username ? this.currentUser.username : "guest";
    },
  },
};
</script>

<style>
@font-face {
  font-family: "국립박물관문화재단클래식B";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_twelve@1.0/국립박물관문화재단클래식B.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
nav a {
  color: white;
}
.nav-link {
  color: white;
}
* {
  font-family: "국립박물관문화재단클래식B";
}
</style>
