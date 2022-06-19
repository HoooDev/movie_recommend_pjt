<template>
  <div class="container">
    <div class="row">
      <vue-glide
        v-if="genres.length"
        class="glide__track"
        data-glide-el="track"
        ref="slider"
        type="slider"
        :autoplay="true"
        :animationDuration="1500"
        :breakpoints="{
          3000: { perView: 3 },
          991: { perView: 2 },
          800: { perView: 1 },
        }"
      >
        <vue-glide-slide v-for="(genre, idx) in genres" :key="idx">
          <movie-list class="align-items-center" :genre="genre" />
        </vue-glide-slide>
      </vue-glide>
    </div>
  </div>
</template>

<script>
import { Glide, GlideSlide } from "vue-glide-js";
import MovieList from "./MovieList.vue";
export default {
  name: "GenreMovies",
  props: {
    genres: {
      type: Array,
      required: true,
    },
  },
  components: {
    MovieList,
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide,
  },
  methods: {},
};
</script>

<style>
</style>