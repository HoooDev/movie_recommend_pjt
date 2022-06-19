<template>
  <div v-if="isPastMovies">
    <h1 class="title-font text-center mt-5">2000'무-비</h1>
    <past-movies :movies="Movies2000" />
    <h1 class="title-font text-center mt-5">1990'무-비</h1>
    <past-movies :movies="Movies1990" />
    <h1 class="title-font text-center mt-5">1980'무-비</h1>
    <past-movies :movies="Movies1980" />
    <h1 class="title-font text-center mt-5">1970'무-비</h1>
    <past-movies :movies="Movies1970" />
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import PastMovies from "@/components/PastMovies.vue";

export default {
  components: { PastMovies },
  name: "PastYear",
  computed: {
    ...mapGetters(["pastMovies", "isPastMovies"]),
    Movies2000() {
      return this.pastMovies[0];
    },
    Movies1990() {
      return this.pastMovies[1];
    },
    Movies1980() {
      return this.pastMovies[2];
    },
    Movies1970() {
      return this.pastMovies[3];
    },
  },
  methods: {
    ...mapActions(["fetchPastMovies"]),
  },
  created() {
    this.fetchPastMovies();
  },
};
</script>

<style>
</style>