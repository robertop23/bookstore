import colors from 'vuetify/es5/util/colors'

export default {
  router: {
    base: '/'
  },
  mode: 'spa',
  /*
   ** Headers of the page
   */
  head: {
    titleTemplate: '%s',
    title: 'EbookStore',
    meta: [{
      charset: 'utf-8'
    },
    {
      name: 'viewport',
      content: 'width=device-width, initial-scale=1'
    },
    {
      hid: 'description',
      name: 'description',
      content: process.env.npm_package_description || ''
    }
    ]
  },
  /*
   ** Customize the progress-bar color
   */
  loading: {
    color: '#fff'
  },
  /*
   ** Global CSS
   */
  css: [{
    src: '~/plugins/icons.js',
    ssr: false
  }],
  /*
   ** Plugins to load before mounting the App
   */
  plugins: [
    '@/plugins/axios',
    '@/plugins/notifier',
    '@/plugins/base'
  ],
  /*
   ** Nuxt.js dev-modules
   */
  buildModules: [
    // Doc: https://github.com/nuxt-community/eslint-module
    '@nuxtjs/eslint-module',
    '@nuxtjs/vuetify'
  ],
  /*
   ** Nuxt.js modules
   */
  // Doc: https://axios.nuxtjs.org/usage
  modules: ['@nuxtjs/axios', '@nuxtjs/auth'],
  /*
   ** Axios module configuration
   ** See https://axios.nuxtjs.org/options
   */
  axios: {
    baseURL: 'http://127.0.0.1:8000/'
  },
  /*
   ** vuetify module configuration
   ** https://github.com/nuxt-community/vuetify-module
   */
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: false,
      iconfont: 'fa',
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3
        }
      }
    }
  },

  auth: {
    strategies: {
      local: {
        endpoints: {
          login: {
            url: '/auth/jwt/create/',
            method: 'post',
            propertyName: 'access'
          },
          user: {
            url: '/auth/users/me/',
            method: 'get',
            propertyName: false
          },
          logout: false
        },
        tokenType: 'JWT'
      }
    },
    redirect: {
      login: '/auth/login',
      logout: '/',
      home: '/'
    }
  },

  /*
   ** Build configuration
   */
  build: {
    /*
     ** You can extend webpack config here
     */
    extend (config, ctx) {}
  }
}
