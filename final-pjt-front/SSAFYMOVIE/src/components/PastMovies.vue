<template>
  <div class="container">
    <div class="row">
      <vue-glide
        v-if="movies.length"
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
        <vue-glide-slide
          class="align-items-center"
          v-for="(movie, idx) in movies"
          :key="idx"
        >
          <past-movie-item :movie="movie" />
        </vue-glide-slide>
      </vue-glide>
    </div>
  </div>
</template>

<script>
import { Glide, GlideSlide } from "vue-glide-js";
import PastMovieItem from "./PastMovieItem.vue";
export default {
  name: "PastMovies",
  props: {
    movies: {
      type: Array,
      required: true,
    },
  },
  components: {
    PastMovieItem,
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide,
  },
  methods: {},
};
</script>

<style>
</style>