<template>
  <div>
    <h1>{{ movie.title }}</h1>
    <p>{{ movie.overview }}</p>
    <rating-form :movie = "movie"></rating-form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import RatingForm from '@/components/RatingForm.vue'

export default {
  name:"MovieDetail",
  components:{
    RatingForm,
  },
  data() {
    return {
      moviePk: this.$route.params.moviePk,
      ratingPk : null,
    }
  },
  computed: {
    ...mapGetters(['movie', 'currentUser']),
  },
  methods: {
    ...mapActions([
      'fetchMovie',
    ]),
  },
  created(){
    this.fetchMovie(this.moviePk)
  },
}
</script>

<style>

</style>