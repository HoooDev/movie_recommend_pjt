import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'
import _ from 'lodash'

export default {
  state: {
    movies: [],
    movie: {},
    review: {},
    genre: [],
    pastMovies: [],
    searchyear: [],
  },

  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    isAuthor: (state, getters) => {
      return state.movie.user?.username === getters.currentUser.username
    },
    isMovie: state => !_.isEmpty(state.movie),
    genre: state => state.genre,
    isGenre: state => !_.isEmpty(state.genre),
    pastMovies: state => state.pastMovies,
    isPastMovies: state => !_.isEmpty(state.pastMovies),
    review: state => state.review,
    searchYear: state => state.searchyear,
    isSearchYear: state => !_.isEmpty(state.searchyear)
  },

  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_REVIEW: (state, review) => (state.movie.review = review),
    SET_GENRE: (state, genre) => (state.genre = genre),
    SET_PASTMOVIES: (state, pastMovies) => (state.pastMovies = pastMovies),
    SET_SEARCH: (state, searchmovies) => (state.searchyear = searchmovies)
  },

  actions: {
    fetchMovies({ commit, getters }) {
      axios({
        url: drf.movies.movies(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIES', res.data))
        .catch(err => console.error(err.response))
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
    fetchReview({ commit, getters }, { moviePk }) {
      console.log(moviePk)
      axios({
        url: drf.movies.reviews(moviePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_REVIEW', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },

    fetchGenre({ commit, getters }) {
      axios({
        url: drf.movies.genre(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_GENRE', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },
    fetchPastMovies({ commit, getters }) {
      axios({
        url: drf.movies.pastyear(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_PASTMOVIES', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },
    search({ commit, getters }, year) {
      // commit('SET_SEARCHYEAR', year)
      if (year <= 2009 && year >= 1950) {
        axios({
          url: drf.movies.searchyear(year),
          method: 'get',
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_SEARCH', res.data)
            // router.push({ name:'search' })
          })
          .catch(err => {
            console.error(err.response)
            if (err.response.status === 404) {
              router.push({ name: 'NotFound404' })
            }
          })
      }
      else {
        alert('1950~2009년 사이의 연도를 입력해주세요.')
      }
    },
    likeMovie({ commit, getters }, moviePk) {

      axios({
        url: drf.movies.likeMovie(moviePk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => console.error(err.response))
    },

    createReview({ commit, getters }, { moviePk, review }) {

      console.log(moviePk, review)
      axios({
        url: drf.movies.reviews(moviePk),
        method: 'post',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW', res.data)
          router.push({
            name: 'movie',
            params: { moviePk: getters.movie.pk }
          })
        })
    },

    updateReview({ commit, getters }, { reviewPk, moviePk, title, content, popularity }) {
      axios({
        url: drf.movies.review(reviewPk, moviePk),
        method: 'put',
        data: { title, content, popularity },
        headers: getters.authHeader,
      })
        .then(res => {
          console.log(res)
          commit('SET_REVIEW', res.data)
          router.push({
            name: 'movie',
            params: { moviePk: getters.movie.pk }
          })
        })
    },
    deleteReview({ getters, dispatch }, { reviewPk, moviePk }) {

      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.movies.review(reviewPk, moviePk),
          method: 'delete',
          headers: getters.authHeader,
        })
          .then(() => {
            dispatch('fetchMovie', moviePk)
          })
          .catch(err => console.error(err.response))
      }
    },

  },
}