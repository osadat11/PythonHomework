<template>
  <v-app>
    <Header />
    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>

<script>
import Header from "./components/Header"
export default {
  name: 'App',
  components: {
    Header
  }
};
</script>

<style>
#app {
  background-image: linear-gradient(-225deg, #FFFEFF 0%, rgb(233, 233, 233) 100%);
}
</style>
