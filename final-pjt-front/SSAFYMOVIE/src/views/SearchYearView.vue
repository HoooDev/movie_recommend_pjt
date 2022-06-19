<template>
  <div>
    <h1 class="text-center mt-4">원하는 연도는?</h1>
    <div class="d-flex justify-content-center align-items-center">
      <input
        style="width: 500px; height: 35px; font-size: 16px"
        type="number"
        size="4"
        placeholder="1955 ~ 2009"
        min="1955"
        max="2009"
        v-model.trim="year"
        @keyup.enter="onInputValue"
      />
    </div>
    <h3 v-if="whatYear" class="text-center mt-5">
      {{ whatYear }}년도 추천영화
    </h3>
    <div class="container">
      <div class="row">
        <div
          class="col-4 d-flex justify-content-center align-items-center"
          v-for="searchMovie in searchYear"
          :key="searchMovie.Pk"
        >
          <div class="card bg-dark text-white" style="width: 300px">
            <img
              :src="`https://image.tmdb.org/t/p/w200/${searchMovie.poster_path}`"
              class="card-img"
            />
            <div class="card-img-overlay">
              <div
                class="position-absolute bottom-0 start-50 translate-middle-x"
              >
                <p class="card-text text-center"></p>
                <router-link
                  :to="{ name: 'movie', params: { moviePk: searchMovie.pk } }"
                  class="
                    btn btn-dark
                    d-flex
                    justify-content-center
                    align-items-center
                  "
                >
                  상세보기 & 리뷰({{ searchMovie.review_count }}) / &nbsp;<i
                    class="fa-solid fa-heart fa-1x"
                    style="color: red"
                  ></i
                  >&nbsp;
                  {{ searchMovie.like_count }}
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
// import SearchList from "@/components/SearchList.vue";

export default {
  name: "SearchYearView",
  components: {
    // SearchList,
  },
  data: function () {
    return {
      year: "",
      whatYear: "",
    };
  },
  methods: {
    onInputValue: function (event) {
      const newYear = event.target.value;
      this.$store.dispatch("search", newYear);
      this.year = "";
      this.whatYear = event.target.value;
    },
  },
  computed: {
    ...mapGetters(["searchYear", "isSearchYear"]),
    PastYear() {
      return this.searchyear;
    },
  },
};
</script>

<style>
</style>