<template>
  <div id="home">
    <books>
      <banner />
    </books>
    <about />

    <subscribe />

    <social />
  </div>
</template>
<script>
export default {
  name: 'Home',

  components: {
    About: () => import('@/components/home/About'),
    Books: () => import('@/components/home/Books'),
    Banner: () => import('@/components/home/Banner'),
    Social: () => import('@/components/home/Social'),
    Subscribe: () => import('@/components/home/Subscribe')
  }
}
</script>
