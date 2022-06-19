<template>
  <div class="login-page">
    <div class="wallpaper-login">
      <div class="container">
        <div class="row">
          <div class="col-lg-4 col-md-6 col-sm-8 mx-auto">
            <div class="card">
              <form @submit.prevent="onSubmit">
                <div>
                  <label for="title">제목 </label><br />
                  <input v-model="newReview.title" type="text" id="title" />
                </div>
                <div>
                  <label for="content">내용 </label><br />
                  <textarea
                    v-model="newReview.content"
                    type="text"
                    id="content"
                  ></textarea>
                </div>
                <div>
                  <label for="popularity">평점 </label><br />
                  <input
                    v-model="newReview.popularity"
                    type="number"
                    name="score"
                    min="0"
                    max="5"
                    step="0.1"
                  />
                </div>
                <br />
                <div>
                  <button>{{ action }}</button>
                </div>
              </form>
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
  name: "ReviewForm",
  props: {
    review: Array,
    action: String,
  },
  computed: {
    ...mapGetters(["movie"]),
  },
  data() {
    return {
      newReview: {
        title: this.review.title,
        popularity: this.review.popularity,
        content: this.review.content,
      },
    };
  },

  methods: {
    ...mapActions(["createReview", "updateReview"]),
    onSubmit() {
      if (this.action === "생성") {
        console.log(this.movie.pk, this.newReview);
        this.createReview({
          moviePk: this.movie.pk,
          review: this.newReview,
        });
      } else if (this.action === "수정") {
        const payload = {
          reviewPk: this.$route.params.reviewPk,
          moviePk: this.$route.params.moviePk,
          ...this.newReview,
        };
        this.updateReview(payload);
      }
    },
  },
};
</script>

<style>
</style>