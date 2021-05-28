<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="10" lg="8">
        <TaskList />
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import TaskList from "./TaskList"
export default {
  components: {
    TaskList
  }
}
</script>
