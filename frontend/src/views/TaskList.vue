<template>
    <div>
        <v-sheet class="pa-5" color="grey lighten-3">
            <v-card height="780">
                <v-card-title>
                    <v-row>
                    <span class="display-4 font-weight-black mx-4">19</span>
                    <v-layout column justify-center wrap>
                        <span class="display-1 font-weight-bold">SEP</span>
                        <span class="display-1 font-weight-bold">2019</span>
                    </v-layout>
                        <v-layout column justify-space-around align-end>
                            <span class="display-1 grey--text text--lighten-1 font-weight-bold pr-8"></span>
                            <v-btn class="ma-5" color="info" fab outlined @click.stop="toggle">
                                <v-icon>mdi-plus</v-icon>
                            </v-btn>
                            <Editor :editor="types[1]" :dialog="dialog" @closed="toggle"></Editor>
                        </v-layout>
                    </v-row>
                </v-card-title>
                <v-divider></v-divider>

                <v-container fluid>
                    <v-list v-for="(task, index) in tasks" :key="index" max-height="625" class="overflow-y-auto">
                    <v-list-item>
                        <v-col cols="1">
                            <v-checkbox color="teal"></v-checkbox>
                        </v-col>

                        <v-list-item-content>
                            <v-row>
                                <v-col cols="6">
                                    <v-list-item-title class="pl-3">{{ task.title }}</v-list-item-title>
                                    <v-list-item-subtitle class="pl-3">{{ task.description }}</v-list-item-subtitle>
                                </v-col>
                                    <v-spacer></v-spacer>
                                <v-col cols="3">
                                    <v-layout column justify-center>
                                        <span>~ {{ task.date }}</span>
                                    </v-layout>
                                </v-col>
                            </v-row>
                        </v-list-item-content>
                        <v-list-item-action>
                            <v-btn icon @click.stop="toggle">
                                <v-icon>mdi-pencil</v-icon>
                            </v-btn>
                            <Editor :editor="types[0]" :dialog="dialog" @closed="toggle"></Editor>
                        </v-list-item-action>
                    </v-list-item>
                </v-list>
                <!-- <v-data-table
                    v-model="selected"
                    :headers="headers"
                    :items="tasks"
                    itemkey="id"
                    show-select
                >
                </v-data-table> -->

                </v-container>
                
            </v-card>
        </v-sheet>
    </div>
</template>

<script>
import Editor from "./TaskEditor"
import axios from 'axios'
export default {
    data () {
        return {
            tasks: '',
            selected: [],
            headers: [
                {
                    text: 'id',
                    align: 'left',
                    sortable: 'false',
                    value:'id'
                },
                {
                    text: 'title',
                    value: 'title'
                },
                {
                    text: 'date',
                    value: 'date'
                },
                {
                    text: 'tag',
                    value: 'tag'
                }
            ],
            types: [
                'edit',
                'Add'
            ],
            dialog: false
        }
    },
    components: {
        Editor
    },
    methods: { 
        toggle: function () {
            this.dialog = !this.dialog
        },
        window:onload = function() {
            
        }
    },
    mounted() {
        const path = 'http://localhost:5000/tasks/get'
            var self = this
            axios.get(path)
            .then(respons => {
                console.log(respons.data)
                this.tasks = respons.data
                console.log(tasks)
            })
            .catch(error => {
                console.log(error)
            })
    },
}
</script>
<style>

</style>