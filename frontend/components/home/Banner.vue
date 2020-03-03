<template>
  <base-card dark>
    <v-img
      class="grey lighten-2"
      height="400"
      width="100%"
      :src="require('@/assets/books/banner.jpg')"
    >
      <v-layout
        fill-height
        align-center
        pa-3
      >
        <v-flex
          xs12
          md7
          offset-md5
        >
          <h1 class="display-3 font-weight-light">
            The biggest E-Book Store
          </h1>
          <div class="subheading text-uppercase pl-2 mb-4">
            Acquire Knowledge, One Book at a time
          </div>
          <v-btn
            v-if="!isAuthenticated"
            color="primary"
            depressed
            rounded
          >
            Sign Up
          </v-btn>
          <v-btn
            v-if="!isAuthenticated"
            color="primary"
            depressed
            rounded
            @click.native="$router.push('auth/login')"
          >
            Log In
          </v-btn>
        </v-flex>
      </v-layout>
    </v-img>
  </base-card>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  computed: {
    ...mapGetters(['isAuthenticated'])
  }
}
</script>
