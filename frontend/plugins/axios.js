const EXPIRED_TOKEN_MESSAGE = 'Expired JWT Token'

export default function ({
  $axios,
  redirect,
  app,
  store,
  router
}) {
  $axios.setHeader('Content-Type', 'application/json')
  $axios.setHeader('Accept', 'application/json')

  $axios.onRequest((config) => {})

  $axios.onError((error) => {
    if (error.message === EXPIRED_TOKEN_MESSAGE) {
      // store.dispatch('authentication/logout')
    } else if (error.response.status === 401) {
      // Unauthorized
      redirect('/auth/login')
    } else {}

    store.dispatch('/auth/login', {})

    return false
  })
}
