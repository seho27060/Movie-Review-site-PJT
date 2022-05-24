<template>

  <form @submit.prevent="onSubmit" class="rating-form">
    <!-- <label for="rating">rating: </label>
    <input type="float" id="rating" v-model="rating" required> -->
    <b-form-rating v-model="rating" stars="5"></b-form-rating>
    <p class="mt-1">Value: {{ rating }}</p>
    <button>Complete</button>
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'RatingForm',
  data() {
    return {
      rating: null,
      value : null,
    }
  },
  computed: {
    ...mapGetters(['movie']),

  },
  methods: {
    ...mapActions(['createRating']),
    onSubmit() {
      const rating = this.rating
      if (typeof (rating) === typeof (0.1)) {
        console.log(this.movie,this.rating)
        this.createRating({ moviePk: this.movie.pk, rating: this.rating, })
        this.rating = null
      } else{
        alert("잘못된 입력입니다.")
      }
    }
  }
}
</script>

<style>
.comment-list-form {
  border: 1px solid black;
  margin: 1rem;
  padding: 1rem;
}
</style>