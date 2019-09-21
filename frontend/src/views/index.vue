<template>
    <v-sheet>
    <v-container>
        <v-row justify="center">
            <v-col cols="10" lg="8">
                <TaskList />
            </v-col>
        </v-row>
    </v-container>
    </v-sheet>
</template>
<script>
import TaskList from "./TaskList"
export default {
    components: {
        TaskList
    }
}
</script>