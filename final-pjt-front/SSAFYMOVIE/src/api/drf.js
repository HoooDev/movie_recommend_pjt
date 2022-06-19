const HOST = 'http://localhost:8000/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const REVIEWS = 'reviews/'

// const COMMENTS = 'comments/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },
  movies: {
    // /articles/
    movies: () => HOST + MOVIES,
    // /articles/1/
    movie: moviePk => HOST + MOVIES + `${moviePk}/`,
    likeMovie: moviePk => HOST + MOVIES + `${moviePk}/` + 'like/',
    // 리뷰 생성, 조회
    reviews: moviePk => HOST + MOVIES + `${moviePk}/` + REVIEWS,
    // 리뷰 업데이트 & 삭제
    review: (reviewPk, moviePk) =>
      HOST + MOVIES + `${moviePk}/` + REVIEWS + `${reviewPk}/`,
    genre: () => HOST + MOVIES + 'genre/',
    pastyear: () => HOST + MOVIES + 'pastyear/',
    searchyear: (year) => HOST + MOVIES + 'searchyear/' + `${year}`,
  },
}