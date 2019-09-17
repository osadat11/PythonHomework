<template>
    <div>
        <v-sheet class="pa-6" color="grey lighten-3">
            <v-card height="780">
                <v-card-title>
                    <v-row>
                    <span class="display-4 font-weight-black mx-4">09</span>
                    <v-layout column justify-center wrap>
                        <span class="display-1 font-weight-bold">SEP</span>
                        <span class="display-1 font-weight-bold">2019</span>
                    </v-layout>
                        <v-layout column justify-space-around align-end>
                            <span class="display-1 grey--text text--lighten-1 font-weight-bold pr-8">FRIDAY</span>
                        </v-layout>
                    </v-row>
                </v-card-title>
                <v-divider></v-divider>

                <v-container fluid>
                    <v-list
                    max-height="625"
                    class="overflow-y-auto"
                >
                    <v-list-item>
                        <v-checkbox color="teal" v-on="c"></v-checkbox>

                        <v-list-item-content>
                            <v-row>
                                <v-col>
                                    <v-list-item-title class="pl-3">Title</v-list-item-title>
                                    <v-list-item-subtitle class="pl-3">Description</v-list-item-subtitle>
                                </v-col>
                                    <v-spacer></v-spacer>
                                <v-col>
                                    <v-layout column justify-center>
                                        <span>Date</span>
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
                </v-container>
                
            </v-card>
        </v-sheet>
    </div>
</template>

<script>
import Editor from "./TaskEditor"
export default {
    data: () => {
        return {
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
        }
    }
}
</script>

<style>

</style>