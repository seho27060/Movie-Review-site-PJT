import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

export default {
  state: {
    movies: [],
    movie: {},
    rating: null,
    ratingPk : null,
  },
  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    rating: state => state.rating,
    ratingPk: state => state.ratingPk,

    // isAuthor: (state, getters) => {
    //   return state.article.user?.username === getters.currentUser.username
    // },
    // isArticle: state => !_.isEmpty(state.article),
  },

  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_RATING: (state, rating) => state.rating = rating,
    SET_RATINGPK: (state, ratingPk) => state.ratingPk = ratingPk,
    SET_MOVIE_RATINGS: (state, ratings) => (state.movies.ratings = ratings),
  },

  actions: {
    fetchMovies({ commit, getters }) {
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
        .then((res)=>{
          commit('SET_MOVIE', res.data)
          console.log(res.data, getters.rating, getters.ratingPk)
          console.log(res.data.rating)
          let check = true
          for (const el of res.data.ratings) {
            if (el.user.pk === getters.currentUser.pk){
              console.log(el.rating,el.pk)
              commit('SET_RATING', el.rating)
              commit('SET_RATINGPK', el.pk)
              check = false
              break
            }
          }
          if(check){
            commit('SET_RATING', null)
            commit('SET_RATINGPK', null)
          }
        }
        )
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
          const ratingdata = res.data[0]
          console.log('create',res,res.data[0].pk)
          // commit('SET_RATING', res.data.rating)
          commit('SET_MOVIE_RATINGS', res.data)
          commit('SET_RATINGPK', ratingdata.pk)
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
        const ratingdata = res.data[0]
        // console.log("up",res, res.data[0], ratingdata.pk)
        // commit('SET_RATING', res.data.rating)
        commit('SET_MOVIE_RATINGS', res.data)
        commit('SET_RATINGPK', ratingdata.pk)
      })
      .catch(err => console.log(err.response))
    },
    
    ratingDelete({ commit, getters }, { moviePk, ratingPk}) {
      console.log("store delete rating")
      axios({
        url: drf.movies.ratingModify(moviePk, ratingPk),
        method: 'delete',
        headers: getters.authHeader,
      })
      .then(res => {
        console.log(res)
        // commit('SET_RATING', res.data.rating)
        commit('SET_MOVIE_RATINGS', res.data)
        commit('SET_RATINGPK', null)
      })
      .catch(err => console.error(err.response))
    },
  },

  
}