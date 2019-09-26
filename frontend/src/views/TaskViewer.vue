<template>
    <div>
        <v-row justify="center">
        <v-dialog v-model="dialog" persistent max-width="600px">
            <v-card class="mx-auto">
                <v-img
                    class="white--text"
                    height="200"
                    style="background-image: linear-gradient(to top, #4481eb 0%, #04befe 100%);"
                >
                    <v-card-title class="display-1 align-end fill-height font-weight-bold">
                        {{ this.title }}
                    </v-card-title>
                </v-img>
            <v-card-text>
                <v-container>
                <v-row>
                    <v-card-text>
                        <span>タスクの説明</span><br>
                        <span class="text--primary body-1">{{ this.description }}</span>
                    </v-card-text>

                    <v-card-text>
                        <span>タスクの期限</span><br>
                        <span v-if="this.due_d!=null" class="text--primary">~&nbsp;</span>
                        <span class="text--primary body-1">{{this.due_d}}&nbsp;{{this.due_t}}</span>

                    </v-card-text>

                    <v-card-text>
                        <span>優先度</span><br>
                        <span v-if="this.priority==0" color="" class="text--primary font-weight-thin">{{this.priorities[this.priority]}}</span>
                        <span v-else-if="this.priority==1" class="cyan--text text--accebt-3 font-weight-thin display-1">{{this.priorities[this.priority]}}</span>
                        <span v-else-if="this.priority==2" class="orange--text text--accent-4 font-weight-thin display-1">{{this.priorities[this.priority]}}</span>
                        <span v-else-if="this.priority==3" class="red--text text--accent-3 font-weight-thin display-1">{{this.priorities[this.priority]}}</span>
                    </v-card-text>
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
import moment from 'moment'
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
            '指定なし',
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
            if(data.due_d != ""){
                var afterDate = moment(data.due_d).format('YYYY年MM月DD日')
            }
            this.due_d = afterDate
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