import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

export default {
  state: {
    movies: [],
    movie: {},
  },
  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    // isAuthor: (state, getters) => {
    //   return state.article.user?.username === getters.currentUser.username
    // },
    // isArticle: state => !_.isEmpty(state.article),
  },

  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_MOVIE_RATINGS: (state, ratings) => (state.movies.ratings = ratings),
  },

  actions: {
    fetchMovies({ commit, getters }) {
      console.log(drf.movies.movies(),getters.authHeader)
      axios({
        url: drf.movies.movies(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIES', res.data)
        })
        .catch(err => {
          console.error(err.response)
        })
    },

    fetchMovie({ commit, getters }, moviePk) {
      axios({
        url: drf.movies.movie(moviePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },

    ratingCreate({ commit, getters }, { moviePk, rating }) {

      const score = { rating }
      
      axios({
        url: drf.movies.rating(moviePk),
        method: 'post',
        data: score,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_RATINGS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    ratingUpdate({ commit, getters }, { moviePk, ratingPk, rating }) {

      const score = { rating }

      axios({
        url: drf.movies.ratingModify(moviePk, ratingPk),
        method: 'put',
        data: score,
        headers: getters.authHeader,
      })
      .then(res => {
        commit('SET_MOVIE_RATINGS', res.data)
      })
      .catch(err => console.log(err.response))
    }
  },

  
}