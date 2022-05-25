<template>
  <div class="container">
    <b-input-group>
      <b-input-group-prepend>
        <b-button @click="rating = 0">Clear</b-button>
      </b-input-group-prepend>
      <b-form-rating @change="onSubmit" v-model="rating" color="#ff8800"></b-form-rating>
      <b-input-group-append>
        <b-input-group-text class="justify-content-center" style="min-width: 3em;">
          {{ rating }}
        </b-input-group-text>
      </b-input-group-append>
    </b-input-group>
    <p>{{ movie.ratings }}</p>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'RatingForm',
  data(){
    return{
      rating: null,
    }
  },
  computed: {
    ...mapGetters(['movie','currentUser','ratingPk']),
  },
  methods: {
    ...mapActions(['ratingCreate', 'ratingUpdate', 'ratingDelete']),
    onSubmit () {
      console.log('onsiub')
      if (!this.ratingPk) {
        console.log('crate')
        this.ratingCreate({ moviePk: this.movie.pk, rating: this.rating})
      } else if (this.rating === 0) {
        console.log('delete')
        this.ratingDelete()
        this.rating = null
      } else {
        console.log('update')
        this.ratingUpdate({moviePk: this.movie.pk, ratingPk: this.ratingPk, rating: this.rating})
      }
    },

  },
  created(){
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