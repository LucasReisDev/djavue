<template>
  <div class="home">
    <h1>Djavue</h1>
    <HelloWorld msg="Djavue TEST"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  }
}
</script>
