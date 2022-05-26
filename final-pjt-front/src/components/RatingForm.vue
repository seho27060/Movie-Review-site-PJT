<template>
  <div class="container">
    <b-input-group>
      <b-input-group-prepend>
        <b-button @click="deleteRating">Clear</b-button>
      </b-input-group-prepend>
      <b-form-rating @change="onSubmit()" v-model="rating" color="#ff8800"></b-form-rating>
      <b-input-group-append>
        <b-input-group-text class="justify-content-center" style="min-width: 3em;">
          {{ rating }}
        </b-input-group-text>
      </b-input-group-append>
    </b-input-group>
    <!-- <b-button>{{ ratingScore }}</b-button> -->
    <!-- {{ movie.ratings}}
    {{  movie.rating.length}} -->
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'RatingForm',
  computed: {
    ...mapGetters(['movie','currentUser']),
    rating: {
      get(){
        return this.$store.getters.rating
      },
      set(value){
        this.$store.commit("SET_RATING",value)
      }
    },
    ratingPk: {
      get(){
        return this.$store.getters.ratingPk
      },
      set(value){
        this.$store.commit("SET_RATINGPK",value)
      }
    },

  },
  methods: {
    ...mapActions(['ratingCreate', 'ratingUpdate', 'ratingDelete']),

    deleteRating () {
      console.log("delete",this.movie.pk,this.ratingPk)
        // this.ratingDelete({moviePk: this.movie.pk, ratingPk: this.ratingPk})
        this.rating = 0
        this.ratingDelete({ moviePk: this.movie.pk, ratingPk: this.ratingPk})
    },
    onSubmit () {
      console.log('onsiub')
        if (this.ratingPk === null) 
        {
          console.log('crate',this.movie.pk,this.rating, this.ratingPk)
          this.ratingCreate({ moviePk: this.movie.pk, rating: this.rating})
        } else
        {
          console.log('update',this.movie.pk,this.rating, this.ratingPk)
          this.ratingUpdate({moviePk: this.movie.pk, ratingPk: this.ratingPk, rating: this.rating})
        }
      },
      
  },
}
</script>

<style>
.comment-list-form {
  border: 1px solid black;
  margin: 1rem;
  padding: 1rem;
}
</style>