<template>
  <div>
    <h1 class="text-center mt-5">영화</h1>
    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-4 mx-5">
      <div class="col" v-for="movie in movies" :key="movie.pk">
        <div class="card bg-dark text-white">
          <img
            :src="`https://image.tmdb.org/t/p/w200/${movie.poster_path}`"
            class="card-img"
            height="420"
            width="350"
          />
          <div class="card-img-overlay">
            <div class="position-absolute bottom-0 start-50 translate-middle-x">
              <p class="card-text text-center"></p>
              <router-link
                :to="{ name: 'movie', params: { moviePk: movie.pk } }"
                class="
                  btn btn-dark
                  d-flex
                  justify-content-center
                  align-items-center
                "
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
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "MovieListView",
  computed: {
    ...mapGetters(["movies"]),
  },
  methods: {
    ...mapActions(["fetchMovies"]),
  },
  created() {
    this.fetchMovies();
  },
};
</script>

<style>
.card {
  display: flex;
  justify-content: space-between;
  margin: 0 70px;
  margin-top: 30px;
  flex-wrap: wrap;
  color: black;
}

.btn {
  width: 245px;
  height: 40px;
}
</style>