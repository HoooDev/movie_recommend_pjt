<template>
  <div class="container">
    <div class="col">
      <div class="card bg-dark text-white">
        <img
          :src="`https://image.tmdb.org/t/p/w200/${genre.poster_path}`"
          class="card-img"
        />
        <div class="card-img-overlay">
          <div class="position-absolute bottom-0 start-50 translate-middle-x">
            <p class="card-text text-center"></p>
            <router-link
              :to="{ name: 'movie', params: { moviePk: genre.pk } }"
              class="
                btn btn-dark
                d-flex
                justify-content-center
                align-items-center
              "
            >
              상세보기 & 리뷰({{ genre.review_count }}) / &nbsp;<i
                class="fa-solid fa-heart fa-1x"
                style="color: red"
              ></i
              >&nbsp;
              {{ genre.like_count }}
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieList",
  props: {
    genre: {
      type: Object,
      required: true,
    },
  },
  methods: {},
};
</script>

<style>
</style>