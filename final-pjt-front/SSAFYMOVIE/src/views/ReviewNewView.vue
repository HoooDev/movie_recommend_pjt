<template>
  <div>
    <h1 class="text-center mt-5">리뷰 생성</h1>
    <review-form :review="review" action="생성"></review-form>
  </div>
</template>

<script>
import ReviewForm from "@/components/ReviewForm.vue";
export default {
  name: "ReviewNewView",
  components: { ReviewForm },
  data() {
    return {
      review: {
        pk: null,
        title: "",
        popularity: null,
        content: "",
      },
    };
  },
};
</script>

<style>
</style>