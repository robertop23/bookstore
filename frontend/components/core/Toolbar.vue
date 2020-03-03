<template>
  <v-app-bar
    app
    flat
  >
    <v-app-bar-nav-icon
      class="hidden-md-and-up"
      @click="toggleDrawer"
    />
    <v-container
      mx-auto
      py-0
    >
      <v-layout>
        <v-img
          :src="require('@/assets/bookstore_logo.png')"
          class="mr-5"
          contain
          height="48"
          width="48"
          max-width="48"
          @click="$vuetify.goTo(0)"
        />
        <v-btn
          v-for="(link, i) in links"
          :key="i"
          class="ml-0 hidden-sm-and-down"
          text
          @click="onClick($event, link)"
        >
          {{ link.text }}
        </v-btn>
        <v-spacer />
        <v-text-field
          append-icon="mdi-magnify"
          flat
          hide-details
          solo-inverted
          style="max-width: 500px;"
        />
        <v-menu v-if="$auth.$state.user" bottom left offset-y>
          <template v-slot:activator="{ on }">
            <v-card flat dense color="#f5f5f5">
              <v-list-item v-on="on">
                <v-list-item-avatar>
                  <img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="User">
                </v-list-item-avatar>

                <v-list-item-content />
              </v-list-item>
            </v-card>
          </template>

          <v-card>
            <v-list min-width="150">
              <v-subheader>{{ $auth.$state.user.username }}</v-subheader>

              <v-list-item to="/account">
                <v-list-item-icon>
                  <v-icon>fa fa-user-cog</v-icon>
                </v-list-item-icon>
                <v-list-item-title>Account</v-list-item-title>
              </v-list-item>
              <v-divider />

              <v-list-item @click="$auth.logout()">
                <v-list-item-icon>
                  <v-icon>fa fa-sign-out-alt</v-icon>
                </v-list-item-icon>
                <v-list-item-title>Logout</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-card>
        </v-menu>
      </v-layout>
    </v-container>
  </v-app-bar>
</template>

<script>
// Utilities
import {
  mapState,
  mapMutations
} from 'vuex'

export default {
  computed: {
    ...mapState(['links'])
  },

  methods: {
    ...mapMutations(['toggleDrawer']),
    onClick (e, item) {
      e.stopPropagation()
      if (item.to || !item.href) { return }
      this.$vuetify.goTo(item.href)
    }
  }
}
</script>
