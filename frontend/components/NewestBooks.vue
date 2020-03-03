<template>
  <v-container pa-0>
    <base-subheading>Newest Books</base-subheading>
    <v-layout
      v-for="(book, i) in books.slice(0, 3)"
      :key="i"
      align-center
      mb-2
    >
      <v-flex
        xs12
        d-flex
      >
        <v-img
          v-if="book.cover!==null"
          :src="book.cover"
          class="mr-3"
          height="36"
          max-width="36"
        />
        <v-img
          v-else
          src="/assets/books/empty_book.png"
          class="mr-3"
          height="36"
          max-width="36"
        />

        <div>
          <div class="subheading">
            {{ book.title }}
          </div>
          <div class="caption">
            {{ book.publish_date }}
          </div>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
// Utilities
import {
  mapState
} from 'vuex'

export default {
  computed: {
    ...mapState(['books'])
  }
}
</script>
