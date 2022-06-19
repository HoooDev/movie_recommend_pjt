<template>
  <div>
    <h1 class="text-center mt-5">리뷰 수정</h1>
    <review-form :review="review" action="수정"></review-form>
  </div>
</template>

<script>
import ReviewForm from "@/components/ReviewForm.vue";
import { mapActions, mapGetters } from "vuex";

export default {
  name: "ReviewEditView",
  components: { ReviewForm },
  data() {
    return {
      payload: {
        moviePk: this.$route.params.moviePk,
      },
    };
  },
  computed: {
    ...mapGetters(["review"]),
  },
  methods: {
    ...mapActions(["fetchReview"]),
  },
  created() {
    this.fetchReview(this.payload);
  },
};
</script>

<style></style>
