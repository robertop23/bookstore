<template>
  <v-container
    id="social"
    tag="section"
    grid-list-xl
  >
    <v-layout wrap>
      </v-flex>
      <v-flex
        xs12
        md6
      >
        <newest-books />
      </v-flex>
      <v-flex
        xs12
        md6
      >
        <categories />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  components: {
    NewestBooks: () => import('@/components/NewestBooks'),
    Categories: () => import('@/components/Categories')
  }
}
</script>
