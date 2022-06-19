import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'

import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'
import ProfileView from '@/views/ProfileView.vue'
import MovieListView from '@/views/MovieListView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import NotFound404 from '../views/NotFound404.vue'
import ReviewNewView from '@/views/ReviewNewView.vue'
import ReviewEditView from '@/views/ReviewEditView.vue'
import GenreView from '@/views/GenreView.vue'
import PastYear from '@/views/PastYearView.vue'
import SearchYear from '@/views/SearchYearView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView,
  },
  {
    path: '/',  // Home
    name: 'movies',
    component: MovieListView
  },
  {
    path: '/movies/pastyear',
    name: 'pastyear',
    component: PastYear
  },
  {
    path: '/movies/searchyear',
    name: 'searchyear',
    component: SearchYear
  },
  {
    path: '/movies/genre',
    name: 'Genre',
    component: GenreView
  },
  // 영화 디테일
  {
    path: '/movies/:moviePk',
    name: 'movie',
    component: MovieDetailView
  },
  // 영화 리뷰 작성
  {
    path: '/movies/:moviePk/reviews',
    name: 'review',
    component: ReviewNewView
  },
  {
    path: '/movies/:moviePk/reviews/edit',
    name: 'reviewEdit',
    component: ReviewEditView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },


]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  store.commit('SET_AUTH_ERROR', null)

  const { isLoggedIn } = store.getters

  const noAuthPages = ['login', 'signup']

  const isAuthRequired = !noAuthPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    alert('Require Login. Redirecting..')
    next({ name: 'login' })
  } else {
    next()
  }

  if (!isAuthRequired && isLoggedIn) {
    next({ name: 'movies' })
  }
})

export default router

