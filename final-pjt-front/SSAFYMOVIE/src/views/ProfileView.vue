<template>
  <div>
    <h1 class="text-center mt-5">{{ profile.username }}'의 공간</h1>
    <h3 class="text-center mt-5">작성한 리뷰</h3>
    <div
      class="container d-flex justify-content-center align-items-center mt-5"
    >
      <div class="col-8">
        <ul class="list-group">
          <li
            class="
              list-group-item list-group-item-action list-group-item-light
              text-center
            "
            v-for="review in profile.reviews"
            :key="review.pk"
          >
            제목 : {{ review.title }} <br />
            내용 : {{ review.content }} <br />
            <router-link
              :to="{ name: 'movie', params: { moviePk: review.movie } }"
              class="btn btn-primary mt-3"
              >바로가기</router-link
            >
          </li>
        </ul>
      </div>
    </div>

    <h3 class="text-center mt-5">찜한 영화</h3>
    <div
      class="container mt-5 d-flex justify-content-center align-items-center"
    >
      <div class="col-8">
        <ul class="list-group">
          <li
            class="list-group-item text-center"
            v-for="like_movie in profile.like_movies"
            :key="like_movie.pk"
          >
            {{ like_movie.title }} / {{ like_movie.genre }} <br />
            <router-link
              :to="{ name: 'movie', params: { moviePk: like_movie.id } }"
              class="btn btn-primary mt-3"
              >바로가기</router-link
            >
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "ProfileView",
  computed: {
    ...mapGetters(["profile"]),
  },
  methods: {
    ...mapActions(["fetchProfile"]),
  },
  created() {
    const payload = { username: this.$route.params.username };
    this.fetchProfile(payload);
  },
};
</script>
