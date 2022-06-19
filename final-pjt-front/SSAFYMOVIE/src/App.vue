<template>
  <div id="app">
    <nav-bar></nav-bar>
    <router-view></router-view>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";

import { mapActions } from "vuex";

export default {
  name: "App",
  components: { NavBar },
  methods: {
    ...mapActions(["fetchCurrentUser"]),
  },
  created() {
    this.fetchCurrentUser();
  },
};
</script>

<style>
#app {
  color: rgb(255, 255, 255);
}

body {
  background-image: url("@/assets/bg3.png");
  background-size: cover;
  background-attachment: fixed;
  background-repeat: no-repeat;
  width: 100%;
  height: 100%;
}
</style>
