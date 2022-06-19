<template>
  <div v-if="isMovie">
    <div class="container">
      <div class="d-flex justify-content-around">
        <img
          :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`"
          class="d-block my-4"
          height="450"
          width="350"
        />
        <div class="col-6 d-flex align-items-center">
          <div>
            <h4 class="text-center mt-4">{{ movie.title }}</h4>
            <h6 class="text-center">{{ movie.original_title }}</h6>
            <h6 class="text-center">{{ movie.release_date }}</h6>

            <p class="text-center">{{ movie.genre }}</p>
            <p class="text-center" @click="likeMovie(moviePk)">
              <i class="fa-solid fa-heart" style="color: red"></i>
              {{ likeCount }}
            </p>
            <hr />
            <p>{{ movie.overview }}</p>
          </div>
        </div>
      </div>
      <router-link
        :to="{ name: 'review', params: { moviePk } }"
        class="btn btn-dark"
        >리뷰 작성</router-link
      >
      <div v-for="(review, index) in movie.reviews" :key="review.pk">
        <ol class="list-group">
          <div>
            <li
              class="
                list-group-item
                d-flex
                justify-content-between
                align-items-center
              "
            >
              <div class="ms-2 me-auto">
                {{ index + 1 }}.&nbsp;&nbsp;{{ review.title }}
                <br />
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ review.content }}
              </div>

              <span class="badge bg-dark rounded-pill"
                >★&nbsp;{{ review.popularity }}</span
              >
              <div v-if="currentUser.username === review.user.username">
                <span
                  >&nbsp;<button @click="deleteReview2(review.pk)">
                    삭제
                  </button></span
                >&nbsp;
                <router-link
                  :to="{ name: 'reviewEdit', params: { reviewPk: review.pk } }"
                  ><button>수정</button></router-link
                >
              </div>
            </li>
          </div>
        </ol>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
// import ReviewList from "@/components/ReviewList.vue";

export default {
  name: "MovieDetailView",
  components: {},
  data() {
    return {
      moviePk: this.$route.params.moviePk,
    };
  },
  computed: {
    ...mapGetters(["movie", "isAuthor", "isMovie", "review", "currentUser"]),
    likeCount() {
      return this.movie.like_users?.length;
    },
  },
  methods: {
    ...mapActions(["fetchMovie", "likeMovie", "deleteReview"]),
    deleteReview2(reviewPk) {
      const payload = {
        reviewPk: reviewPk,
        moviePk: this.moviePk,
      };
      return this.deleteReview(payload);
    },
  },
  created() {
    this.fetchMovie(this.moviePk);
  },
};
</script>

<style>
</style>