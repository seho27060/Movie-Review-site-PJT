<template>
  <form @submit.prevent="onSubmit" class="rating-form">
    <label for="rating">rating: </label>
    <input type="float" id="rating" v-model="rating" required>
    <button>Complete</button>
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'RatingForm',
  data() {
    return {
      rating: null
    }
  },
  computed: {
    ...mapGetters(['movie']),
  },
  methods: {
    ...mapActions(['createRating']),
    onSubmit() {
      this.createRating({ moviePk: this.movie.pk, rating: this.rating, })
      this.rating = ''
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