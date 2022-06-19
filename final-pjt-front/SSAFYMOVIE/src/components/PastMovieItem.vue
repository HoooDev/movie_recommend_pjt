<template>
  <div class="card bg-dark text-white">
    <img
      :src="`https://image.tmdb.org/t/p/w200/${movie.poster_path}`"
      class="card-img"
    />
    <div class="card-img-overlay">
      <div class="position-absolute bottom-0 start-50 translate-middle-x">
        <p class="card-text text-center"></p>
        <router-link
          :to="{ name: 'movie', params: { moviePk: movie.pk } }"
          class="btn btn-dark d-flex justify-content-center align-items-center"
        >
          상세보기 & 리뷰({{ movie.review_count }}) / &nbsp;<i
            class="fa-solid fa-heart"
            style="color: red"
          ></i
          >&nbsp;
          {{ movie.like_count }}
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PastMovieItem",
  props: {
    movie: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style>
</style>