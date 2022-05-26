<template>
  <div class="container">
    <b-card no-body class="overflow-hidden" id="card">
      <b-row no-gutters>
        <b-col md="6">
          <b-card-img :src=poster_path alt="Image" class="rounded-0"></b-card-img>
        </b-col>
        <b-col md="6">
          <b-card-body :title=movie.title><hr>
            <b-card-text>
              <strong>개봉일</strong><br><br>
              {{ releaseDate }}
            </b-card-text><hr>
            <b-card-text>
              <strong>장르</strong><br><br>
              {{ genres }}
            </b-card-text><hr>
            <b-card-text>
              <strong>줄거리</strong><br><br>
              {{ movie.overview }}
            </b-card-text><hr>
            <b-card-text>
              <strong>{{ movie.title }}의 평점을 입력해주세요</strong><br><br>
              <rating-form></rating-form>
            </b-card-text>
          </b-card-body>
        </b-col>
      </b-row>
    </b-card>
    
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
    }
  },
  computed: {
    ...mapGetters(['movie', 'currentUser', 'rating']),
    poster_path () {
            return 'https://image.tmdb.org/t/p/original/' + this.movie.poster_path
        },
    releaseDate () {
      return this.movie.release_date.substr(0,10)
    },
    genres () {
      const genres = this.movie.genre_ids.map((genre) => {
        return genre["name"]
      })
      return genres
    },

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
#card {
  width: 900px;
}
</style>