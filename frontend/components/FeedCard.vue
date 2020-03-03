<template>
  <v-flex
    xs12
    :class="classes"
  >
    <base-card
      :height="value.prominent ? 450 : 350"
      color="grey lighten-1"
      dark
      href="#!"
    >
      <v-img
        v-if="value.cover!==null"
        :src="value.cover"
        height="100%"
        gradient="rgba(0, 0, 0, .42), rgba(0, 0, 0, .42)"
      >
        <v-layout
          v-if="!value.prominent"
          fill-height
          wrap
          text-xs-right
          ma-0
        >
          <v-flex xs12>
            <v-chip
              label
              class="mx-0 mb-2 text-uppercase"
              color="grey darken-3"
              text-color="white"
              small
              @click.stop=""
            >
              {{ value.category }}
            </v-chip>
            <h3 class="title font-weight-bold mb-2">
              {{ value.title }}
            </h3>
            <div v-if="value.author" class="caption">
              {{ value.author.author.first_name }} {{ value.author.author.last_name }}<br>{{ value.publish_date }}
            </div>
          </v-flex>
          <v-flex align-self-end>
            <v-chip
              v-if="isAuthenticated"
              class="text-uppercase ma-0"
              color="primary"
              label
              small
              @click.stop="bookPurchase('purchased')"
            >
              Buy Now
            </v-chip>
            <v-chip
              v-if="isAuthenticated"
              class="text-uppercase ma-0"
              color="primary"
              label
              small
              @click.stop="bookPurchase('rented')"
            >
              Rent Now
            </v-chip>
          </v-flex>
        </v-layout>
      </v-img>
    </base-card>
  </v-flex>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  props: {
    size: {
      type: Number,
      required: true
    },
    value: {
      type: Object,
      default: () => ({})
    }
  },

  computed: {
    ...mapGetters(['isAuthenticated']),
    classes () {
      return {
        md6: this.size === 2,
        md4: this.size === 3
      }
    }
  },
  methods: {
    bookPurchase (status) {
      const me = this
      const payload = { book: this.value.id, status }
      this.$axios.post('books/bookpurchase', payload)
        .then(function (response) {
          me.$notifier.showMessage({ content: 'Book Added to your Library', color: 'success' })
        })
        .catch(function () {
          me.$notifier.showMessage({ content: 'Error adding book', color: 'error' })
        })
    }
  }
}
</script>

<style>
.v-image__image {
  transition: .3s linear;
}
</style>
