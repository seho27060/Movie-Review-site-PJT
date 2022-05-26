<template>
  <div class="container">
    <h4>좋아하는 장르를 골라주세요</h4>
    <b-form-group v-slot="{ ariaDescribedby }">
      <br>
      <b-form-checkbox-group
        id="checkbox-group-1"
        v-model="selected"
        :options="options"
        :aria-describedby="ariaDescribedby"
        name="flavour-1"
      ></b-form-checkbox-group>
    </b-form-group>
    <br>
    <b-button @click="recommend" variant="primary">영화추천 받기</b-button>

    <hr>
    <div class="row">
      <movie-list-item v-for="movie in movies" :key="movie.pk" :movie="movie" class="col-3">
      </movie-list-item>
    </div>
  </div>
</template>

<script>
import { mapGetters  } from 'vuex'
import axios from 'axios'
import drf from '@/api/drf'
import MovieListItem from '@/components/MovieListItem.vue'

export default {
  name: 'movieRecommendList',
  components: {
    MovieListItem,
  },
  data() {
    return {
        selected: [], // Must be an array reference!
        options: [
          { text: '모험', value: '12' },
          { text: '판타지', value: '14' },
          { text: '애니메이션', value: '16' },
          { text: '드라마', value: '18' },
          { text: '공포', value: '27' },
          { text: '액션', value: '28' },
          { text: '코미디', value: '35' },
          { text: '역사', value: '36' },
          { text: '서부', value: '37' },
          { text: '스릴러', value: '53' },
          { text: '범죄', value: '80' },
          { text: '다큐멘터리', value: '99' },
          { text: 'SF', value: '878' },
          { text: '미스터리', value: '9648' },
          { text: '음악', value: '10402' },
          { text: '로맨스', value: '10749' },
          { text: '가족', value: '10751' },
          { text: '전쟁', value: '10752' },
          { text: 'TV 영화', value: '10770' },
        ],
        movies: [],
      }
  },
  computed: {
    ...mapGetters(['authHeader']),
  },
  methods:{
    recommend(){
      const genres = this.selected
      console.log(genres,this.authHeader)
      axios({
        url: drf.movies.recommend(),
        method: 'post',
        data : this.selected,
        headers: this.authHeader,
      })
      .then(res => {
        console.log(res)
        this.movies = res.data
      })
      .catch(err => console.error(err.response))
    },
    }
  }
</script>

<style>

</style>