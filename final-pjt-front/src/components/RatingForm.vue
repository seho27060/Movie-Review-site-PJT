<template>
  <div class="container">
    <b-input-group>
      <b-input-group-prepend>
        <b-button @click="rating = 0">Clear</b-button>
      </b-input-group-prepend>
      <b-form-rating @click="onSubmit" v-model="rating" color="#ff8800"></b-form-rating>
      <b-input-group-append>
        <b-input-group-text class="justify-content-center" style="min-width: 3em;">
          {{ rating }}
        </b-input-group-text>
      </b-input-group-append>
    </b-input-group>
    <p>{{ movie }}</p>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'RatingForm',
  props:{
    movie:Object
  },
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
    ...mapActions(['ratingCreate', 'ratingUpdate', 'ratingDelete']),
    onSubmit () {
      if (this.rating === null) {
        this.ratingCreate({ moviePk: this.movie.pk, rating: this.rating})
      } else if (this.rating === 0) {
        this.ratingDelete()
        this.rating = null
      } else {
        this.ratingUpdate({moviePk: this.movie.pk, ratingPk: this.ratingPk, rating: this.rating})
      }
    },
    checkRating(){
      console.log()
      for (const rating of this.movie.ratings) {
        if (rating.user.pk === this.currentUser.pk){
          this.ratingPk = rating.pk
          break
        }
      }
      console.log(this.ratingPk, typeof(this.ratingPk))
    },
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