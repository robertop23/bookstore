<template>
  <v-app id="login" class="primary">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4 lg4>
            <v-card class="elevation-1 pa-4">
              <v-card-text>
                <div class="layout column align-center">
                  <img id="bookstore_logo" src="~/static/bookstore_logo.png" alt="Book Store">
                </div>
                <v-form>
                  <v-text-field v-model="model.username" append-icon="fa-user" name="login" label="Login" type="text" />
                  <v-text-field
                    id="password"
                    v-model="model.password"
                    append-icon="fa-unlock"
                    name="password"
                    label="Password"
                    type="password"
                  />
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-btn :loading="loading" block color="primary" @click="login">
                  Login
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
    <snackbar />
  </v-app>
</template>

<script>
export default {
  components: {
    Snackbar: () => import('@/components/core/Snackbar')
  },
  auth: false,
  layout: 'empty',
  data () {
    return {
      loading: false,
      model: {
        username: 'userconsumer',
        password: '1212pass'
      }
    }
  },

  methods: {
    async login () {
      this.loading = true
      try {
        await this.$auth.loginWith('local', {
          data: {
            username: this.model.username,
            password: this.model.password
          }
        })
        if (this.$auth.loggedIn) {
          const currentUser = Object.assign(this.$auth.user)
          this.$auth.setUser(currentUser)
        }
        this.$router.push('/')
      } catch (e) {
        this.error = e.response.data.detail
        this.$notifier.showMessage({ content: this.error, color: 'error' })
      }
      this.loading = false
    }
  }
}
</script>
<style scoped lang="css">
#login {
  height: 50%;
  width: 100%;
  position: absolute;
  top: 0;
  left: 0;
  content: "";
  z-index: 0;
}
#bookstore_logo {
  width: 300px;
  height: 68px;
}
@media only screen and (min-width: 1200px) {
  #bookstore_logo {
    width: 300px;
    height: 68px;
  }
}
@media only screen and (min-width: 960px) and (max-width: 1199px) {
  #bookstore_logo {
    width: 300px;
    height: 68px;
  }
}
@media only screen and (min-width: 859px) and (max-width: 959px) {/*150%*/
  #bookstore_logo {
    width: 400px;
    height: 80px;
  }
}
@media only screen and (min-width: 799px) and (max-width: 858px) {/*175%*/
  #bookstore_logo {
    width: 400px;
    height: 90px;
  }
}
@media only screen and (min-width: 600px) and (max-width: 798px) {/*200%*/
  #bookstore_logo {
    width: 300px;
    height: 68px;
  }
}
@media only screen and (min-width: 480px) and (max-width: 599px) {/*250%*/
  #bookstore_logo {
    width: 400px;
    height: 90px;
  }
}
@media only screen and (min-width: 400px) and (max-width: 479px) {/*300%*/
  #bookstore_logo {
    width: 400px;
    height: 90px;
  }
}
@media only screen and (max-width: 399px) {/*400%*/
  #bookstore_logo {
    width: 300px;
    height: 68px;
  }
}
</style>
