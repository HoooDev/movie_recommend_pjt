<template>
  <div v-if="isGenre">
    <h1 class="title-font text-center mt-5">액션 무-비</h1>
    <genre-movies :genres="actionMovies" />
    <h1 class="title-font text-center mt-5">만화</h1>
    <genre-movies :genres="animationMovies" />
    <h1 class="title-font text-center mt-5">스릴러 무-비</h1>
    <genre-movies :genres="horrorMovies" />
    <h1 class="title-font text-center mt-5">달달한 무-비</h1>
    <genre-movies :genres="romanceMovies" />
    <h1 class="title-font text-center mt-5">공상과학 무-비</h1>
    <genre-movies :genres="sfMovies" />
    <h1 class="title-font text-center mt-5">웃긴 무-비</h1>
    <genre-movies :genres="comedyMovies" />
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import GenreMovies from "@/components/GenreMovies.vue";

export default {
  components: { GenreMovies },
  name: "GenreView",
  computed: {
    ...mapGetters(["genre", "isGenre"]),
    actionMovies() {
      return this.genre[0];
    },
    animationMovies() {
      return this.genre[1];
    },
    horrorMovies() {
      return this.genre[2];
    },
    romanceMovies() {
      return this.genre[3];
    },
    sfMovies() {
      return this.genre[4];
    },
    comedyMovies() {
      return this.genre[5];
    },
  },
  methods: {
    ...mapActions(["fetchGenre"]),
  },
  created() {
    this.fetchGenre();
  },
};
</script>

<style>
</style>