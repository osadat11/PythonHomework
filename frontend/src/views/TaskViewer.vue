<template>
    <div>
        <v-row justify="center">
        <v-dialog v-model="dialog" persistent max-width="600px">
            <v-card>
            <v-card-title>
                タスクの詳細
            </v-card-title>
            <v-card-text>
                <v-container>
                <v-row>
                    <v-col cols="12">
                    <v-text-field 
                        label="タイトル" 
                        v-model="title" 
                        ></v-text-field>
                    </v-col>
                    <v-col cols="12">
                        <v-textarea
                            label="このタスクの説明"
                            v-model="description"
                            :counter="180"
                            editable=false
                        ></v-textarea>
                    </v-col>

                    <v-col cols="12">
                        <v-list-item-title class="pl-3">{{ this.title }}</v-list-item-title>
                        <v-list-item-subtitle class="pl-3" v-if="(this.due_t, this.due_t)!=empty && (this.due_t, this.due_t)!=null">期限 : {{ this.due_d }}&nbsp;&nbsp;{{ this.due_t}}</v-list-item-subtitle>
                        <v-list-item-subtitle class="pl-3" v-else>&nbsp;</v-list-item-subtitle>
                    </v-col>

                    <v-subheader class="pl-2">優先度</v-subheader>
                    <v-col cols="12">
                        {{ this.priority }}
                    </v-col>
                </v-row>
                </v-container>
                <v-divider></v-divider>
            </v-card-text>
            <v-card-actions>
                <div class="flex-grow-1"></div>
                <v-btn color="blue darken-1" text @click="close()">閉じる</v-btn>
            </v-card-actions>
            </v-card>
        </v-dialog>
        </v-row>
    </div>
</template>
<script>
import axios from 'axios'
import { isString } from 'util'
export default {
    data: () => ({
        id: '',
        title: '',
        description: '',
        due_t:'',
        due_d: '',
        priority: 0,
        done:'',
        dialog : false,
        priorities: [
            'なし',
            '低',
            '中',
            '高'
        ],
        empty:""
    }),
    methods: {
        open(data) {
            this.dialog = true

            this.id = data.id
            this.title = data.title
            this.due_d = data.due_d
            this.due_t = data.due_t
            this.priority = data.priority
            this.description = data.description
            this.done = data.done
        },
        close(){
            this.reset()
            this.dialog = false
        },
        reset(){
            this.id = null
            this.title = null
            this.due_d = null
            this.due_t = null
            this.priority = null
            this.description = null
            this.done = null
            return 0
        }
    }
}
</script>